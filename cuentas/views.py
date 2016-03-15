from django.shortcuts import render
from django.views.generic import View



# Create your views here.

class LoginView(View):
	def get(self, request):
		template_name = "cuentas/login.html"
		return render(request, template_name)


class RegistroView(View):
	def get(self, request):
		template_name = "cuentas/registro.html"
		return render(request, template_name)

