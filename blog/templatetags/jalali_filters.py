from django import template
from jdatetime import datetime as jdatetime

register = template.Library()

@register.filter
def gregorian_to_jalali(date):
    if date:
        jalali_date = jdatetime.fromgregorian(date=date).date()
        return jalali_date
    return ''

@register.filter
def jalali_day(date):
    if date:
        jalali_date = jdatetime.fromgregorian(date=date).date()
        return jalali_date.day
    return ''

@register.filter
def jalali_month(date):
    if date:
        jalali_date = jdatetime.fromgregorian(date=date).date()
        return jalali_date.month
    return ''

@register.filter
def jalali_year(date):
    if date:
        jalali_date = jdatetime.fromgregorian(date=date).date()
        return jalali_date.year
    return ''

@register.filter
def jalali_month_name(date):
    if date:
        jalali_date = jdatetime.fromgregorian(date=date).date()
        month_number = jalali_date.month
        month_names = [
            'فروردین',
            'اردیبهشت',
            'خرداد',
            'تیر',
            'مرداد',
            'شهریور',
            'مهر',
            'آبان',
            'آذر',
            'دی',
            'بهمن',
            'اسفند'
        ]
        return month_names[month_number - 1]
    return ''