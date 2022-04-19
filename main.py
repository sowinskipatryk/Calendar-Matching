# Given two schedules and working hours, return the time windows in which
# you can make an appointment of a certain length

my_schedule = [['9:00', '10:30'], ['12:00', '13:00'],
               ['16:00', '18:00']]

sb_schedule = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'],
               ['16:00', '17:00']]

my_workhours = ['9:00', '20:00']
sb_workhours = ['10:00', '18:30']

meeting_len = 30

common_schedule = []
time_windows = []


def convert_str_to_int(string):
    return int(string.replace(':', ''))


def limit_hours(schedule, workhours):
    while schedule[0][0] <= workhours[0] and schedule[0][1] <= workhours[0]:
        schedule.pop(0)
    while schedule[-1][0] >= workhours[1] and schedule[-1][1] >= workhours[1]:
        schedule.pop()
    for i in range(len(schedule)):
        if schedule[i][0] < workhours[0]:
            schedule[i][0] = workhours[0]
        if schedule[i][1] > workhours[1]:
            schedule[i][1] = workhours[1]


def convert_60_min_to_hour(time):
    if time % 100 >= 60:
        time += 40
    return time


def convert_back_to_string(integer):
    string = str(integer)
    return string[:-2]+':'+string[-2:]


for i in range(len(my_schedule)):
    my_schedule[i] = [convert_str_to_int(my_schedule[i][0]),
                      convert_str_to_int(my_schedule[i][1])]

for j in range(len(sb_schedule)):
    sb_schedule[j] = [convert_str_to_int(sb_schedule[j][0]),
                      convert_str_to_int(sb_schedule[j][1])]

my_workhours = [convert_str_to_int(my_workhours[0]),
                convert_str_to_int(my_workhours[1])]
sb_workhours = [convert_str_to_int(sb_workhours[0]),
                convert_str_to_int(sb_workhours[1])]

common_hours = [max(my_workhours[0], sb_workhours[0]),
                min(my_workhours[1], sb_workhours[1])]

limit_hours(my_schedule, common_hours)
limit_hours(sb_schedule, common_hours)

while sb_schedule and my_schedule:
    if my_schedule[0][0] < sb_schedule[0][0]:
        common_schedule.append(my_schedule.pop(0))
    else:
        common_schedule.append(sb_schedule.pop(0))
if my_schedule and not sb_schedule:
    common_schedule += my_schedule
if sb_schedule and not my_schedule:
    common_schedule += sb_schedule

if common_hours[0] + meeting_len <= common_schedule[0][0]:
    time_windows.append([common_hours[0], common_schedule[0][0]])

while common_schedule:
    if len(common_schedule) > 1 and common_schedule[0][1] >= common_schedule[1][1]:
        common_schedule.pop(1)
        continue
    if len(common_schedule) > 1 and common_schedule[0][1] + meeting_len <= common_schedule[1][0]:
        time_windows.append([common_schedule[0][1], common_schedule[1][0]])
    if len(common_schedule) == 1 and common_schedule[0][1] + meeting_len <= common_hours[1]:
        time_windows.append([common_schedule[0][1], common_hours[1]])
    common_schedule.pop(0)

for i in range(len(time_windows)):
    time_windows[i][0] = convert_back_to_string(time_windows[i][0])
    time_windows[i][1] = convert_back_to_string(time_windows[i][1])

print(time_windows)
