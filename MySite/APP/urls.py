from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from . import views


urlpatterns = [
    url(r'^adds$', views.StudentAddView, name='add_student'),
    url(r'^dels$', views.StudentDelView, name='del_student'),
    url(r'^mods$', views.StudentModView, name='mod_student'),

    url(r'^addc$', views.CourseAddView, name='add_course'),
    url(r'^delc$', views.CourseDelView, name='del_course'),
    url(r'^modc$', views.CourseModView, name='mod_course'),

    url(r'^addsc$', views.SelectAddView, name='add_select'),
    url(r'^delsc$', views.SelectDelView, name='del_select'),
    url(r'^modsc$', views.SelectModView, name='mod_select'),

    url(r'^questu$', views.QueryStudentView, name='query_student'),
    url(r'^quesco$', views.QuerySelectView, name='query_select'),
    url(r'^quecou$', views.QueryCourseView, name='query_course'),

    url(r'^stastu$', views.StudentStaticView, name='static_student'),
    url(r'^avesc$', views.CourseAverageView, name='average_course'),

    url(r'^stacla$', views.ClassStaticView, name='static_score'),
    url(r'^stacou$', views.CourseStaticView, name='static_course'),

]