from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

import datetime

class Subject(models.Model):
	"""Subject Model
		:Its for subject taught in school
	"""
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s' % (self.name)

class Board(models.Model):
	"""Board Model
		:Supported School Boards 
	"""
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % (self.name)

class School(models.Model):
	"""School Model
		:School Information
	"""
	TYPE = (
		('pr', 'Private'),
		('pu', 'Public')
	)
	name = models.CharField(max_length=200, unique=True , null=False, blank=False)
	about_school = models.TextField(null=True, blank=True)
	address = models.TextField()
	s_type = models.CharField(choices=TYPE, max_length=2)
	board = models.ForeignKey(Board, related_name='school_board')
	ranking = models.CharField(max_length=10, null=True, blank=True)
	logo = models.ImageField(upload_to='school', null=True, blank=True)
	contact_no = models.CharField(max_length=50,null=True, blank=True)
	email = models.EmailField(max_length = 200, null=True, blank=True)
	fax_no = models.CharField(max_length=50,null=True, blank=True)
	weblink = models.URLField(null=True,  blank=True)
	asso_org = models.CharField(max_length=100, null=True, blank=True)
	affiliation_date = models.DateField(null=True, blank=True)
	affiliation_number = models.CharField(max_length=50, null=True, blank=True)
	affiliation_valid_upto_date = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)


class UserProfile(models.Model):
	"""UserProfile Model
		:User information with types supported for school
	"""
	USER_TYPE = (('student','Student'),
		('staff','Staff'),
		('faculty','Faculty'),
		('principal', 'Principal'),
		('director','Director'),
		('parent','Parent'),
	)
	GENDER = (
		('M', 'Male'), 
		('F', 'Female')
	)
	user = models.ForeignKey(User, related_name='user_profile')
	name = models.CharField(max_length=200)
	secondary_email = models.EmailField(max_length = 200, null=True, blank=True)
	present_address = models.TextField(null=True, blank=True)
	permanent_address = models.TextField(null=True, blank=True)
	gender = models.CharField(max_length=2, choices=GENDER)
	user_type = models.CharField(choices=USER_TYPE, max_length=10)
	is_approved = models.BooleanField(default=False)
	about_me = models.TextField(null=True, blank=True)
	dob = models.DateField(null=True, blank=True)
	blood_group = models.CharField(max_length=5,null=True, blank=True)
	distinguish_mark = models.CharField(max_length=50,null=True, blank=True)
	weblink = models.URLField(null=True,  blank=True)
	hometown = models.CharField(max_length=100,null=True, blank=True)
	contact_no = models.CharField(max_length=20,null=True, blank=True)
	mobile_no = models.CharField(max_length=20,null=True, blank=True)
	photo = models.ImageField(upload_to='profile', null=True, blank=True)
	is_deleted = models.BooleanField(default=False)
	is_blocked = models.BooleanField(default=False)

	join_date = models.DateField(null=True, blank=True)
	leave_date = models.DateField(null=True, blank=True)

	school = models.ForeignKey(School)

	def __unicode__(self):
		return u'%s' % (self.name)

class Student(models.Model):
	"""Student Model
		:Student specific information
	"""
	user_profile = models.ForeignKey(UserProfile, related_name='student_user_profile')
	standard = models.CharField(max_length=4)
	roll_number = models.CharField(max_length=20)
	section = models.CharField(max_length=2, null=True, blank=True)
	father = models.ForeignKey(UserProfile, null=True, blank=True, related_name='father_user_profile')
	mother = models.ForeignKey(UserProfile, null=True, blank=True, related_name='mother_user_profile')
	guardian = models.ForeignKey(UserProfile, null=True, blank=True, related_name='guardian_user_profile')

	def __unicode__(self):
		return u'%s' % (self.user_profile.name)

	class Meta:
		ordering = ['roll_number']
		unique_together = (("standard", "roll_number", "section"))

class Faculty(models.Model):
	"""Faculty Model
		:Faculty specific Information
	"""
	user_profile = models.ForeignKey(UserProfile)
	emp_id = models.CharField(max_length=20, null=True, blank=True)
	subjects = models.ManyToManyField(Subject, null=True, blank=True)
	designation = models.CharField(max_length=100, null=True, blank=True)
	office_number = models.CharField(max_length=50, null=True, blank=True)
	degrees = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.user_profile.name)

	class Meta:
		ordering = ['emp_id']

class Principal(models.Model):
	"""Principal Model
		: Principal specific information
	"""
	user_profile = models.ForeignKey(UserProfile)
	emp_id = models.CharField(max_length=20, null=True, blank=True)
	subjects = models.ManyToManyField(Subject, null=True, blank=True)
	office_number = models.CharField(max_length=50, null=True, blank=True)
	degrees = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.user_profile.name)

	class Meta:
		ordering = ['emp_id']

class Director(models.Model):
	"""Director Model
		: Director specific information
	"""
	user_profile = models.ForeignKey(UserProfile)
	emp_id = models.CharField(max_length=20, null=True, blank=True)
	office_number = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.user_profile.name)

	class Meta:
		ordering = ['emp_id']

class Staff(models.Model):
	"""Staff Model
		: Staff specific information
	"""
	DEPARTMENT = (('li','Library'),
		('pl','Physics Lab'),
		('cl','Chemistry Lab'),
		('bl','Biology Lab'),
		('cn', 'Clean-up')
	)
	user_profile = models.ForeignKey(UserProfile)
	emp_id = models.CharField(max_length=20, null=True, blank=True)
	department = models.CharField(max_length=2, choices=DEPARTMENT)

	def __unicode__(self):
		return u'%s' % (self.user_profile.name)

	class Meta:
		ordering = ['emp_id']

class Slide(models.Model):
	"""Slide Model
		:Homepage slides
	"""
	image = models.ImageField(upload_to='slide')
	landing_page= models.CharField(max_length=200, null=True, blank=True)
	order = models.PositiveIntegerField()
	school = models.ForeignKey(School)

	def __unicode__(self):
		return self.landing_page

class CustomPage(models.Model):
	"""CustomPage Model
		:Custom Pages model
	"""
	page_name = models.CharField(max_length=50)
	page_url = models.CharField(max_length=20, null=True, blank=True)
	content = models.TextField()
	title = models.CharField(max_length=50, null=True, blank=True)
	school = models.ForeignKey(School)

	class Meta:
		unique_together = ("page_url", "school")

	def __unicode__(self):
		return self.page_name

class DomainName(models.Model):
	"""DomainName
		:Domains supported for school
	"""
	school = models.ForeignKey(School)
	url = models.CharField(max_length=100)

	def __unicode__(self):
		return self.url

class Navigation(models.Model):
	"""Navigation
		:Website navigation tabs
	"""
	TABS = (
		('1','1st Tab'),
		('2','2nd Tab'),
		('2a','2nd Tab - 1st dropdown'),
		('2b','2nd Tab - 2nd dropdown'),
		('2c','2nd Tab - 3rd dropdown'),
		('2d','2nd Tab - 4th dropdown'),
		('2e','2nd Tab - 5th dropdown'),
		('3','3rd Tab'),
		('3a','3rd Tab - 1st dropdown'),
		('3b','3rd Tab - 2nd dropdown'),
		('3c','3rd Tab - 3rd dropdown'),
		('3d','3rd Tab - 4th dropdown'),
		('3e','3rd Tab - 5th dropdown'),
		('4','4th Tab'),
		('4a','4th Tab - 1st dropdown'),
		('4b','4th Tab - 2nd dropdown'),
		('4c','4th Tab - 3rd dropdown'),
		('4d','4th Tab - 4th dropdown'),
		('4e','4th Tab - 5th dropdown'),
		('5','5th Tab'),
		('5a','5th Tab - 1st dropdown'),
		('5b','5th Tab - 2nd dropdown'),
		('5c','5th Tab - 3rd dropdown'),
		('5d','5th Tab - 4th dropdown'),
		('5e','5th Tab - 5th dropdown'),
	)
	school = models.ForeignKey(School)
	name = models.CharField(max_length=30)
	page_url = models.CharField(max_length=20, null=True, blank=True)
	is_admin_provided = models.BooleanField()
	position = models.CharField(max_length=3, choices=TABS)

	def __unicode__(self):
		return self.name

admin.site.register(Subject)
admin.site.register(Board)
admin.site.register(School)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Principal)
admin.site.register(Director)
admin.site.register(Staff)
admin.site.register(Slide)
admin.site.register(DomainName)
admin.site.register(Navigation)