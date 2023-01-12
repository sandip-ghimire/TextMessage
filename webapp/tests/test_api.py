from django.test.testcases import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from faker import Faker
import django
django.setup()


class TextMessageTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_faulty_post(self):
        request_data = {
            'text': ''
        }
        resp = self.client.post(reverse('msg_list'), request_data)
        self.assertEqual(resp.status_code, 400)  # Bad request

    def test_correct_post(self):
        faker = Faker()
        request_data = {
            'text': faker.text()
        }
        resp = self.client.post(reverse('msg_list'), request_data)
        self.assertEqual(resp.status_code, 201)  # Success
