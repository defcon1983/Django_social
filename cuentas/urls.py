from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[

	url(r'^login/$', 
		auth_views.login,
		name="login"),

	url(r'^logut/$', 
		auth_views.logout,
		name="logout"),

    url(r'^registro/$', 
    	views.RegistroView.as_view(),
    	name='registro'
    	),

]