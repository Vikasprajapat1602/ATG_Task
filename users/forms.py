from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }
        )
    )

    # user_type to use radio buttons explicitly
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'flex items-center space-x-6 mt-1 mb-1 text-gray-700'
        })
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'profile_picture', 'user_type',
            'address_line1', 'city', 'state', 'pincode',
            'password1', 'password2'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': (
                    'block w-60 max-w-md text-sm text-gray-700 bg-gray-50 '
                    'border border-gray-300 rounded-lg cursor-pointer shadow-sm '
                    'file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 '
                    'file:text-sm file:font-semibold file:bg-blue-600 file:text-white '
                    'hover:file:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:outline-none'
    ),
}),

            'address_line1': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'pincode': forms.TextInput(attrs={
                'class': 'w-full mb-6 px-3 py-2 border border-gray-300 rounded-lg '
                         'focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }
