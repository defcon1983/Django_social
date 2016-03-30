from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):

	class Meta:
		model=Post
		fields=('titulo', 'cuerpo')

	# class PostImage:
	# 	image=forms.FileField(laberl='Select photo post')

class ComentarioForm(forms.ModelForm):
	class Meta:
		model=Comentario
		fields=('cuerpo',)