import pyautogui
import keyboard
import time
import instagram_explore as ie

def cautare_google():
  if pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\browser.png', confidence=0.7) !=None:
  	 camp_google=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\browser.png', confidence=0.7)
  	 pyautogui.click(camp_google)
  	 time.sleep(5)
  	 pyautogui.write("https://www.instagram.com/")
  	 pyautogui.press('enter')
  else:
      print ("IMAGINEA NU SE AFLA PE ECRAN")
  time.sleep(5)


  if pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\instasearc.png', confidence=0.7) !=None:
  	 camp_search=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\instasearc.png', confidence=0.7)
  	 pyautogui.click(camp_search)
  	 
  time.sleep(2)

  if pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\ct.png', confidence=0.7) !=None:
  	 camp_cauta=pyautogui.locateOnScreen(r'C:\Users\paula\OneDrive\Desktop\I.A\ct.png', confidence=0.7)
  	 pyautogui.click(camp_cauta)
  pyautogui.write("erasmusplusprojects")
  pyautogui.press('enter')
  

  time.sleep(3)


def coordonate():
  pyautogui.dragTo(x=243, y=377)
  pyautogui.click(x=243, y=377)
  
  time.sleep(3)

  pyautogui.dragTo(x=250, y=837)
  pyautogui.click(x=250, y=837)
  
  time.sleep(3)
  myScreenshot=pyautogui.screenshot()
  myScreenshot.save(r'C:\Users\paula\OneDrive\Desktop\I.A\Folder\schreenshot.png')
  
  #pyautogui.click()
  #pyautogui.keyUp('CTRL')
  #print(pyautogui.position())
  #pyautogui.scroll(-400)



cautare_google()
coordonate()

time.sleep(2)