from django import forms
from cfc.models import Recipe, Category, UserProfile
from django.contrib.auth.models import User
from django.utils import timezone

# form for the creation of a recipe
class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Recipe.")
    recipeID = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    ingredients = forms.CharField(widget=forms.Textarea(), help_text="Please enter the ingredients")
    instructions = forms.CharField(widget=forms.Textarea(), help_text="Please enter the instructions")
    description = forms.CharField(max_length=64, help_text="A short description")
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    created = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('title'))
    picture = forms.ImageField(required=True)
    author = forms.CharField(max_length=128, required=False, widget=forms.HiddenInput())
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Recipe
        fields = ('title', 'picture', 'description', 'ingredients', 'instructions', 'category')

        # What fields do we want to include in our form?
        # This way we dont need every field in the model present
        # Some fields may allow NULL values, so we may not want to include them
        # Here, we are hiding the foreign key
        # we cna either exclude the category fueld fromt he form,
        # we can either exclude the category fueld fromt he form,

        # or specify the fields to include (i.e not include the category fueld)
        #fields = ("title", "url", "views")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

class RatingForm(forms.Form):
    RATING_CHOICES = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))
    CurrentRating = forms.ChoiceField(choices=RATING_CHOICES, label="Rate")
