from django import forms

class TextForward(forms.Form):
    Usertext= forms.CharField(widget=forms.Textarea(attrs={'maxlength':None}))