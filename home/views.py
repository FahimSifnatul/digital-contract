from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.mail import send_mail

# Create your views here.
class Home(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'index.html', context)


	def post(self, request, *args, **kwargs):

		# Sign In 
		if "username" in request.POST:
			username = request.POST["username"]
			password = request.POST["password"]

			user = authenticate(request, username=username, password=password)

			if user is not None: # user exists
				login(request, user)
				return redirect(reverse('account'))
			
			else: # no user exists
				messages.error(request, 'Sign In error')
				return redirect(reverse('home'))
		

		# Sign Up
		elif "new_username" in request.POST:
			new_username = request.POST['new_username']
			new_password = request.POST['new_password']

			# To check whether a user already exists or not with the new username
			user = User.objects.filter(username=new_username)
			if user is not None: # user exists
				messages.error(request, 'User already exists')
				return redirect(reverse('home'))

			# passed above user existence check with no user exists with new_username
			# Now to create new user
			user = User.objects.create(username=new_username,\
										email=new_username,\
										password=new_password)

			# To create connection to mysql database CVAfs9ELTr
			cursor = connection.cursor()

			# Query to execute to set the new user's verification status as 0
			sql    = "INSERT INTO UserVerification \
					VALUES('"+new_username+"', 0)"
			cursor.execute(sql)

			return redirect(reverse('account'))


