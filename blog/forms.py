from django import forms

class CommentForm(forms.Form):
	
	author = forms.CharField(label="Author", max_length=30)
	author_email = forms.EmailField()
	text = forms.CharField(label="Comment", widget=forms.Textarea)
