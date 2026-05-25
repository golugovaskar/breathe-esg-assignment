from rest_framework.views import APIView
from rest_framework.response import Response

from emissions.models import EmissionRecord


class DashboardStatsView(APIView):

    def get(self, request):

        total_records = EmissionRecord.objects.count()

        approved_records = (
            EmissionRecord.objects.filter(
                status="APPROVED"
            ).count()
        )

        rejected_records = (
            EmissionRecord.objects.filter(
                status="REJECTED"
            ).count()
        )

        pending_records = (
            EmissionRecord.objects.filter(
                status="PENDING"
            ).count()
        )

        suspicious_records = (
            EmissionRecord.objects.filter(
                suspicious=True
            ).count()
        )

        scope_1_count = (
            EmissionRecord.objects.filter(
                scope="SCOPE_1"
            ).count()
        )

        scope_2_count = (
            EmissionRecord.objects.filter(
                scope="SCOPE_2"
            ).count()
        )

        scope_3_count = (
            EmissionRecord.objects.filter(
                scope="SCOPE_3"
            ).count()
        )

        return Response({
            "total_records": total_records,
            "approved_records": approved_records,
            "rejected_records": rejected_records,
            "pending_records": pending_records,
            "suspicious_records": suspicious_records,
            "scope_1_count": scope_1_count,
            "scope_2_count": scope_2_count,
            "scope_3_count": scope_3_count,
        })