from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^todos/$', 
			views.PostView.as_view(),
			name='todos'
			),

	#?P lo que viene enseguida es un nombre de variable
	url(r'^detalle/(?P<slug>[-\w]+)',
			views.PostDetailView.as_view(),
			name='detalle'
		),
	url(r'api/$',
		views.Api.as_view(),
		name='api'),

]