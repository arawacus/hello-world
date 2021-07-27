# Сколько секунд в 42 минутах и 42 секундах?
# Сколько миль в 10 километрах? Подсказка: одна миля равна 1,61 км.
# Если вы пробежали 10 километров за 42 минуты 42 секунды, каков ваш средний темп бега 
# (время, затраченное на преодоление мили, в минутах и секундах)? 
# Какова ваша средняя скорость в милях в час?”
# new text
timeSec = 42 * 60 + 42
print("total {} sec".format(timeSec))

distMile  = 10 / 1.61
print("{} miles".format(distMile))
runPace = timeSec / distMile
print("1 mile for {} sec".format(runPace))
timeMin = runPace // 60 
timeRest = runPace % 60 
print("{} minut, {} secund".format(timeMin, timeRest))
speed = 10 * 3600 / timeSec
print("A speed = {}".format(speed))