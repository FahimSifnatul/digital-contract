from django.shortcuts import render
from django.views import View

# Create your views here.
class Account(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'account.html', context)