from django import forms

class TaskForm(forms.Form):
    OPTIONS = [(1, 'Never'), (2, 'Rarely'), (3, 'Sometimes'), (4, 'Often'), (5, 'Very Often')]
    option_1 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_2 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_3 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_4 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_5 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_6 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_7 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_8 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_9 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
    option_10 = forms.TypedMultipleChoiceField(choices=OPTIONS, coerce=int, widget=forms.CheckboxSelectMultiple, required=True)
