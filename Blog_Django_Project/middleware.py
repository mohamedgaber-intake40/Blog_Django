import re

from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		response = self.get_response(request)
		return response

	def process_view(self,request,view_func,view_args,view_kwargs):
		assert hasattr(request,'user')
		path =request.path_info.lstrip('/')
		print(path)

		# if not request.user.is_authenticated:
		# 	if not any(url.match(path) for url in EXEMPT_URLS):
		# 		return redirect(settings.LOGIN_URL)

		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
		print("hello hena :",request.user)

		if request.user.is_authenticated and url_is_exempt:
			return redirect(settings.LOGIN_REDIRECT_URL)
		elif request.user.is_authenticated:
			if request.user.is_active == 0:
				print("hello")
				logout(request)
				return redirect(settings.LOGIN_URL)


		

		# if request.user.is_authenticated:
		# 	if request.user.is_active == 0:
		# 		return redirect(settings.LOGIN_REDIRECT_URL)

		
		# if request.user.is_authenticated:
		# 	if request.user.role == 2:
		# 		if not any(url.match(path) for url in EXEMPT_URLS):
		# 			return redirect(settings.LOGIN_REDIRECT_URL)
				