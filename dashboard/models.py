from django.db import models
from django.contrib.postgres.fields import JSONField
#from django.contrib.auth.models import User

# Create your models here.

class Traps(models.Model):
    device = models.CharField(max_length=100, primary_key=True)
    time = models.CharField(max_length=100)
    data = JSONField()
    # since device field need not be unique we need a id column to give us primary keys
    # id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    #created = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self

    class Meta:
        managed = False
        db_table = 'traps'
