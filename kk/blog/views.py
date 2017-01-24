from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from . models import Blog, BlogType
from . forms import LoginForm, SignupForm


class HomeView(generic.ListView):
	template_name = 'blog/base.html'

	def get_queryset(self):
		return BlogType.objects.all()


class IndexView(generic.ListView):
	template_name = 'blog/blog_list.html'
	paginate_by = 5
	allow_empty = True

	def get_queryset(self):
		args = list(self.args)
		return Blog.objects.filter(blog_type__name__icontains=args[0])


class DetailView(generic.DetailView):
	model = Blog
	template_name = 'blog/detail.html'


class CreateBlog(generic.CreateView):
	model = Blog
	fields = [
		'blog_header',
		'blog_content',
		'blog_added_date',
		'blog_updated_date',
		'blog_type'
	]

	def form_valid(self, form):
		form.instance.blog_author = self.request.user
		return super(CreateBlog, self).form_valid(form)


class UpdateBlog(generic.UpdateView):
	model = Blog
	fields = [
		'blog_header',
		'blog_content',
		'blog_added_date',
		'blog_updated_date',
		'blog_type'
	]
	success_url = reverse_lazy('blog:home-index')


class DeleteBlog(generic.DeleteView):
	model = Blog
	success_url = reverse_lazy('blog:home-index')


class UserLogin(View):
	form_class = LoginForm
	template_name = 'blog/login_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		# cleaned (normalized) data
		username = form.data['username']
		password = form.data['password']
		# returns user objects if credentials are correct
		user = authenticate(username=username, password=password)
		if user is not None:
			#if user.is_active:
			login(request,user)
			return redirect('blog:home-index')
		return render(request, self.template_name, {'form': form, 'error_message':'username or password is incorrect!'})


class UserLogout(View):

	def get(self,request):
		logout(request)
		return redirect('blog:home-index')


class UserSignup(View):
	form_class = SignupForm
	template_name = 'blog/signup_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# returns user objects if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('blog:home-index')
		return render(request, self.template_name, {'form': form, 'error_message': 'Please enter valid credentials !'})
