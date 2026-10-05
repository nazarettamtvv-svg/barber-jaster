from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service",
                    models.CharField(
                        choices=[
                            ("haircut", "Чоловіча стрижка"),
                            ("beard", "Оформлення бороди"),
                            ("combo", "Стрижка + борода"),
                            ("machine", "Стрижка машинкою"),
                        ],
                        max_length=30,
                    ),
                ),
                ("appointment_date", models.DateField()),
                (
                    "appointment_time",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=5,
                    ),
                ),
                ("phone", models.CharField(max_length=20)),
                ("comment", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["appointment_date", "appointment_time"],
            },
        ),
        migrations.AddConstraint(
            model_name="appointment",
            constraint=models.UniqueConstraint(
                fields=("appointment_date", "appointment_time"),
                name="unique_booking_slot",
            ),
        ),
    ]
