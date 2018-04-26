from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
 
from visualize.usecases.get_user_info import GetUserInfo
from visualize.usecases.analysis import Analysis


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class VisualizeView(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		analysis = Analysis()
		response = analysis.execute("yasintoy")
		return render(request, self.template_name, {"info": response["user_info"]}) 
