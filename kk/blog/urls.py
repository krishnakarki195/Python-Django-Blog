from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home-index'),
	url(r'^blog/([a-zA-Z]+)$', views.IndexView.as_view(), name='blog-index'),
	url(r'^blog/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='blog-detail'),
	url(r'^blog/add/$', views.CreateBlog.as_view(), name='blog-add'),
	url(r'^blog/(?P<pk>[0-9]+)/update/$', views.UpdateBlog.as_view(), name='blog-update'),
	url(r'^blog/(?P<pk>[0-9]+)/delete/$', views.DeleteBlog.as_view(), name='blog-delete'),
	url(r'^blog/login/$', views.UserLogin.as_view(), name='user-login'),
	url(r'^blog/logout/$', views.UserLogout.as_view(), name='user-logout'),
	url(r'^blog/signup/$', views.UserSignup.as_view(), name='user-signup'),
]