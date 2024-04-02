from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

        widgets = {
            "patient_name": forms.TextInput(attrs={"class": "form-control"}),
            "patient_relative_name": forms.TextInput(attrs={"class": "form-control"}),
            "patient_mobile_number": forms.NumberInput(),
            "patient_email": forms.EmailInput(attrs={"class": "form-control"}),
            "patient_city": forms.TextInput(attrs={"class": "form-control"}),
            "health_issue": forms.TextInput(attrs={"class": "form-control"}),
            "appointment_date": forms.DateInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "marital_status": forms.Select(attrs={"class": "form-control"}),
        }

