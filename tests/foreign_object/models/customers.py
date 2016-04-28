from django.db import models
from django.db.models.fields.related import ForeignObject


class Address(models.Model):
    company = models.CharField(max_length=1)
    customer_id = models.IntegerField()

    class Meta(object):
        unique_together = [
            ("company", "customer_id"),
        ]


class Customer(models.Model):
    company = models.CharField(max_length=1)
    customer_id = models.IntegerField()
    address = ForeignObject(
        Address, models.CASCADE, null=True,
        # order mismatch the others ForepignObjects
        from_fields=["company", "customer_id"],
        to_fields=["company", "customer_id"]
    )

    class Meta(object):
        unique_together = [
            ("company", "customer_id"),
        ]


class Contact(models.Model):
    company_code = models.CharField(max_length=1)
    customer_code = models.IntegerField()
    # virtual field
    customer = ForeignObject(
        Customer, models.CASCADE, related_name='contacts',
        to_fields=["customer_id", "company"],
        from_fields=["customer_code", "company_code"]
    )