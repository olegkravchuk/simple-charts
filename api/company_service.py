# coding=utf-8
from django.http import JsonResponse
from django.forms.models import model_to_dict
from models.models import Company


def get_companies(request):

    response = [model_to_dict(item) for item in Company.objects.all()]

    return JsonResponse(response, safe=False)
