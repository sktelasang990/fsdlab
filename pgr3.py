1. Install mysql server from oracle site in your system
2. If using sqliteDB install sqlite DB Browser for windows
3. Create a DJango Project after creating a virtual environment.
4. Execute the following command after activating the virtual environment in your project
folder.
(myworld) C:\Users\kamat\Documents\
DJangoProjs3\myworld\mysql_db>pip install mysqlclient
Collecting mysqlclient
Downloading
mysqlclient-2.2.4-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
Downloading mysqlclient-2.2.4-cp312-cp312-win_amd64.whl (203
kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━ 203.3/203.3 kB 1.5 MB/s eta 0:00:00
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.2.4
5. installing DJango in it. Via >pip install django
6. Add bin folder of mysql installation in path, then open a cmd prompt:
Launch mysql
(myworld) C:\Users\kamat\Documents\
DJangoProjs3\myworld\mysql_db>mysql -u root -p
Enter password: ****
7. Create a database
mysql> create database fruitstudent;
Query OK, 1 row affected (0.00 sec)
8. Use the created database
mysql> use fruitstudent;
Database changed
9. Exit from mysql like this
mysql> exit
Bye
10. Open the Django project created earlier in Visual Studio Code
11. In the Project Settings.py file modify the DATABASES settings to



From
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite,
'NAME': BASE_DIR / 'db.sqlite3',
}
}



To This


DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'fruitstudent',
'USER': 'root',
'PASSWORD': 'root',
'HOST': 'localhost',
'PORT': 3306,
}
}

Also optionally add ‘127.0.0.1’ in
ALLOWED_HOSTS = ["127.0.0.1" ,"localhost",]


And add the app name in INSTALLED_APPS.
12. Create an app inside django project:
(myworld) C:\Users\kamat\Documents\DJangoProjs3\myworld\mysql_db>
py manage.py startapp fruitstudent
13. Create a new folder templates within this fruitstudent folder


14. Create to templates called “db_template_fruit.html” and

“db_template_student.html”
15. In these two files have the content:

<ul>
{%for fruititem in fruits%}
<li>{{fruititem.fruit}}</li>
{% endfor %}
</ul>
<ol>
{%for student in students%}
<li>{{student.name}}</li>
{% endfor %}
</ol>
16. Models.py should have the following:

from django.db import models
# Create your models here.
Class fruitlist(models.Model):
fruit = models.CharField(max_length=30)
Class studentlist(models.Model):
name = models.CharField(max_length=40)



17. Views.py should have
from django.shortcuts import render
from .models import fruitlist, studentlist
from django.template import Template, Context
# Create your views here.
def stud_list(request):
students = studentlist.objects.all()
c1 = {'students':students}
return render(request, 'db_template_student.html', c1)
def fruit_list(request):
fruits = fruitlist.objects.all()
c2 = {'fruits':fruits}
return render(request, 'db_template_fruit.html', c2)

18. urls .py file in fruitstudent app:
from django.urls import path
from . import views
urlpatterns = [
path('students/', views.stud_list),
path('fruits/', views.fruit_list),
]

19. urls.py in mysql_db project:
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('',include('fruitstudent.urls')),
]












