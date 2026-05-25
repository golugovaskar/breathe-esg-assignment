from django.db import models
from django.contrib.auth.models import User
from emissions.models import EmissionRecord


class AuditLog(models.Model):

    ACTION_CHOICES = [
        ("CREATED", "CREATED"),
        ("UPDATED", "UPDATED"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("FLAGGED", "FLAGGED"),
    ]

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    changed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    change_note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.emission_record.activity_type}"