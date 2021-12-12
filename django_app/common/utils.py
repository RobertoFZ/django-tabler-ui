from datetime import datetime, date as datetime_date
from dateutil.relativedelta import relativedelta

weekdays = {
    0: 'Lunes',
    1: 'Martes',
    2: 'Miércoles',
    3: 'Jueves',
    4: 'Viernes',
    5: 'Sábado',
    6: 'Domingo',
}

def incorrect_date(date, format='%d-%m-%Y'):
    try:
        datetime.strptime(date, format)
        return True
    except:
        return False


def add_months_to_date(date, months=1):
    return date + relativedelta(months=months)

def get_day_name_from_weekday(weekday):
    return weekdays[weekday]