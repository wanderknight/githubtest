from django.test import TestCase
from .models import Book, Author, BookAuthor


# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        b1 = Book.objects.create(title='b1')
        b2 = Book.objects.create(title='b2')
        b1.save()
        b2.save()

    def test_book_model(self):
        result = Book.objects.get(title='b1')
        print(result.title)
        self.assertEqual(result.title, 'b1')


if __name__ == '__main__':
    modelTestCase = ModelTest()
    modelTestCase.test_book_model()