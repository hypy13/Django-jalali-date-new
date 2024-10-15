from django.conf import settings
from django.db.models import DateTimeField, DateField
from jalali_date_new.fields import JalaliDateTimeField, JalaliDateField
from jalali_date_new.utils import datetime2jalali
from jalali_date_new.widgets import AdminJalaliDateTimeWidget, AdminJalaliDateWidget


class JalaliDateTimeModelField(DateTimeField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                'form_class': JalaliDateTimeField,
                "widget": AdminJalaliDateTimeWidget,
                **kwargs,
            }
        )

    def from_db_value(self, value, expression, connection):
        return datetime2jalali(value).strftime(
            getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d %H:%M:%S")
        )


class JalaliDateModelField(DateField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                'form_class': JalaliDateField,
                "widget": AdminJalaliDateWidget,
                **kwargs,
            }
        )

    def from_db_value(self, value, expression, connection):
        return datetime2jalali(value).strftime(
            getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d")
        )
