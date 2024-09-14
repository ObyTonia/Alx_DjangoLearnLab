from django import forms

class ExampleForm(forms.ModelForm):

    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField(widget=forms.SelectDateWidget)

    # You can also add custom validation if needed
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Add custom validation logic if necessary
        return title
