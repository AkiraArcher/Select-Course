from __future__ import unicode_literals
from django.db import models, DatabaseError, transaction

# Create your models here.


class BaseManager(models.Manager):
    def get_object(self, **kwargs):
        try:
            return self.get(**kwargs)
        except models.ObjectDoesNotExist:
            return None
    def filter_object(self, **kwargs):
        try:
            return self.filter(**kwargs)
        except models.ObjectDoesNotExist:
            return None


class Student(models.Model):
    sid = models.IntegerField(unique=True)
    sname = models.CharField(max_length=30, default='')
    gender = models.IntegerField()
    start_age = models.IntegerField()
    start_year = models.IntegerField()
    squad = models.IntegerField()
    objects = BaseManager()

    def as_dict(self):
        return {
            "sid": self.sid,
            "sname": self.sname,
            "gender": self.gender,
            "start_age": self.start_age,
            "start_year": self.start_year,
            "squad": self.squad
        }


class Course(models.Model):
    cid = models.IntegerField(unique=True)
    cname = models.CharField(max_length=30, default='')
    teacher = models.CharField(max_length=30, default='')
    credit = models.IntegerField(default=0)
    grades = models.IntegerField()
    cancel_year = models.IntegerField(null=True)
    students = models.ManyToManyField(Student, through="Select")
    objects = BaseManager()

    def as_dict(self):
        return {
            "cid": self.cid,
            "cname": self.cname,
            "teacher": self.teacher,
            "credit": self.credit,
            "grades": self.grades,
            "cancel_year": self.cancel_year
        }


class Select(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    select_year = models.IntegerField()
    score = models.IntegerField()
    objects = BaseManager()

    def as_dict(self):
        return {
            "select_year": self.select_year,
            "score": self.score
        }
