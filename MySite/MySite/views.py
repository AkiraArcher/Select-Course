# -*- coding=UTF-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from APP.models import Student, Course, Select
from collections import defaultdict

import APP.views
# Create your views here.


def index(request):
    students_num = Student.objects.count()
    courses_num = Course.objects.count()
    selects_num = Select.objects.count()
    teachers_num = Course.objects.values('teacher').distinct().count()
    return render(request, 'index.html', {'students_num': students_num,
                                          'courses_num': courses_num,
                                          'selects_num': selects_num,
                                          'teachers_num': teachers_num})


def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})


def student_add(request):
    return render_to_response('student_add.html', context=RequestContext(request))


def student_mod(request):
    return render(request, 'student_mod.html', {})


def student_find1(request):
    if request.method == 'POST':
        cd = request.POST
        stu = Student.objects.get_object(sid=cd['key'])
        if stu is None:
            stu = Student.objects.get_object(sname=cd['key'])
        if stu is None:
            return render(request, 'student_mod.html', {'code': -1})
        else:
            return render(request, 'student_mod.html', {'code': 0, 'stu': stu})
    else:
        return render_to_response('student_mod.html', context=RequestContext(request))


def student_del(request):
    return render(request, 'student_del.html', {})


def student_find2(request):
    if request.method == 'POST':
        cd = request.POST
        stu = Student.objects.get_object(sid=cd['key'])
        if stu is None:
            stu = Student.objects.get_object(sname=cd['key'])
        if stu is None:
            return render(request, 'student_del.html', {'code': -1})
        else:
            return render(request, 'student_del.html', {'code': 0, 'stu': stu})
    else:
        return render_to_response('student_del.html', context=RequestContext(request))


def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})


def course_add(request):
    return render_to_response('course_add.html', context=RequestContext(request))


def course_mod(request):
    return render(request, 'course_mod.html', {})


def course_find1(request):
    if request.method == 'POST':
        cd = request.POST
        cou = Course.objects.get_object(cid=cd['key'])
        if cou is None:
            cou = Student.objects.get_object(cname=cd['key'])
        if cou is None:
            return render(request, 'course_mod.html', {'code': -1})
        else:
            return render(request, 'course_mod.html', {'code': 0, 'cou': cou})
    else:
        return render_to_response('course_mod.html', context=RequestContext(request))


def course_del(request):
    return render(request, 'course_del.html', {})


def course_find2(request):
    if request.method == 'POST':
        cd = request.POST
        cou = Course.objects.get_object(cid=cd['key'])
        if cou is None:
            cou = Student.objects.get_object(cname=cd['key'])
        if cou is None:
            return render(request, 'course_del.html', {'code': -1})
        else:
            return render(request, 'course_del.html', {'code': 0, 'cou': cou})
    else:
        return render_to_response('course_del.html', context=RequestContext(request))


def select(request):
    selects = Select.objects.all()
    return render(request, 'select.html', {'selects': selects})


def select_add(request):
    return render_to_response('select_add.html', context=RequestContext(request))


def select_mod(request):
    return render(request, 'select_mod.html', {})


def select_find1(request):
    if request.method == 'POST':
        cd = request.POST
        stu = Student.objects.get_object(sid=cd['key1'])
        cou = Course.objects.get_object(cid=cd['key2'])
        sel = Select.objects.get_object(student=stu, course=cou)
        if sel is None:
            return render(request, 'select_mod.html', {'code': -1})
        else:
            return render(request, 'select_mod.html', {'code': 0, 'sel': sel})
    else:
        return render_to_response('select_mod.html', context=RequestContext(request))


def select_del(request):
    return render(request, 'select_del.html', {})


def select_find2(request):
    if request.method == 'POST':
        cd = request.POST
        stu = Student.objects.get_object(sid=cd['key1'])
        cou = Course.objects.get_object(cid=cd['key2'])
        sel = Select.objects.get_object(student=stu, course=cou)
        if sel is None:
            return render(request, 'select_del.html', {'code': -1})
        else:
            return render(request, 'select_del.html', {'code': 0, 'sel': sel})
    else:
        return render_to_response('select_del.html', context=RequestContext(request))


def student_query(request):
    return render(request, 'student_query.html', {})


def course_query(request):
    return render(request, 'course_query.html', {})


def select_query(request):
    return render(request, 'select_query.html', {})


# 能够统计出班级的加权平均成绩
def class_table(request):
    result = {}
    students = Student.objects.all()
    cnt_credit = defaultdict(lambda: 0)
    cnt_creditscore = defaultdict(lambda: 0)
    for s in students:
        selects = Select.objects.filter(student=s)
        for se in selects:
            c = se.course
            cnt_credit[s.squad] += c.credit
            cnt_creditscore[s.squad] += c.credit * se.score
    for kc, vc in cnt_credit.iteritems():
        for kcs, vcs in cnt_creditscore.iteritems():
            if kc == kcs and vc != 0:
                result[kc] = float(vcs / vc)
    return render(request, 'class_table.html', {'ans': zip(result.keys(), result.values())})#{'keys': result.keys(), 'vals': result.values()})


# 课程的成绩分布（不及格，60－69，70－79，80－89，90－99，满分）
def course_table(request):
    result = {}
    courses = Course.objects.all()
    for c in courses:
        cname = c.cname
        selects = Select.objects.filter(course=c)
        cnt = defaultdict(lambda: 0)
        for se in selects:
            if se.score < 60:
                cnt['a'] += 1
            elif se.score < 70:
                cnt['b'] += 1
            elif se.score < 80:
                cnt['c'] += 1
            elif se.score < 90:
                cnt['d'] += 1
            elif se.score < 100:
                cnt['e'] += 1
            else:
                cnt['f'] += 1
        result[cname] = cnt
    return render(request, 'course_table.html', {'ans': zip(result.keys(), result.values())})
