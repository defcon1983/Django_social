from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from django.views.generic import View
from .forms import PostForm
# Create your views here.
from django.core import serializers


class PostView(View):
	def get(self, request):
		template="post/todos.html"
		posts=Post.objects.all()
		form=PostForm()
		context = {
		'posts': posts,
		'form': form,
		}

		return render(request, template, context)

	def post(self,request):
		#Esto llena el formulario
		form=PostForm(request.POST)
		form.save()
		#Recarga la página con la url que indicamos y renderiza de nuevo
		return redirect('post:todos')

class PostDetailView(View):
		def get(self, request,slug):
			post=Post.objects.get(slug=slug)
			template='post/detalle.html'
			context={
			'post':post
			}
			return render(request, template, context)

class Api(View):
	def get(self, request):
		posts=Post.objects.all()
		data = serializers.serialize('xml', posts)

		return HttpResponse(data, content_type='application/xml')