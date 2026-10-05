from django.conf import settings
from django.db import models


class Appointment(models.Model):
    SERVICE_CHOICES = [
        ("haircut", "Чоловіча стрижка"),
        ("beard", "Оформлення бороди"),
        ("combo", "Стрижка + борода"),
        ("machine", "Стрижка машинкою"),
    ]

    TIME_CHOICES = [
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments"
    )
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    phone = models.CharField(max_length=20)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date", "appointment_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["appointment_date", "appointment_time"],
                name="unique_booking_slot"
            )
        ]

    def __str__(self):
        return (
            f"{self.user.username} — {self.get_service_display()} — "
            f"{self.appointment_date} {self.appointment_time}"
        )
