from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from http import HTTPStatus
from rest_framework.decorators import api_view
from webapp.models import Message
from .serializers import MessageSerializer
from .constants import WEBHOOK_URL, NOT_FOUND
import requests
import json
import os
import uuid

file_path = os.path.join(settings.MEDIA_ROOT, 'temp_data/')
os.makedirs(file_path, exist_ok=True)


def landing_page(request):
    """
    Renders home page with text area and send button
    """
    response = render(request, 'webapp/home.html', {
        'url': settings.URL,
    })
    return response


def list_display(request):
    """
    Renders text lists
    """
    messages = Message.objects.all()
    response = render(request, 'webapp/list_display.html', {
        'messages': messages,
    })
    return response


@api_view(['GET', 'POST', 'DELETE'])
def msg_api(request, pk=None) -> JsonResponse:
    """
    Api view for message text functionality.
    Supports GET,POST and DELETE requests.
    Returns JsonResponse
    """
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)
        # save text to database
        serializer.save()

        file = file_path + str(uuid.uuid4()) + settings.FILE_EXT
        data = json.dumps(serializer.data)

        # write text to a file in media/temp_data/
        with open(file, 'w+') as f:
            f.write(data)

        # call webhook url and send response
        req = requests.post(settings.WEBHOOK_URL, data=data)
        resp_status = HTTPStatus.CREATED if req.status_code == 200 else req.status_code
        return JsonResponse(serializer.data, status=resp_status)

    elif request.method == 'GET':
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        try:
            message = Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            return JsonResponse({'message': NOT_FOUND}, status=HTTPStatus.NOT_FOUND)
        message.delete()
        return JsonResponse({'message': 'Success'}, status=HTTPStatus.NO_CONTENT)
