# coding=utf-8
from django.http import JsonResponse
from django.forms.models import model_to_dict
from models.models import Requester


def get_requesters(request):

    response = [model_to_dict(item) for item in Requester.objects.all()]

    return JsonResponse(response, safe=False)
