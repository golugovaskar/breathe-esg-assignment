from django.db import models
from tenants.models import Tenant
from ingestion.models import DataSource


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("FLAGGED", "FLAGGED"),
    ]

    SCOPE_CHOICES = [
        ("SCOPE_1", "SCOPE_1"),
        ("SCOPE_2", "SCOPE_2"),
        ("SCOPE_3", "SCOPE_3"),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(max_length=255)

    raw_value = models.FloatField()

    raw_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    suspicious = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_type