from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=('titulo', 'slug', 'fecha', 'autor')
	list_filter=('fecha', 'autor')
	search_fields=('titutlo', 'cuerpo')
	prepopulated_fields={'slug':('titulo',)}
	ordering=['fecha']




admin.site.register(Post, PostAdmin)
# Register your models here.
