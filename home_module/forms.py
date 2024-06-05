from django import forms
from home_module.models import EmailSubscriber,ContactUs
class EmailSubscriberForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your mail'}))
    class Meta:
        model = EmailSubscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if EmailSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists.")
        return email

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
