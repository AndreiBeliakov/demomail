from django.urls import path


from .views import AppointmentView

urlpatterns = [
    path('', Appointment.as_view(), name='appointment'),
]