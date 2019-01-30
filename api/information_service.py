# coding=utf-8
from datetime import datetime

from django.http import JsonResponse
from django.forms.models import model_to_dict
from models.models import Information


def get_information(request):
    date_from = request.GET.get("from", "")
    date_to = request.GET.get("to", "")

    if date_from and date_to:
        date_from = datetime.strptime(date_from, "%m-%d-%Y").date()
        date_to = datetime.strptime(date_to, "%m-%d-%Y").date()

        response = [model_to_dict(item) for item in Information.objects.filter(
            request_date__range=[date_from, date_to]
        )]
    else:
        response = [model_to_dict(item) for item in Information.objects.all()]

    return JsonResponse(response, safe=False)
