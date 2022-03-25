from django.test import TestCase
from .models import NewsModel
from django.test import SimpleTestCase


class NewsModelTest(TestCase):
    def setUp(self):
        NewsModel.objects.create(title='a title', body='a body')

    def test_news_content(self):
        news = NewsModel.objects.get(id=1)
        expected_title = f'{news.title}'
        expected_body = f'{news.body}'
        self.assertEqual(expected_body, 'a body')
        self.assertEqual(expected_title, 'a title')


class HomePageViewTest(TestCase):
    def setUp(self):
        NewsModel.objects.create(title='a title', body='a body')

    def test_view_url_exist(self):
        resp = self.client.get('/news/main/')
        self.assertEqual(resp.status_code, 200)

    def test_view_proper_template(self):
        resp = self.client.get('/news/main/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'page/news.html')
