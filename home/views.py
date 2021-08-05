from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.mail import send_mail
from secrets import token_urlsafe


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
				# To check user (email) verified or not
				cursor = connection.cursor()
				sql    = "SELECT status FROM UserVerification WHERE username='"+username+"'"
				cursor.execute(sql)

				status_flag = cursor.fetchone()[0]

				if status_flag == 0: # new user - not verified. Attaching error message
					messages.error(request, 'User not verified')
					return redirect(reverse('home'))
				elif status_flag == 1: # email verified user. logging in and redirecting to My Account page
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
			if len(user) > 0: # user exists
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
			verification_token = token_urlsafe(6)
			sql    = "INSERT INTO UserVerification \
					VALUES('"+new_username+"', 0, '"+verification_token+"')"
			cursor.execute(sql)

			# Sending verification email
			subject = 'Digital Contract Account verification'
			message = 'Please click to verify your account - 127.0.0.1:8000/'+verification_token
			from_email = 'digital.contract.0@gmail.com'
			to_email   = [new_username] 
			send_mail(subject, message, from_email, to_email, fail_silently=False,)

			return HttpResponse("<h1 style='height:100%;text-align:center;background-color:cyan;'>\
							Please verify your Account. Click on the link sent to\
							your E-mail.</h1>")


class UserVerification(View):
	def get(self, request, verification_token, *args, **kwargs):
		cursor = connection.cursor()
		sql    = "UPDATE UserVerification\
				 SET status=1 \
				 WHERE verification_token='"+verification_token+"'"
		cursor.execute(sql)

		return redirect(reverse('account'))