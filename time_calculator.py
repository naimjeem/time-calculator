import datetime

def add_time(start, duration, weekday_name = ' '):

    start = datetime.datetime.strptime(start,'%I:%M %p')
    h_duration,m_duration = duration.split(':')
    t_duration = int(h_duration)*60 + int(m_duration)
    calc_time = start + datetime.timedelta(minutes=int(t_duration))
    day = calc_time.day
    time = calc_time.strftime('%I:%M %p')

    if day == 1:
        day_text = ''
    elif day == 2:
        day_text = '(next day)'
    else: 
        day_text = '('+ str(day-1) + ' days later)'

    list_weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if weekday_name != ' ' and day >= 2:
        weekday_name = weekday_name.lower().capitalize()
        weekday_name_index = list_weekdays.index(weekday_name) 
        i=1
        indexw = weekday_name_index
        while i != day:
            if indexw == 6:
                indexw = 0
                i+=1
            else:
                indexw = indexw + 1
                i+=1

        new_weekday_name =  list_weekdays[indexw]
        new_time = str(time + ', ' + new_weekday_name + ' ' + day_text)
    elif weekday_name != ' ' and day == 1:
        new_time = str(time + ', '+ weekday_name.lower().capitalize())
    else:
        new_time = str(time + ' ' + day_text)

    if new_time[0] == '0':
        new_time = new_time[1:]
    else:
        new_time = new_time

    return new_time.strip()