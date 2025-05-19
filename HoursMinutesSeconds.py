def getHoursMinutesSeconds(totalSeconds):
    string_seconds=str(totalSeconds)
    minutes = (totalSeconds%3600)//60
    hours = totalSeconds//3600
    seconds_left=totalSeconds%60
    if totalSeconds <60:
        return string_seconds+'s'
    elif totalSeconds>= 60 and totalSeconds < 3600:
        return (str(minutes)+'m'+('' if seconds_left == 0 else ' '+str(seconds_left) + 's'))
    elif totalSeconds >= 3600:
        return str(hours)+'h'+('' if minutes == 0 else ' '+str(minutes) + 'm')+('' if seconds_left == 0 else ' '+str(seconds_left) + 's')



assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
