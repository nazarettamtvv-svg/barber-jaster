from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appointment


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=80,
        required=True,
        label="Ім'я",
        widget=forms.TextInput(attrs={"placeholder": "Назар"})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "name@gmail.com"})
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
        labels = {
            "username": "Логін",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "nazar123"}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "service",
            "appointment_date",
            "appointment_time",
            "phone",
            "comment",
        ]
        labels = {
            "service": "Послуга",
            "appointment_date": "Дата",
            "appointment_time": "Час",
            "phone": "Номер телефону",
            "comment": "Коментар",
        }
        widgets = {
            "appointment_date": forms.DateInput(
                attrs={"type": "date", "id": "appointment-date"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "+380 00 000 00 00"}
            ),
            "comment": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Наприклад: хочу коротше з боків..."
                }
            ),
        }

    def clean_appointment_date(self):
        selected_date = self.cleaned_data["appointment_date"]
        if selected_date < date.today():
            raise forms.ValidationError("Не можна записатися на минулу дату.")
        return selected_date
