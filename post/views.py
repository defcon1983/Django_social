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
		form=PostForm(request.POST)
		form.save()

		return redirect('todos')


