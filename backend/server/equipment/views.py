from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.conf import settings
from .models import Dataset
import pandas as pd
import os

class UploadCSV(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=400)

        file = request.FILES['file']
        filename = default_storage.save(file.name, file)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        try:
            df = pd.read_csv(file_path, sep=None, engine='python')
            df.columns = df.columns.str.strip()

            summary = {
                "total_equipment": int(len(df)),
                "avg_flowrate": float(df['Flowrate'].mean()),
                "avg_pressure": float(df['Pressure'].mean()),
                "avg_temperature": float(df['Temperature'].mean()),
                "type_distribution": df['Type'].value_counts().to_dict()
            }

            Dataset.objects.create(name=file.name, summary=summary)

            if Dataset.objects.count() > 5:
                Dataset.objects.order_by('uploaded_at').first().delete()

            return Response(summary)

        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class History(APIView):
    def get(self, request):
        data = Dataset.objects.order_by('-uploaded_at').values()
        return Response(list(data))
