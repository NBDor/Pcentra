from django.test import TestCase
from .models import Url

class URLTests(TestCase):
    def test_create_page(self):
        response = self.client.post("/s/create", {'full_link':'https://ravkavonline.co.il'})
        self.assertEqual(response.status_code, 200)


    def test_redirect_page(self):
        shortcut_response = self.client.post("/s/create", {'full_link':'https://ravkavonline.co.il'})
        shortcut = Url.objects.get(id=1).shortcut
        response = self.client.get("/s/"+shortcut)
        self.assertEqual(response['Location'], 'https://ravkavonline.co.il')

    def test_none_existing_shortcut(self):
        none_existing_url = "123\><+&^%@"
        response = self.client.get("/s/"+none_existing_url)
        self.assertEqual(response.status_code, 404)
        
