from datetime import datetime
from django.utils.timezone import get_current_timezone


def get_dates(dates_input):
    dates = dict()

    ''' min_date definition '''
    min_date_str = dates_input[0].split('/')
    min_date_day = int(min_date_str[0])
    min_date_month = int(min_date_str[1])
    min_date_year = int(min_date_str[2])
    dates['min_date'] = datetime(min_date_year, min_date_month, min_date_day, tzinfo=get_current_timezone())
    ''' max_date definition '''
    max_date_str = dates_input[2].split('/')
    max_date_day = int(max_date_str[0])
    max_date_month = int(max_date_str[1])
    max_date_year = int(max_date_str[2])
    dates['max_date'] = datetime(max_date_year, max_date_month, max_date_day, 23, 59, 59, 999999, tzinfo=get_current_timezone())

    return dates
