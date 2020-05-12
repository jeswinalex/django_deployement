from django import forms
from my_app.models import Name


class NewUsers(forms.ModelForm):
    class Meta:
        model = Name
        fields = "__all__"