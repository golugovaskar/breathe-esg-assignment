from rest_framework.views import APIView
from rest_framework.response import Response

from .models import EmissionRecord


class EmissionListView(APIView):

    def get(self, request):

        data = []

        records = EmissionRecord.objects.all()

        for record in records:
            data.append({
                "id": record.id,
                "activity_type": record.activity_type,
                "scope": record.scope,
                "status": record.status,
                "suspicious": record.suspicious,
            })

        return Response(data)