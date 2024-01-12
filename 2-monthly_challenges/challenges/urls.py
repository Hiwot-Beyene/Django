from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenges_inNumber, name="monthly_challenges_inNumber"),
    path("<str:month>", views.monthly_challenges, name="monthly_challenges"),
]
