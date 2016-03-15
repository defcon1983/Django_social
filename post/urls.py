from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^todos/$', 
			views.PostView.as_view(),
			name='todos'
			),
]