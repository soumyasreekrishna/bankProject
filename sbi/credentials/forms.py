from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ('name', 'dob', 'age', 'gender','phone','mailid', 'address','district','account')



