from django.test import TestCase

from django.urls import reverse

class RssIndexViewTests(TestCase):
	def test_no_feed(self):
		response = self.client.get(reverse("index"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["feed"], None)



	def test_user_feed_business(self):
		response = self.client.get(reverse("index") + "?url=https://www.wired.com/feed/category/business/latest/rss")

		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response.context["feed"], None)


	def test_user_feed_ideas(self):
		response = self.client.get(reverse("index") + "?url=https://www.wired.com/feed/category/ideas/latest/rss")

		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response.context["feed"], None)