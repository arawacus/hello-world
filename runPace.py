# Сколько секунд в 42 минутах и 42 секундах?
# Сколько миль в 10 километрах? Подсказка: одна миля равна 1,61 км.
# Если вы пробежали 10 километров за 42 минуты 42 секунды, каков ваш средний темп бега 
# (время, затраченное на преодоление мили, в минутах и секундах)? 
# Какова ваша средняя скорость в милях в час?”

class Solution:
    def speedCalc(self, time, dist):


        timeSec = time[-3] * 60 + time[-2] * 60 + time[-1]
        distMile = dist / 1.6
        resSec = timeSec / distMile

    def timeToSec(self, days, hours, min, sec):
        return(days * 24 * 3600 + hours * 3600 + min * 60 + sec)

    def timeFromSec(self, time):
        timeMin = time // 60
        timeSec = time % 60
        timeHour = 0
        timeDay = 0
        timeHour = 0
        timeMin = 0
        timeSec = 0
        if timeMin >= 60:
            timeHour = timeMin // 60
            timeMin =  timeMin % 60
            if timeHour >= 24:
                timeDay = timeHour // 24
                timeHour = timeHour % 24
                if timeDay >= 365:
                    timeYear = timeDay // 365
                    timeDay = timeDay % 365
        res = [timeYear, timeDay, timeHour, timeMin, timeSec]
        return res
                    
       
