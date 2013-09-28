from core.models import CustomPage
from django.contrib import admin
from django import forms
from django.db import models

class CustomPageAdmin(admin.ModelAdmin):
	formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

	class Media:
		js = ('js/plugins/ckeditor/ckeditor.js',)

admin.site.register(CustomPage, CustomPageAdmin)