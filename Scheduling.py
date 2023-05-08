import datetime
import time
import time, winsound
import requests
import pygame


print(time.time())
print(time.ctime())
print(time.ctime(0))
'''

> time.time() returns the current time as a number in seconds since a specific reference 
point in the past (January 1, 1970). It's like a stopwatch that started counting when 
computers were invented.

> time.ctime(0) simply tells you the exact starting point of the time measurement used by
your computer, which is January 1, 1970, at midnight.
'''
print(time.ctime(1683532389.4307165))




url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

headers = {
	"X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
	"X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com"
}

start = time.time()

response = requests.get(url, headers=headers)

print("**********"+response.json()[0]['fact'])

stop = time.time()

seconds = stop - start


print('its took' , seconds ,'seconds to run the script!')


# for i in range(0,5):

	# print('beep')
	# time.sleep(1)

for i in range(0, 2):
	winsound.Beep(500,300)
	time.sleep(1)




# this code for playing sound-
pygame.mixer.init()
pygame.mixer.music.load('yeah.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	continue
print("**********"+'audio played', '\n')



for i in range(2):
	print('tick')
	time.sleep(1)
	print('tock')
	time.sleep(1)

print(datetime.datetime.now())
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)  # year,month,day,hour,minute,second
print(dt.year)
now = datetime.datetime.now()
print(datetime.datetime.fromtimestamp(10))


# %Y: Year with century (e.g., 2023)
# %m: Month as a zero-padded decimal number (e.g., 05 for May)
# %d: Day of the month as a zero-padded decimal number (e.g., 08)
# %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 15)
# %M: Minute as a zero-padded decimal number (e.g., 30)
# %S: Second as a zero-padded decimal number (e.g., 45)

print(dt.strftime("%d %B %y")) # string formatting time
print(now.strftime("%Hhr %Mmin %Ssec"))

