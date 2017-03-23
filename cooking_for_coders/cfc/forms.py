from django import forms
from cfc.models import Recipe, Category, UserProfile
from django.contrib.auth.models import User

#
# class RecipeForm(forms.ModelForm):
#     title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#
#         # If url is not empty and doesn't start with 'http://',
#         # then prepend 'http://'.
#         if url and not url.startswith('http://'):
#             url = 'http://' + url
#             cleaned_data['url'] = url
#
#             return cleaned_data
#
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Page
#
#         # What fields do we want to include in our form?
#         # This way we dont need every field in the model present
#         # Some fields may allow NULL values, so we may not want to include them
#         # Here, we are hiding the foreign key
#         # we cna either exclude the category fueld fromt he form,
#         # we can either exclude the category fueld fromt he form,
#         exclude = ("category",)
#         # or specify the fields to include (i.e not include the category fueld)
#         #fields = ("title", "url", "views")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', "email", "password")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( "picture")
