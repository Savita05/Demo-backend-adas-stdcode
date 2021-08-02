from rest_framework.test import APITestCase
from django.urls import reverse
# from Faker import faker


class TestsetUp(APITestCase):
    def setUp(self):

        
        self.registerdUsers_url = reverse('register')
        self.login_url = reverse('login')
        self.projectlist_url = reverse('project')
        # self.fake = Faker()

        self.user_data={
            'firstName':"name",
            'password': "savita",
            'role':"maker"  
        }

        #Fixtures
        return super().setUp()

    def tearDown(self):
        return super().tearDown()