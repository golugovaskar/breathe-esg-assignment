import pandas as pd

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from tenants.models import Tenant
from ingestion.models import DataSource
from emissions.models import EmissionRecord


class SAPUploadView(APIView):

    def post(self, request):

        csv_file = request.FILES.get("file")

        if not csv_file:
            return Response(
                {"error": "CSV file required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            df = pd.read_csv(csv_file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Company"
            )

            source, _ = DataSource.objects.get_or_create(
                tenant=tenant,
                source_type="SAP"
            )

            for _, row in df.iterrows():

                quantity = float(row["quantity"])
                unit = row["unit"]

                normalized_value = quantity
                normalized_unit = unit

                if unit == "GAL":
                    normalized_value = quantity * 3.78541
                    normalized_unit = "L"

                suspicious = quantity <= 0

                EmissionRecord.objects.create(
                    tenant=tenant,
                    source=source,
                    activity_type=row["fuel_type"],
                    raw_value=quantity,
                    raw_unit=unit,
                    normalized_value=normalized_value,
                    normalized_unit=normalized_unit,
                    scope="SCOPE_1",
                    suspicious=suspicious
                )

            return Response({
                "message": "SAP CSV uploaded successfully"
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class UtilityUploadView(APIView):

    def post(self, request):

        csv_file = request.FILES.get("file")

        if not csv_file:
            return Response(
                {"error": "CSV file required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            df = pd.read_csv(csv_file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Company"
            )

            source, _ = DataSource.objects.get_or_create(
                tenant=tenant,
                source_type="UTILITY"
            )

            for _, row in df.iterrows():

                usage = float(row["usage_kwh"])

                suspicious = usage <= 0

                EmissionRecord.objects.create(
                    tenant=tenant,
                    source=source,
                    activity_type="Electricity",
                    raw_value=usage,
                    raw_unit="kWh",
                    normalized_value=usage,
                    normalized_unit="kWh",
                    scope="SCOPE_2",
                    suspicious=suspicious
                )

            return Response({
                "message": "Utility CSV uploaded successfully"
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
class TravelUploadView(APIView):

    def post(self, request):

        csv_file = request.FILES.get("file")

        if not csv_file:
            return Response(
                {"error": "CSV file required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            df = pd.read_csv(csv_file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Company"
            )

            source, _ = DataSource.objects.get_or_create(
                tenant=tenant,
                source_type="TRAVEL"
            )

            valid_types = ["flight", "hotel", "cab"]

            for _, row in df.iterrows():

                travel_type = str(row["travel_type"]).lower()

                suspicious = (
                    travel_type not in valid_types
                    or not row["from_location"]
                )

                EmissionRecord.objects.create(
                    tenant=tenant,
                    source=source,
                    activity_type=travel_type,
                    raw_value=1,
                    raw_unit="trip",
                    normalized_value=1,
                    normalized_unit="trip",
                    scope="SCOPE_3",
                    suspicious=suspicious
                )

            return Response({
                "message": "Travel CSV uploaded successfully"
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )            