import pyautogui
import keyboard
import time

def cautare_google():
  if pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\browser.png', confidence=0.7) !=None:
  	 camp_google=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\browser.png', confidence=0.7)
  	 pyautogui.click(camp_google)
  	 time.sleep(5)
  	 pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
  	 pyautogui.press('enter')
  else:
      print ("IMAGINEA NU SE AFLA PE ECRAN")
  time.sleep(5)
  if pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\cautare_subscribe.png', confidence=0.7) !=None:
  	 camp_subscribe=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\cautare_subscribe.png', confidence=0.7)
  	 pyautogui.click(camp_subscribe)
  	 camp_video=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\video.png', confidence=0.7)
  	 pyautogui.click(camp_video)
  time.sleep(3)
  

def coordonate():
	pyautogui.dragTo(x=342, y=720)
	#pyautogui.click(x=342, y=720)
	pyautogui.keyDown('CTRL')
	pyautogui.click()
	pyautogui.keyUp('CTRL')
	print(pyautogui.position())
	pyautogui.scroll(-400)
	
	

	


cautare_google()
coordonate()
#Point(x=458, y=518) #video
#Point(x=951, y=329) 
time.sleep(2)