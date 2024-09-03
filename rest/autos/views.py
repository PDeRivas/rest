from django.shortcuts import render
from django.views import View
from autos.models import Auto
from autos.serializers import AutoSerializer
from django.http import JsonResponse

class Autos(View):
    def get(self, request):
        data = Auto.objects.all()
        serializer = AutoSerializer(data, many=True)
        return JsonResponse({'autos': serializer.data})