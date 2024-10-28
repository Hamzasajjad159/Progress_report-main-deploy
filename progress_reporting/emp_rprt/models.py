from django.db import models
from django.contrib.auth.models import AbstractUser

# Work Detail model to define work
class WorkDetail(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class WorkflowStage(models.Model):
    title = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(unique=True, null = True, blank = True)
    next_stages = models.ManyToManyField('self', symmetrical=False, related_name='previous_stages', blank=True)

    def __str__(self):
        return self.title


# Employee Position model to define positions in the company
class Department(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

# Employee User model to define employees
class EmpUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=128, default='temp_password')
    # username = models.CharField(max_length=128, default='temp_Username')



    def __str__(self):
        return self.name

# Products model to define products worked on
class Products(models.Model):
    title = models.CharField(max_length=100)
    sku = models.CharField(max_length=10, unique=True)
    variant_quantity = models.IntegerField()
    variant_colors = models.CharField(max_length=100)
    sp = models.IntegerField()
    cp = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True)  # Optional completion date

    def __str__(self):
        return self.sku

# Progress model to track work progress on products
class Progress(models.Model):
    work = models.ForeignKey(WorkDetail, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(EmpUser, null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    workflow_stage = models.ForeignKey(WorkflowStage, on_delete=models.CASCADE, null=True, blank=True)
    date_last_changed = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('not_started', 'Not Started'), ('ongoing', 'Ongoing'), ('completed', 'Completed')])

    def __str__(self):
        return f"Progress on {self.product} by {self.user}"

    

class UserDepartment(models.Model):
    user = models.ForeignKey(EmpUser, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    work = models.ForeignKey(WorkflowStage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name}"
    
class ProgressUpdated(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(EmpUser, on_delete=models.CASCADE)
    work = models.ForeignKey(WorkDetail, on_delete=models.CASCADE, null=True, blank=True)
    workflow_stage = models.ForeignKey(WorkflowStage, on_delete=models.CASCADE, null=True, blank=True)
    date_changed = models.DateField(auto_now_add=True)  # Date when change occurred
    status_changed_to = models.CharField(max_length=20, choices=[('not_started', 'Not Started'), ('ongoing', 'Ongoing'), ('completed', 'Completed')])

    def __str__(self):
        return f"{self.product.title}  - {self.status_changed_to}"
