from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^cuentas/',
        include('cuentas.urls')),

    url(r'^post/', 
    	include('post.urls')),
    
]


