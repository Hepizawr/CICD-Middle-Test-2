from django.test import TestCase
from django.urls import reverse
from gallery.models import Image


# Create your tests here.
class ModelImageTests(TestCase):
    def setUp(self):
        Image.objects.create(title="TestImage1", image="media/gallery_images/00016-3918825854.png",
                             created_date="2023-05-23", age_limit="10")

    def test_get_image(self):
        image = Image.objects.get(title="TestImage1")
        self.assertTrue(image)

    def test_image_age_limit(self):
        image = Image.objects.get(title="TestImage1")
        self.assertTrue(image.age_limit == 10)

    def test_get_image_at_main_page(self):
        image = Image.objects.get(title="TestImage1")
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["images"], [image])
