Step1:

Create a models.py with following code
from django.db import models
class Languages(models.Model):
name = models.CharField(max_length=20)
def __str__(self):
return self.name
# Create your models here.
class Projects(models.Model):
topic = models.CharField(max_length = 40)
languages = models.ManyToManyField(Languages,related_name='languages')
duration_days = models.IntegerField()
def __str__(self):
return self.topic


Step2: Write the urls.py(app)
from django.urls import path, include
from . import views
urlpatterns = [
path('tracking/<int:pk>/', views.viewProjectDetails.as_view(),
name='project_detail'),
path('tracking/', views.ProjectList.as_view())
]



Step3: Write the urls.py(project)
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('trackingapp.urls')),
]


Step4: Views.py
from django.shortcuts import render
from .models import Projects, Languages
from django.views.generic import DetailView, ListView
# Create your views here.
class viewProjectDetails(DetailView):
template_name = "trackingapp/project_details.html"
model = Projects
context_object_name = "projects"
class ProjectList(ListView):
template_name = "trackingapp/project_list.html"
model = Projects
context_object_name = "projects"


Step5: Admin.py(in app)
from django.contrib import admin
from .models import Projects, Languages
# Register your models here.
admin.site.register(Projects)
admin.site.register(Languages)


Step6: Create templates folder in app and within it folder named trackingapp
Create two templates project_list.html
<html>
<body>
<h1>Project List</h1>
<ul>
{% for project in projects %}
<li><a href="{% url 'project_detail' pk=project.id
%}">{{project.topic}}</a></li>
{% endfor %}
</ul>
</body>
</html>

Project_details.html
<html>
<body>
<h1>Title:{{projects.topic}}</h1>
<br/>
<h2>Languages: {% for language in projects.languages.all %}
{{ language.name }}<br/>
{% endfor %}
</h2>
<br/>
<h2>
Duration(days):{{projects.duration_days}}
</h2>
</body>
</html>



Step7: Make migrations and Migrate
py manage.py makemigrations
py manage.py migrate
Step8: Create SuperUser and login through it:
Py manage.py createsuperuser
Add a few languages and Projects
Step9: py manage.py runserver
