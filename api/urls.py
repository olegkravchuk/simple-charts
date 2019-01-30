from django.contrib import admin
from django.urls import path
from api.company_service import get_companies
from api.buyer_service import get_buyers
from api.department_service import get_departments
from api.requester_service import get_requesters
from api.status_service import get_statuses
from api.category_service import get_categories
from api.information_service import get_information

urlpatterns = [
    path('companies', get_companies),

    path('buyers', get_buyers),

    path('departments', get_departments),

    path('requesters', get_requesters),

    path('statuses', get_statuses),

    path('categories', get_categories),

    path('information', get_information),
]
