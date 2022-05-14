import datetime


def format_date(dt, fmt="%Y-%m-%d %H:%M:%S"):
  return dt.strftime(fmt)


def format_now():
  return format_date(datetime.datetime.now())