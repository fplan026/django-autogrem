from django.urls import path

from . import views

app_name = "finance"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    path("bill/new/", views.new_bill, name="new-bill"),
    path("<int:pk>/", views.RecurringBillDetailsView.as_view(), name="recurring-bill-detail"),
]