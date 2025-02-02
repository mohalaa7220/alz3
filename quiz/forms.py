from django import forms
from .models import Question


class QuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "is_correct"]
        widgets = {
            "is_correct": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
