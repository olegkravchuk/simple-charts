from decimal import *
from django.http import JsonResponse
from datetime import datetime
import xlrd
import os
from models.models import *

getcontext().prec = 14

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parser(request):
    file = os.path.join(BASE_DIR, 'DataforTest.xlsx')
    my_excel = xlrd.open_workbook(file)
    sheet = my_excel.sheet_by_index(0)

    for row_index, row_num in enumerate(range(sheet.nrows)):
        if row_index != 0:
            company, created = Company.objects.get_or_create(name=sheet.cell(row_index, 0).value)
            requester, created = Requester.objects.get_or_create(name=sheet.cell(row_index, 3).value)
            department, created = Department.objects.get_or_create(name=sheet.cell(row_index, 4).value)
            category, created = Category.objects.get_or_create(name=sheet.cell(row_index, 5).value)
            currency, created = Currency.objects.get_or_create(name=sheet.cell(row_index, 11).value)
            status, created = Status.objects.get_or_create(name=sheet.cell(row_index, 16).value)
            buyer, created = Buyer.objects.get_or_create(name=sheet.cell(row_index, 17).value)
            request_type, created = RequestType.objects.get_or_create(name=sheet.cell(row_index, 18).value)
            saving, created = Saving.objects.get_or_create(name=sheet.cell(row_index, 32).value)
            type_of_savings, created = TypeOfSavings.objects.get_or_create(name=sheet.cell(row_index, 33).value)
            Information.objects.create(
                company=company,
                request_number=sheet.cell(row_index, 1).value,
                request_date=datetime.strptime(sheet.cell(row_index, 2).value, "%d/%m/%Y").date(),
                requester=requester,
                department=department,
                category=category,
                description=sheet.cell(row_index, 6).value,
                quantity_required=sheet.cell(row_index, 7).value,
                unit_of_measure=sheet.cell(row_index, 8).value,
                estimated_unit_price=float(sheet.cell(row_index, 9).value),
                total_estimated_price=float(sheet.cell(row_index, 10).value),
                currency=currency,
                delivery_location=sheet.cell(row_index, 12).value,
                date_required=datetime.strptime(sheet.cell(row_index, 13).value, "%d/%m/%Y").date(),
                emergency=True if sheet.cell(row_index, 14).value == "Yes" else False,
                sample_required=True if sheet.cell(row_index, 15).value == "Yes" else False,
                status=status,
                buyer=buyer,
                request_type=request_type,
                item=sheet.cell(row_index, 19).value,
                quote=sheet.cell(row_index, 20).value if sheet.cell(row_index, 20).value else None,
                round=sheet.cell(row_index, 21).value if sheet.cell(row_index, 21).value else None,
                exact_match=True if sheet.cell(row_index, 22).value == "Yes" else False,
                quote_requested_date=datetime.strptime(sheet.cell(row_index, 23).value, "%d/%m/%Y").date() if sheet.cell(row_index, 23).value else None,
                suppliers=sheet.cell(row_index, 24).value,
                quote_received_date=datetime.strptime(sheet.cell(row_index, 25).value, "%d/%m/%Y").date() if sheet.cell(row_index, 25).value else None,
                quoted_unit_price=float(sheet.cell(row_index, 26).value) if sheet.cell(row_index, 26).value else None,
                total_quote_price=float(sheet.cell(row_index, 27).value) if sheet.cell(row_index, 27).value else None,
                quote_submitted_date=datetime.strptime(sheet.cell(row_index, 28).value, "%d/%m/%Y").date() if sheet.cell(row_index, 28).value and sheet.cell(row_index, 28).value != "None" else None,
                quote_selected=True if sheet.cell(row_index, 29).value == "Yes" else False,
                quote_accepted_date=datetime.strptime(sheet.cell(row_index, 30).value, "%d/%m/%Y").date() if sheet.cell(row_index, 30).value else None,
                forecast=sheet.cell(row_index, 31).value,
                saving=saving,
                type_of_savings=type_of_savings,
                baseline_spend=float(sheet.cell(row_index, 34).value) if sheet.cell(row_index, 34).value else None,
                savings_amount=float(sheet.cell(row_index, 35).value) if sheet.cell(row_index, 35).value else None,
                savings_percent=float(sheet.cell(row_index, 36).value) if sheet.cell(row_index, 36).value else None,
                savings_levels_applied=sheet.cell(row_index, 37).value,
                request_to_quote_cycle_time=sheet.cell(row_index, 38).value,
                supplier_response_cycle_time=sheet.cell(row_index, 39).value,
                quote_acceptance_cycle_time=sheet.cell(row_index, 40).value,
            )

    return JsonResponse({
        'count': Information.objects.count()
    })
