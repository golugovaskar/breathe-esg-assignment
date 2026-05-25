from django.urls import path
from .views import SAPUploadView, UtilityUploadView, TravelUploadView

urlpatterns = [
    path(
        "sap-upload/",
        SAPUploadView.as_view()
    ),

    path(
        "utility-upload/",
        UtilityUploadView.as_view()
    ),

    path(
        "travel-upload/",
        TravelUploadView.as_view()
    ),
]