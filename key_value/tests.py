from django.test import TestCase
from django.test import Client
from key_value.views import stored_key_values


class SetKeyValueTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_set_key_value(self):
        """Test that the key and value are store in memory"""
        self.client.get('/set/?greeting=hello')
        self.assertIn('greeting', stored_key_values)

    def test_set_key_value_with_wrong_url(self):
        """Test that the key and value are not store in memory if the url is wrong"""
        self.client.get('/set/?hello')
        self.assertNotIn('hello', stored_key_values)

    def test_get_key_value(self):
        """Test that the value corresponding to the provided key is returned"""
        self.client.get('/set/?greeting=hello')
        response = self.client.get('/get/?key=greeting')
        self.assertIn(b'hello', response.content)

    def test_get_key_value_with_wrong_url(self):
        """Test that the if the url is wrong the value is not returned"""
        response = self.client.get('/get/?greeting')
        response_msg = response.content
        same_msg = response_msg == b'To retrieve a key value you must do key=key_name.'
        self.assertTrue(same_msg)
