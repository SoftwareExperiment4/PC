from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.context_processors import csrf

from post_service.models import Post
from post_service.forms import LoginForm
# testing https://github.com/SoftwareExperiment4/PC.git
# Create your views here.
def post_list(request):
	template = get_template('post_list.html')
	
	page_data = Paginator(Post.objects.all(), 5)
	page = request.GET.get('page')
	
	if page is None:
		page = 1
		
	try:
		posts = page_data.page(page)
	except PageNotAnInteger:
		posts = page_data.page(1)
	except EmptyPage:
		posts = page_data.page(page_data.num_pages)
		
	context = Context({'post_list': posts, 'current_page': int(page), 'total_page': range(1, page_data.num_pages + 1)})
	
	return HttpResponse(template.render(context))
	
def login(request):
	template = get_template('login_form.html')
	
	context = Context({'login_form': LoginForm()})
	context.update(csrf(request))
	
	return HttpResponse(template.render(context))
	
def login_validate(request):
	login_form_data = LoginForm(request)
	
	if login_form_data.is_valid():
		auth.authenticate()