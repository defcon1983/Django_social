from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	titulo =models.CharField(max_length=50)
	#blank y null estan declarando que puede quedar el campo vacio, que no es obligatorio
	slug =models.SlugField(max_length=50, blank=True, null=True)
	cuerpo=models.TextField()
	fecha=models.DateTimeField(auto_now=True)
	publicado= models.BooleanField(default=True)
	autor=models.ForeignKey(User, related_name='posts_publicados', blank=True, null=True)
	imagen= models.ImageField(upload_to='img_post', blank=True, null = True)



	def __str__(self):
		return self.titulo

	#Nombre por convencion
	def get_absolute_url(self):
		return reverse('post:detalle', args=(self.slug,))

class Comentario(models.Model):
	post=models.ForeignKey(Post, related_name='comentarios', blank=True, null=True)
	cuerpo=models.TextField(blank=True, null=True)
	name=models.ForeignKey(User, related_name='autor', blank=True, null=True)
	fecha=models.DateTimeField(auto_now=True, blank=True,null=True)

	def __str__(self):
		return 'Comentario de {} en {}'.format(self.name, self.post)