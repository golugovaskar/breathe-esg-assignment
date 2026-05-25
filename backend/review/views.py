from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from emissions.models import EmissionRecord
from review.models import ReviewAction
from audit.models import AuditLog


class ReviewEmissionView(APIView):

    def post(self, request, record_id):

        action = request.data.get("action")
        comment = request.data.get("comment", "")

        try:
            emission_record = EmissionRecord.objects.get(id=record_id)

            emission_record.status = action
            emission_record.save()

            user = User.objects.first()

            ReviewAction.objects.create(
                emission_record=emission_record,
                reviewed_by=user,
                action=action,
                comment=comment
            )

            AuditLog.objects.create(
                emission_record=emission_record,
                action=action,
                changed_by=user,
                change_note=comment
            )

            return Response({
                "message": f"Record {action.lower()} successfully"
            })

        except EmissionRecord.DoesNotExist:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )