from django.test import TestCase
from createuser.models import loginprofile, Book


class TestModels(TestCase):
    def test_book_has_an_author(self):

        test = loginprofile.objects.create(first_name="Philip", last_name="K. Dick")
        test1 = loginprofile.objects.create(first_name="Juliana", last_name="Crain")
        loginprofile.set([test.pk, test1.pk])
        self.assertEqual(loginprofile.authors.count(), 2)