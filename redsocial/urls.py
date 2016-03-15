from django.conf.urls import url
from django.contrib import admin
from cuentas import views
from post import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 
    	views.LoginView.as_view(),
    	name='login'
    	),

    url(r'^registro/$', 
    	views.RegistroView.as_view(),
    	name='registro'
    	),

    url(r'^todos/$', 
    	views2.PostView.as_view(),
    	name='todos'
    	),
    
]


