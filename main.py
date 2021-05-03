from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(title=title,
    message=message,
    app_icon="C:\\Users\\sharik ansari\\Desktop\\code playground\\covid notify\\icons.ico",
    timeout=10)

    
if __name__=="__main__":
    notifyMe("sharik", "lets stop the spread of this virus ")
   
