# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table = "TestModel_test" #default name is app_test