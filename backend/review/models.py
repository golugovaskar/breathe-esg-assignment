from django.db import models
from django.contrib.auth.models import User
from emissions.models import EmissionRecord


class ReviewAction(models.Model):

    ACTION_CHOICES = [
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("FLAGGED", "FLAGGED"),
    ]

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    comment = models.TextField(blank=True)

    reviewed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action