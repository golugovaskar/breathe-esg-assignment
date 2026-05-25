from django.urls import path
from .views import ReviewEmissionView

urlpatterns = [
    path(
        "review/<int:record_id>/",
        ReviewEmissionView.as_view()
    ),
]