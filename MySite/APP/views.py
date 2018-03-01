# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.conf.urls import url
from collections import defaultdict

import json

from .forms import StudentAddForm, StudentDelForm, StudentModForm, CourseAddForm, CourseDelForm, CourseModForm, \
    SelectAddForm, SelectDelForm, SelectModForm, QueryCourseForm, QuerySelectForm, QueryStudentForm
from .models import Student, Course, Select
# Create your views here.


def CheckCode(code):
    if int(code) == -1:
        ss = "wrong request!"
    elif int(code) == -2:
        ss = "wrong data!"
    elif int(code) == -3:
        ss = "Can't find this data in database!"
    elif int(code) == -4:
        ss = "Can't save the same data in database!"
    elif int(code) == -5:
        ss = "Message Error!"
    else:
        ss = "OK!"
    return {"code": code, "ss": ss}
    #return HttpResponse(json.dumps({"code": code, "response": ss}), content_type="application/json")


def StudentAddView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = StudentAddForm(request.POST)
        code = form.save()

    result = CheckCode(code)
    return render(request, 'student_add.html', {'code': result['code'], 'ss': result['ss']})

def StudentDelView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = StudentDelForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'student_del.html', {'code': result['code'], 'ss': result['ss']})


def StudentModView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = StudentModForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'student_mod.html', {'code': result['code'], 'ss': result['ss']})


def CourseAddView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = CourseAddForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'course_add.html', {'code': result['code'], 'ss': result['ss']})


def CourseDelView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = CourseDelForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'course_del.html', {'code': result['code'], 'ss': result['ss']})


def CourseModView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = CourseModForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'course_mod.html', {'code': result['code'], 'ss': result['ss']})


def SelectAddView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = SelectAddForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'select_add.html', {'code': result['code'], 'ss': result['ss']})


def SelectDelView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = SelectDelForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'select_del.html', {'code': result['code'], 'ss': result['ss']})


def SelectModView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = SelectModForm(request.POST)
        code = form.save()
    result = CheckCode(code)
    return render(request, 'select_mod.html', {'code': result['code'], 'ss': result['ss']})


#能够根据学生姓名或学号查询生的基本信息或所选课的情况
def QueryStudentView(request):
    if request.method != 'POST':
        code = -1
    else:
        if request.POST['sid'] == "":
            request.POST['sid'] = None
        form = QueryStudentForm(request.POST)
        ans = form.query()
        cnt = ans['selects']
        credit_sum = 0
        creditscore_sum = 0
        for se in cnt:
            c = se.course
            credit_sum += c.credit
            creditscore_sum += c.credit * se.score
        if credit_sum != 0:
            weight = float(creditscore_sum / credit_sum)
        else:
            weight = 0
        code = ans['code']
    result = CheckCode(code)
    if code > 0:
        return render(request, 'student_query.html', {"code": ans['code'], "student": ans['student'], "selects": ans['selects'], "weight": weight})
    else:
        return render(request, 'student_query.html', {'code': result['code'], 'ss': result['ss']})


#能够根据课程名称或课程编号查询课程的基本信息或该课程的选课情况
def QueryCourseView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = QueryCourseForm(request.POST)
        ans = form.query()
        code = ans['code']
        cnt = ans['selects']
        people = 0
        sum_score = 0
        for se in cnt:
            people += 1
            sum_score += se.score
        if people:
            avg = float(sum_score / people)
        else:
            avg = 0
    result = CheckCode(code)
    if code > 0:
        return render(request, 'course_query.html', {"code": ans['code'], "course": ans['course'], "selects": ans['selects'], "avg": avg})
    else:
        return render(request, 'course_query.html', {'code': result['code'], 'ss': result['ss']})


#能够根据学生姓名或学号和课程名称或课程编号查询该生该课程的成绩
def QuerySelectView(request):
    if request.method != 'POST':
        code = -1
    else:
        form = QuerySelectForm(request.POST)
        ans = form.query()
        code = ans['code']
        result = CheckCode(code)
    if code > 0:
        return render(request, 'select_query.html', {"code": ans['code'], "select": ans['select']})
    else:
        return render(request, 'select_query.html', {'code': result['code'], 'ss': result['ss']})


#能够统计出学生的加权平均成绩
def StudentStaticView(request):
    if request.method != 'GET':
        code = -1
    else:
        result = {}
        students = Student.objects.all()
        for s in students:
            sid = s.sid
            selects = Select.objects.filter(student=s)
            credit_sum = 0
            creditscore_sum = 0
            for se in selects:
                c = se.course
                credit_sum += c.credit
                creditscore_sum += c.credit * se.score
            if credit_sum != 0:
                weight = float(creditscore_sum/credit_sum)
            else:
                weight = 0
            result[sid] = weight
        return HttpResponse(json.dumps({"code": 1, "StudentStatic": result}), content_type="application/json")
    return CheckCode(code)


#课程的平均成绩
def CourseAverageView(request):
    if request.method != 'GET':
        code = -1
    else:
        result = {}
        courses = Course.objects.all()
        for c in courses:
            cid = c.cid
            selects = Select.objects.filter(course=c)
            people = 0
            sum_score = 0
            for se in selects:
                people += 1
                sum_score += se.score
            if people:
                result[cid] = float(sum_score/people)
            else:
                result[cid] = 0
        return HttpResponse(json.dumps({"code": 1, "CourseAverageStatic": result}), content_type="application/json")
    return CheckCode(code)


#能够统计出班级的加权平均成绩
def ClassStaticView(request):
    if request.method != 'GET':
        code = -1
    else:
        code = 1
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
                    result[kc] = float(vcs/vc)

#课程的成绩分布（不及格，60－69，70－79，80－89，90－99，满分）
def CourseStaticView(request):
    if request.method != 'GET':
        code = -1
    else:
        result = {}
        courses = Course.objects.all()
        for c in courses:
            cid = c.cid
            selects = Select.objects.filter(course=c)
            cnt = defaultdict(lambda: 0)
            for se in selects:
                if se.score < 60:
                    cnt['不及格'] += 1
                elif se.score < 70:
                    cnt['60-69'] += 1
                elif se.score < 80:
                    cnt['70-79'] += 1
                elif se.score < 90:
                    cnt['80-89'] += 1
                elif se.score < 100:
                    cnt['90-99'] += 1
                else:
                    cnt['满分'] += 1
            result[cid] = cnt
        return HttpResponse(json.dumps({"code": 1, "CourseStatic": result}), content_type="application/json")
    return CheckCode(code)


