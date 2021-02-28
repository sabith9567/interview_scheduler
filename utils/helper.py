import datetime
from datetimerange import DateTimeRange


def get_time_slots(start_time, end_time, time_diff):
    slots = set()
    while start_time <= end_time - time_diff:
        slots.add((start_time.time().strftime("%I:%M %p"),
                   (start_time + time_diff).time().strftime("%I:%M %p")))
        start_time = start_time + time_diff
    return slots


def create_time_range(start_time, end_time, date):
    start_time = datetime.datetime(year=date.year, month=date.month, day=date.day,
                                   hour=start_time.hour, minute=start_time.minute)
    end_time = datetime.datetime(year=date.year, month=date.month, day=date.day,
                                 hour=end_time.hour, minute=end_time.minute)

    return DateTimeRange(start_time, end_time)


def get_time_range_by_date(time_slot_obj):
    date_list = time_slot_obj.values('available_date').distinct()
    time_range_by_date = {}
    for date in date_list:
        time_slot = time_slot_obj.values('start_time', 'end_time').filter(available_date=date['available_date'])
        time_range_list = []
        for time in time_slot:
            available_time_list = create_time_range(time['start_time'], time['end_time'], date['available_date'])
            time_range_list.append(available_time_list)
        time_range_by_date[date['available_date'].strftime("%d/%m/%Y")] = time_range_list
    return time_range_by_date


def get_time_slot_by_date(time_slot_obj):
    time_slot_by_date = {}
    for date, slots in time_slot_obj.items():
        time_slot_sets = []
        for slot in slots:
            available_time_list = get_time_slots(slot.start_datetime, slot.end_datetime, datetime.timedelta(hours=1))
            time_slot_sets.append(available_time_list)
        if len(time_slot_sets) > 0:
            time_slot_by_date[date] = set.union(*time_slot_sets)

    data = {}
    for key, value in time_slot_by_date.items():
        data[key] = value
    return data