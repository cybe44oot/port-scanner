from django.db import models

# Create your models here.
class Request(models.Model):
    id=models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    start_port=models.IntegerField()
    end_port=models.IntegerField()
   
    date_added = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    
    port=models.IntegerField()
    status=models.CharField(max_length=200)
    request_id =models.ForeignKey(Request,on_delete=models.CASCADE)