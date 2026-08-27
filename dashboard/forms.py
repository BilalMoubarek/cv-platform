from django import forms
from .models import ContactMessage, CVSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الإسم الكامل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع الرسالة'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'اكتب رسالتك هنا...'}),
        }

class CVSubmissionForm(forms.ModelForm):
    class Meta:
        model = CVSubmission
        fields = ['phone', 'cv_file', 'message']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '06XXXXXXXX'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'رسالة إضافية (اختياري)...'}),
            'cv_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
        }