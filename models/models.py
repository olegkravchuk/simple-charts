# coding=utf-8
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Requester(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RequestType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Saving(models.Model):
    name = models.CharField(max_length=255)  # Realized / Unrealized

    def __str__(self):
        return self.name


class TypeOfSavings(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Information(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    request_number = models.CharField(max_length=255)
    request_date = models.DateField()
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    quantity_required = models.PositiveIntegerField()
    unit_of_measure = models.CharField(max_length=10)
    estimated_unit_price = models.FloatField()
    total_estimated_price = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    delivery_location = models.TextField(null=True, blank=True)
    date_required = models.DateField()
    emergency = models.BooleanField(default=False)
    sample_required = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    request_type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, null=True, blank=True)
    quote = models.PositiveIntegerField(null=True, blank=True)
    round = models.PositiveIntegerField(null=True, blank=True)
    exact_match = models.BooleanField(default=False)
    quote_requested_date = models.DateField(null=True, blank=True)
    suppliers = models.CharField(max_length=255)
    quote_received_date = models.DateField(null=True, blank=True)
    quoted_unit_price = models.FloatField(null=True, blank=True)
    total_quote_price = models.FloatField(null=True, blank=True)
    quote_submitted_date = models.DateField(null=True, blank=True)
    quote_selected = models.BooleanField(default=False)
    quote_accepted_date = models.DateField(null=True, blank=True)
    forecast = models.CharField(max_length=255, null=True, blank=True)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE, null=True)
    type_of_savings = models.ForeignKey(TypeOfSavings, on_delete=models.CASCADE, null=True)
    baseline_spend = models.FloatField(null=True, blank=True)
    savings_amount = models.FloatField(null=True, blank=True)
    savings_percent = models.FloatField(null=True, blank=True)
    savings_levels_applied = models.CharField(max_length=255, null=True, blank=True)
    request_to_quote_cycle_time = models.CharField(max_length=255, null=True, blank=True)
    supplier_response_cycle_time = models.CharField(max_length=255, null=True, blank=True)
    quote_acceptance_cycle_time = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.request_number
