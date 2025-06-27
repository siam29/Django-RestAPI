from django.contrib import admin

# Register your models here.
from .models import Student


admin.site.register(Student)
# Register the Student model with the admin site so it can be managed through the Django admin interface
# This allows you to add, edit, and delete Student records from the admin panel.
# The Student model is defined in students/models.py, and this registration makes it accessible in the