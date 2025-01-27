import abc
from datetime import date
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    """
    Python sourcery so we can make abstract Model classes

    Usage:
        class AbstractModelClass(models.Model, metaclass=AbstractModelMeta):
    """
    pass

class Transaction(models.Model, metaclass=AbstractModelMeta):
    """
    Abstract class representing a financial transaction.
    """
    name = models.CharField(max_length=30)
    # allows amounts up to 999,999.99
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    @abc.abstractmethod
    def is_recent(self) -> bool:
        pass

    class Meta:
        abstract = True

class Purchase(Transaction):
    """
    A one-time purchase.
    """
    transaction_date = models.DateField(default=date.today)

    def is_recent(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"Transaction on {self.transaction_date} of ${self.amount}"

class TimeUnit(models.TextChoices):
    """
    Represents a unit of time. Can be used as an option for selection fields.
    """
    YEAR = "Y", _("Year")
    MONTH = "M", _("Month")
    DAY = "D", _("Day")
    HOUR = "h", _("Hour")
    MINUTE = "m", _("Minute")
    SECOND = "s", _("Second")
    DAY_OF_WEEK = "DOW", _("Day of the week")
    DAY_OF_YEAR = "DOY", _("Day of the year")

class Bill(Transaction):
    """
    A recurring purchase with flexible duration options.
    """
    
    start_date = models.DateField(verbose_name="start date", default=date.today)
    is_indefinate = models.BooleanField(default=True)

    # In the Django admin any field with blank=False is marked as a required.
    # If you don't set a value for these fields your form will have a validation 
    # error even if the field is nullable!
    # 
    # ;tldr is to use both blank=True and null=True
    end_date = models.DateField(verbose_name="end date", blank=True, null=True)
    
    duration = models.IntegerField()
    duration_unit = models.CharField(max_length=3,
                                 choices=TimeUnit,
                                 default=TimeUnit.DAY)
    
    def is_recent(self) -> bool:
        return False
