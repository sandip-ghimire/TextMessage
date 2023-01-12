from rest_framework import serializers
from webapp.models import Message


class MessageSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    date = serializers.DateTimeField(format="%d-%b-%Y", required=False, read_only=True, allow_null=True)

    class Meta(object):
        model = Message
        fields = ('text', 'date')
