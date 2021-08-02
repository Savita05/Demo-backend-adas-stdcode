
from django.http import response
from django.urls import reverse
from .test_setup import TestsetUp
from createuser.models import loginprofile

#description----
#pylint static code analysis
class TestViews(TestsetUp):       

    def test_project_list_get(self):   
        response = self.client.get(self.projectlist_url)
        self.assertEquals(response.status_code, 200)
#assert functionalities google test

    def test_registeredusers_get(self):
        response = self.client.get(self.registerdUsers_url)
        self.assertEquals(response.status_code, 200)
    
    def test_registerusers_post(self):
        res = self.client.post(self.registerdUsers_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()
       # self.assertEqual(res.data['firstName'], self.user_data['firstName'])
        self.assertEquals(res.status_code, 200)

    def test_correct_login(self):
        self.client.post(self.registerdUsers_url , self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data , format ="json")
        # import pdb
        # pdb.set_trace()
        self.assertEquals(res.status_code, 200)

    
    def test_api_can_delete_RegisteredUser(self):
        """Test the api can delete a users."""
        response = self.client.delete(
            reverse('register'),
            format='json',
            follow=True)
        # import pdb
        # pdb.set_trace()
        self.assertEquals(response.status_code, 204)

#for bigger data set
    
   

           