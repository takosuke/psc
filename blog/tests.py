from django.test import TestCase
import datetime
from django.utils import timezone

from blog.models import Post

class PostMethodTests(TestCase):
    def test_was_published_recently_with_future(self):
        future_post = Post(date = timezone.now() + datetime.timedelta(days=20))
        self.assertEqual(future_post.was_published_recently(), False)



class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
