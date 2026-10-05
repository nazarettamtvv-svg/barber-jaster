from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppointmentForm, RegisterForm
from .models import Appointment


SERVICES = [
    {
        "code": "haircut",
        "name": "Чоловіча стрижка",
        "price": 450,
        "description": "Підбір форми, стрижка та фінальний стайлінг.",
    },
    {
        "code": "beard",
        "name": "Оформлення бороди",
        "price": 300,
        "description": "Форма, контур і догляд для акуратного вигляду.",
    },
    {
        "code": "combo",
        "name": "Стрижка + борода",
        "price": 650,
        "description": "Повний образ за один візит.",
    },
    {
        "code": "machine",
        "name": "Стрижка машинкою",
        "price": 300,
        "description": "Швидко, чисто та акуратно.",
    },
]


def home(request):
    return render(request, "main/home.html", {"services": SERVICES})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Акаунт створено. Тепер можна записуватися.")
            return redirect("main:booking")
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form": form})


@login_required
def booking_view(request):
    initial_service = request.GET.get("service", "")

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user

            try:
                appointment.save()
            except IntegrityError:
                form.add_error(
                    None,
                    "Цей час уже зайнятий. Обери інший час або дату."
                )
            else:
                messages.success(
                    request,
                    "Готово! Ти успішно записався на прийом."
                )
                return redirect("main:my_bookings")
    else:
        form = AppointmentForm(initial={"service": initial_service})

    return render(request, "main/booking.html", {"form": form})


@login_required
def my_bookings(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(
        request,
        "main/my_bookings.html",
        {"appointments": appointments}
    )


@login_required
def cancel_booking(request, pk):
    appointment = get_object_or_404(
        Appointment,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Запис скасовано.")
        return redirect("main:my_bookings")

    return render(
        request,
        "main/cancel_booking.html",
        {"appointment": appointment}
    )
