from createuser import urls
from django.test import SimpleTestCase

from django.urls import resolve, reverse
from createuser.views import registerUsers, Login , taskFilesList, scenelevelattributes, objectlevelattributes, projectFiles

class TestUrls(SimpleTestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, Login)

    def test_add_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registerUsers)

    def test_tasks_url(self):
        url = reverse('tasks')
        self.assertEqual(resolve(url).func, taskFilesList)

    def test_scenLevel_url(self):
        url = reverse('sceneLevel')
        self.assertEqual(resolve(url).func, scenelevelattributes)

    def test_objectLevel_url(self):
        url = reverse('objectLevel')
        self.assertEqual(resolve(url).func, objectlevelattributes)

    def test_projectFiles_url(self):
        url = reverse('project')
        self.assertEqual(resolve(url).func, projectFiles)