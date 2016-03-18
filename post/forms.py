from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model=Post
		fields=('titulo', 'cuerpo')

	# class PostImage:
	# 	image=forms.FileField(laberl='Select photo post')

