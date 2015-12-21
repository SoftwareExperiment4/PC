from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Email',
				'required' : 'true',
			}
		)
	)

	username = forms.RegexField(label="Username", max_length=30,
		regex=r'^[\w.@+-]+$',
		help_text="Required. 30 characters or fewer. Letters, digits and "
			"@/./+/-/_ only.",
		error_messages={
			'invalid': "This value may contain only letters, numbers and "
			"@/./+/-/_ characters."},
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Username',
			'required': 'true',
		})
	)

	password1 = forms.CharField(label="Password",
		widget=forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Password',
			'required': 'true',
		})
	)

	password2 = forms.CharField(label="Password confirmation",
		help_text="Enter the same password as above, for verification.",
		widget=forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Password confirmation',
			'required': 'true',
		})
	)


class Meta:
	model = User
	fields = ("username", "email", "password1", "password2",)
