"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from views import index, student, student_add, student_mod, student_del, student_find1, student_find2, student_query,\
                         course, course_add, course_mod, course_del, course_find1, course_find2, course_query,\
                         select, select_add, select_mod, select_del, select_find1, select_find2, select_query, \
                         class_table, course_table

from django.contrib.auth.views import login, logout

urlpatterns = [

    # front end
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^student/$', student, name='student'),
    url(r'^student_add/$', student_add, name='student_add'),
    url(r'^student_mod/$', student_mod, name='student_mod'),
    url(r'^student_del/$', student_del, name='student_del'),
    url(r'^student_find1/$', student_find1, name='student_find1'),
    url(r'^student_find2/$', student_find2, name='student_find2'),
    url(r'^student_query/$', student_query, name='student_query'),

    url(r'^course/$', course, name='course'),
    url(r'^course_add/$', course_add, name='course_add'),
    url(r'^course_mod/$', course_mod, name='course_mod'),
    url(r'^course_del/$', course_del, name='course_del'),
    url(r'^course_find1/$', course_find1, name='course_find1'),
    url(r'^course_find2/$', course_find2, name='course_find2'),
    url(r'^course_query/$', course_query, name='course_query'),

    url(r'^select/$', select, name='select'),
    url(r'^select_add/$', select_add, name='select_add'),
    url(r'^select_mod/$', select_mod, name='select_mod'),
    url(r'^select_del/$', select_del, name='select_del'),
    url(r'^select_find1/$', select_find1, name='select_find1'),
    url(r'^select_find2/$', select_find2, name='select_find2'),
    url(r'^select_query/$', select_query, name='select_query'),

    url(r'^class_table/$', class_table, name='class_table'),
    url(r'^course_table/', course_table, name='course_table'),

    # back end
    url(r'^admin/', admin.site.urls),
    url(r'APP/', include('APP.urls')),
]
