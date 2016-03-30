from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm, ComentarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
			form=ComentarioForm()
			comments=post.comentarios.all()
			template='post/detalle.html'
			context={
			'post':post,
			'form': form,
			'comments': comments
			}
			return render(request, template, context)

		def post(self,request, slug):
			post=Post.objects.get(slug=slug)
			new_form=ComentarioForm(request.POST)

			if new_form.is_valid():
				new_com=new_form.save(commit=False)
				new_com.name=request.user
				new_com.post=post
				new_com.save()
				messages.success(request,"Comentario agregado!")
			else: 
				messages.error(request,'Algo fallo')
			
			return HttpResponseRedirect(reverse('post:detalle',args=[slug]))


