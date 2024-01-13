from django import forms

class TaskForm(forms.Form):
    OPTIONS = [(1, 'Never'), (2, 'Rarely'), (3, 'Sometimes'), (4, 'Often'), (5, 'Very Often')]
    option1 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option2 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option3 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option4 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option5 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option6 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option7 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option8 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option9 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option10 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
