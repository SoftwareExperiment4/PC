from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from register.forms import SignupForm

# Create your views here.
def signup(request):
	if request.method == "POST":
		signupform = SignupForm(request.POST)
		if signupform.is_valid():
			user = signupform.save(commit=False)
			user.email = signupform.cleaned_data['email']
			user.save()

			return HttpResponseRedirect(
				reverse("signup_ok")
			)
	elif request.method == "GET":
		signupform = SignupForm()

		return render(request, "registration/signup.html", {
			"signupform": signupform,
		})
