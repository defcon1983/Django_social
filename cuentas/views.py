from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import LoginForm
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login



# Create your views here.

class LoginView(View):
	def get(self, request):
		form=LoginForm()
		template_name = "cuentas/login.html"
		context={
		'form':form
		}
		return render(request, template_name,context)

	def post(self, request):
		form=LoginForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			user=authenticate(username=cd['username'],
			password=cd['password'])
		if user is not None:
			login(request, user)
			return redirect('post:todos')
		
class RegistroView(View):
	def get(self, request):
		template_name = "cuentas/registro.html"
		return render(request, template_name)

