from django.contrib import admin
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
	list_display=('titulo', 'slug', 'fecha', 'autor')
	list_filter=('fecha', 'autor')
	search_fields=('titutlo', 'cuerpo')
	prepopulated_fields={'slug':('titulo',)}
	ordering=['fecha']




admin.site.register(Post, PostAdmin)
# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
	list_display=('post', 'name', 'fecha')
	search_fields=('cuerpo',)

admin.site.register(Comentario, ComentarioAdmin)
