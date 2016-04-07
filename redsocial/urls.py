from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^cuentas/',
        include('cuentas.urls', namespace="cuentas")),

    url(r'^post/', 
    	include('post.urls', namespace="post")),

    url(
    	regex=r'^media/(?P<path>.*)$',
    	view= 'django.views.static.serve',
    	kwargs={'document_root':settings.MEDIA_ROOT}
    	),
    
]


