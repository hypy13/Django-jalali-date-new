from django.conf import settings
from django.db.models import DateTimeField, DateField
from jalali_date_new.fields import JalaliDateTimeField, JalaliDateField
from jalali_date_new.utils import datetime2jalali, to_georgian
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
        if value:
            value = datetime2jalali(value).strftime(
                getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d %H:%M:%S")
            )
        return value

    def pre_save(self, model_instance, add):
        if val := getattr(model_instance, self.attname, None):
            if isinstance(val, str):
                return to_georgian(val, getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d %H:%M:%S"))

        return super().pre_save(model_instance, add)


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
        if value:
            value = datetime2jalali(value).strftime(
                getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d")
            )
        return value

    def pre_save(self, model_instance, add):
        if val := getattr(model_instance, self.attname, None):
            if isinstance(val, str):
                return to_georgian(val, getattr(settings, 'JDATE_FORMAT', "%Y-%m-%d"))

        return super().pre_save(model_instance, add)
