from django.db import models
from tenants.models import Tenant


class DataSource(models.Model):
    SOURCE_TYPES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="data_sources"
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.tenant.name} - {self.source_type}"