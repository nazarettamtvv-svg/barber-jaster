from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "service",
        "appointment_date",
        "appointment_time",
        "phone",
    )
    list_filter = ("service", "appointment_date")
    search_fields = ("user__username", "user__first_name", "phone")
