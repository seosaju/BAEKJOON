month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_sum = 0

month, day = map(int, input().split())
for i in range(month):
    day_sum += month_list[i]
day_sum += day
print(day_list[day_sum % 7])
