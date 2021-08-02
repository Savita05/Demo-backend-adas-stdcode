from django.conf.urls import url
from django.urls import path
from .views import *
from createuser import views 
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
# url(r'registration/$', RegisterUser.as_view()),


# url(r'taskfileslist/$', TaskFiles.as_view()),
# url(r'getTaskFilesList/$', GetTaskFilesList.as_view()),
# url(r'userroles/$', UserRoles.as_view()),
# url(r'objectlevel/$', ObjectLevel.as_view()),
# url(r'getObjectlevel/$', GetObjectLevel.as_view()),
# url(r'scenelevel/$', SceneLevelQuery.as_view()),
# url(r'getScenelevel/$', GetSceneLevel.as_view()),
# url(r'addProjectFiles/$', AddProjectFiles.as_view()),
# url(r'getProjectFiles/$', GetAllProjectsDetails.as_view()),

url(r'registerUsers/$', views.registerUsers , name="register"),
url(r'registerUsers_id/(?P<pk>[0-9]+)$', views.registerdUsers_id),

url(r'getuser/$', Getuser.as_view(), name="getresgisterdusers"),
url(r'loginuser/$', Login.as_view(), name="login"),

url(r'taskfilesAttributes/$', views.taskFilesList , name = "tasks"),
url(r'taskfilesAttributes_id/(?P<pk>[0-9]+)$', views.taskFilesList_id),
url(r'gettaskfilesfilteredonprojects/(?P<project_name>)$', views.gettasksfilteredonProjects),

url(r'objectLevelAttributes/$', views.objectlevelattributes,  name ="objectLevel"),
url(r'objectLevelAttributes_id/(?P<pk>[0-9]+)$', views.objectlevelattributes_id),

url(r'sceneLevelAtrributes/$', views.scenelevelattributes, name = "sceneLevel"),
url(r'sceneLevelAttributes_id/(?P<pk>[0-9]+)$', views.scenelevelattributes_id),

url(r'projectFiles/$', views.projectFiles, name="project"),
url(r'projectFiles_id/(?P<pk>[0-9]+)$', views.projectFiles_id),

url(r'getProjectFilesname/$', GetProjectName.as_view()),
url(r'getProjectFilesdetails/(?P<project_name>)$', views.getProjectDetails),

url(r'objectCategories/$', views.getobjectCategories),
url(r'objectcategorieswithid/(?P<pk>[0-9]+)$', views.getobjectCategories_id),

url(r'getAnnotationImageFile/(?P<File_Name>)(?P<project_name>)$', views.getAnnotationImageFile),
url(r'uploadAnnotationimages/', views.uploadimages)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)