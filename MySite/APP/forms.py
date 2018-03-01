#!/usr/bin/env python
# coding=utf-8
import datetime
import re
from django import forms
from .models import Student
from .models import Course
from .models import Select


class StudentAddForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    gender = forms.IntegerField()
    start_age = forms.IntegerField()
    start_year = forms.IntegerField()
    squad = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            sname = cd['sname']
            gender = cd['gender']
            start_age = cd['start_age']
            start_year = cd['start_year']
            squad = cd['squad']
            if gender != 1 and gender != 0:
                return -5
            if start_age < 10 or start_age > 50:
                return -5
            if len(str(sid)) !=10:
                return -5
            student = Student(
                sid=sid,
                sname=sname,
                gender=gender,
                start_age=start_age,
                start_year=start_year,
                squad=squad
            )
            cnt = Student.objects.get_object(sid=sid)
            if cnt:
                code = -4
            else:
                code = 0
                student.save()
        else:
            code = -2
        return code


class StudentDelForm(forms.Form):
    sid = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            student = Student.objects.get_object(sid=sid)
            if student:
                code = 0
                student.delete()
            else:
                code = -3
        else:
            code = -2
        return code


class StudentModForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField()
    gender = forms.IntegerField()
    start_age = forms.IntegerField()
    start_year = forms.IntegerField()
    squad = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            sname = cd['sname']
            gender = cd['gender']
            start_age = cd['start_age']
            start_year = cd['start_year']
            squad = cd['squad']

            student = Student.objects.get_object(sid=sid)
            if student:
                student.sname = sname
                student.gender = gender
                student.start_age = start_age
                student.start_year = start_year
                student.squad = squad
                student.save()
                code = 0
            else:
                code = -3
        else:
            code = -2
        return code


class CourseAddForm(forms.Form):
    cid = forms.IntegerField()
    cname = forms.CharField()
    teacher = forms.CharField()
    credit = forms.IntegerField()
    grades = forms.IntegerField()
    cancel_year = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            cid = cd['cid']
            cname = cd['cname']
            teacher = cd['teacher']
            credit = cd['credit']
            grades = cd['grades']
            cancel_year = cd['cancel_year']
            if len(str(cid)) != 7:
                return -5

            course = Course(
                cid=cid,
                cname=cname,
                teacher=teacher,
                credit=credit,
                grades=grades,
                cancel_year=cancel_year
            )
            cnt = Course.objects.get_object(cid=cid)
            if cnt:
                code = -4
            else:
                code = 0
                course.save()
        else:
            code = -2
        return code


class CourseDelForm(forms.Form):
    cid = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            cid = cd['cid']
            course = Course.objects.get_object(cid=cid)
            if course:
                course.delete()
                code = 0
            else:
                code = -3
        else:
            code = -2
        return code


class CourseModForm(forms.Form):
    cid = forms.IntegerField()
    cname = forms.CharField()
    teacher = forms.CharField()
    credit = forms.IntegerField()
    grades = forms.IntegerField()
    cancel_year = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            cid = cd['cid']
            cname = cd['cname']
            teacher = cd['teacher']
            credit = cd['credit']
            grades = cd['grades']
            cancel_year = cd['cancel_year']

            course = Course.objects.get_object(cid=cid)
            if course:
                course.cname = cname
                course.teacher = teacher
                course.credit = credit
                course.grades = grades
                course.cancel_year = cancel_year
                course.save()
                code = 0
            else:
                code = -3
        else:
            code = -2
        return code


class SelectAddForm(forms.Form):
    sid = forms.IntegerField()
    cid = forms.IntegerField()
    select_year = forms.IntegerField()
    score = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            cid = cd['cid']
            select_year = cd['select_year']
            score = cd['score']

            student = Student.objects.get_object(sid=sid)
            course = Course.objects.get_object(cid=cid)
            if student and course:
                cnt = Select.objects.get_object(student=student, course=course)
                if cnt:
                    code = -4
                else:
                    if student.start_age > course.grades:
                        return -5
                    if course.cancel_year and select_year >= course.cancel_year:
                        return -5
                    code = 0
                    select = Select(
                        student=student,
                        course=course,
                        select_year=select_year,
                        score=score
                    )
                    select.save()
            else:
                code = -3
        else:
            code = -2
        return code


class SelectDelForm(forms.Form):
    sid = forms.IntegerField()
    cid = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            cid = cd['cid']

            student = Student.objects.get_object(sid=sid)
            course = Course.objects.get_object(cid=cid)
            if student and course:
                cnt = Select.objects.get_object(student=student, course=course)
                if cnt:
                    code = 0
                    cnt.delete()
                else:
                    code = -3
            else:
                code = -3
        else:
            code = -2
        return code


class SelectModForm(forms.Form):
    sid = forms.IntegerField()
    cid = forms.IntegerField()
    select_year = forms.IntegerField()
    score = forms.IntegerField()

    def save(self):
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            cid = cd['cid']
            select_year = cd['select_year']
            score = cd['score']

            student = Student.objects.get_object(sid=sid)
            course = Course.objects.get_object(cid=cid)
            if student and course:
                cnt = Select.objects.get_object(student=student, course=course)
                if cnt:
                    code = 0
                    cnt.student = student
                    cnt.course = course
                    cnt.select_year = select_year
                    cnt.score = score
                    cnt.save()
                else:
                    code = -3
            else:
                code = -3
        else:
            code = -2
        return code


class QueryStudentForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField(required=False)

    def query(self):
        result = {}
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            sname = cd['sname']

            if sid:
                student = Student.objects.get_object(sid=sid)
            else:
                student = Student.objects.get_object(sname=sname)

            if student:
                selects = Select.objects.filter_object(student=student)
                # dic_student = [student.as_dict()]
                # dic_selects = [obj.as_dict() for obj in selects]
                result['code'] = 1
                result['student'] = student
                result['selects'] = selects
            else:
                result['code'] = -3
        else:
            result['code'] = -2
        return result


class QueryCourseForm(forms.Form):
    cid = forms.IntegerField()
    cname = forms.CharField(required=False)

    def query(self):
        result = {}
        if self.is_valid():
            cd = self.cleaned_data
            cid = cd['cid']
            cname = cd['cname']

            if cid:
                course = Course.objects.get_object(cid=cid)
            else:
                course = Course.objects.get_object(cname=cname)

            if course:
                selects = Select.objects.filter_object(course=course)
                # dic_course = [course.as_dict()]
                # dic_selects = [obj.as_dict() for obj in selects]
                result['code'] = 1
                result['course'] = course
                result['selects'] = selects
            else:
                result['code'] = -3
        else:
            result['code'] = -2
        return result


class QuerySelectForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField(required=False)
    cid = forms.IntegerField()
    cname = forms.CharField(required=False)

    def query(self):
        result = {}
        if self.is_valid():
            cd = self.cleaned_data
            sid = cd['sid']
            sname = cd['sname']
            cid = cd['cid']
            cname = cd['cname']
            if sid:
                student = Student.objects.get_object(sid=sid)
            else:
                student = Student.objects.get_object(sname=sname)

            if cid:
                course = Course.objects.get_object(cid=cid)
            else:
                course = Course.objects.get_object(cname=cname)

            if course and student:
                select = Select.objects.get_object(course=course, student=student)
                if select:
                    result['code'] = 1
                    result['select'] = select
                else:
                    result['code'] = -3
            else:
                result['code'] = -3
        else:
            result['code'] = -2
        return result


