#실습1
day_temps = [35, 34, 33, 32, 30]
print(day_temps)
print(len(day_temps))
empty_temps = []
print(len(empty_temps)) #0 인덱스 길이를 초과하면 IndexError 발생

#실습2
time_temps = [35, 34, 34, 35, 33, 36]
print(time_temps[0], "/", time_temps[2], "/", time_temps[-1])

#실습3
line = [30, 45, 55, 12, 32, 78]
first_line = line[0]
last_line = line[-1]
print(first_line + last_line, "/", (first_line + last_line)/2)

#실습4
temps = [22, 25, 26, 27, 30, 31, 32, 34, 35, 36]
print(temps[0:3])
print(temps[-3:])
print(len(temps[0:3]))

#실습5
testlist = [1,2,3,4,5,6,7,8,9,10,11,12]
first = testlist[:6]
print(first)
second = testlist[6:]
print(second)
print(len(first), len(second))

#실습6
temps2 = [22, 25, 26, 27, 240]
print(240 in temps2)
temps2[-1] = 24
print(temps2)
print(240 in temps2)