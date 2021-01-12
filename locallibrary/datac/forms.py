from django import forms

class userform(forms.Form):
    user_name=forms.CharField(label='user_id',max_length=100)
    password=forms.CharField(label='password',max_length=100)
