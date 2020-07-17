import pyautogui as mouse
import time
import os
from datetime import datetime
from threading import Timer

# Open slack
def slack():
	# Open Slack
	mouse.hotkey('command','space')
	time.sleep(1)
	mouse.typewrite('slack')
	time.sleep(1)
	mouse.hotkey('return')
	time.sleep(7)
	channel_1()	

# Post to channel_one
def channel_1():
	# click on first slack channel
	mouse.hotkey('command','k')
	time.sleep(3)
	mouse.typewrite('name_of_first_slack_channel')
	time.sleep(3)
	mouse.hotkey('return')
	time.sleep(1)
	message_list = ["Here interesting message!", "here is another interesting message"]
	# click in input field
	for message in message_list:
		mouse.typewrite('New interesting message: ' + str(message) + ' isn\'t that interesting?.')
		mouse.hotkey('return')
		# Stay awake since screensaver time locked
		for num in range(3):
			time.sleep(540)
			mouse.moveTo(100,100,duration=2)
			mouse.moveTo(80,120,duration=2)
	channel_2()

# Post to second slack channel
def channel_2():
	mouse.hotkey('command','k')
	time.sleep(3)
	mouse.typewrite('name_of_Second_slack_channel')
	time.sleep(3)
	mouse.hotkey('return')
	time.sleep(1)
	links = ['https://I_am_a_link.com', 'https://I_am_another_link.com']
	for link in links:
		mouse.typewrite('Hey, check out this cool link I found! ' + str(link) + ' ')
		mouse.hotkey('return')
		for num in range(3):
			time.sleep(540)
			mouse.moveTo(100,100,duration=2)
			mouse.moveTo(80,120,duration=2)
	channel_3()

# Post to third slack channel
def channel_3():
	mouse.hotkey('command','k')
	time.sleep(3)
	mouse.typewrite('name_of_third_slack_channel')
	time.sleep(3)
	mouse.hotkey('return')
	time.sleep(1)
	article_links = ['list of interesting articles to share']
	for link in article_links:
		mouse.typewrite(str(link))
		mouse.hotkey('return')
		for num in range(3):
			time.sleep(540)
			mouse.moveTo(100,100,duration=2)
			mouse.moveTo(80,120,duration=2)
	shutdown()

# Shutdown after done
def shutdown():
	os.system('echo "hardcodedpassword" | sudo -S shutdown -h now')

def main():
	# Begin posts at a certain time
	x=datetime.today()
	y=x.replace(hour=17, minute=5, second=30, microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t = Timer(secs, slack)
	t.start()
	timeout = time.time() + secs 
	# Move the mouse occasionally until script is ready to begin to avoid Admin mandated screen locks
	while True:
		mouse.moveTo(100,100,duration=2)
		time.sleep(540)
		mouse.moveTo(80,120,duration=2)
		if time.time() >= timeout -10:
			break


if __name__=='__main__':
	main()

