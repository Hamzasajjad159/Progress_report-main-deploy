from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EmpUser, Products, Progress, WorkDetail, WorkflowStage, Department, ProgressUpdated, UserDepartment

# Register your models
admin.site.register(EmpUser)
admin.site.register(Products)
admin.site.register(Progress)
admin.site.register(WorkDetail)
admin.site.register(Department)
admin.site.register(ProgressUpdated)
admin.site.register(UserDepartment)
admin.site.register(WorkflowStage)
