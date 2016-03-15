from django.db import models

# Create your models here.
class Post(models.Model):
	titulo =models.CharField(max_length=50)
	cuerpo=models.TextField()
	fecha=models.DateTimeField(auto_now=True)
	publicado= models.BooleanField(default=True)
	
	def __str__(self):
		return self.titulo

