from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm
# Create your views here.

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
