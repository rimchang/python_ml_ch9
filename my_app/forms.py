
from django import forms

class ReviewForm(forms.Form):
    review = forms.CharField(
                            required=True,
                            widget=forms.Textarea,
                            error_messages={'required': 'review is required'}
                            )

