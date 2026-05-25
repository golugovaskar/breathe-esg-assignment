from django.urls import path
from .views import EmissionListView

urlpatterns = [
    path(
        "records/",
        EmissionListView.as_view()
    ),
]