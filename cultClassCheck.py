from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
classToFind = ["FOOTBALL"]

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 

def getClassToFind(classToSearch):
    driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver',chrome_options=options)
    driver.get('https://www.cure.fit/cult/classbooking/15?centerId=15&pageType=classbooking')
    slots = driver.find_elements_by_class_name('booking-time-row-cell')
    notificationSlots = []
    for slot in slots:
        time = slot.find_elements_by_class_name('time-container')[0].find_element_by_class_name('time-text')
        football = [x for x in slot.find_elements_by_class_name('available-theme') if x.text in classToSearch]
        for f in football:
            notificationSlots.append([time.text,f.text])
    driver.close()
    return notificationSlots

def generateMessage():
    classes = getClassToFind(classToFind)
    message = "No Classes Found"
    print(classes)
    if len(classes) > 0 :
        message = ""
        for x in classes:
            message = message + x[0]+" - "+x[1]+"\n"

    return message


while True:
    time.sleep(600)
    toaster.show_toast("CULT CLASSES",generateMessage())

# firstSlot = slots[0].find_element_by_class_name('available-theme')

# print(firstSlot.text)