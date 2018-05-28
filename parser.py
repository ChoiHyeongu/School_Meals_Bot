import requests
from bs4 import BeautifulSoup
 

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html
 
 
def get_diet(code, ymd, weekend):
    schMmealScCode = code #int
    schYmd = ymd #str
 
    URL = (
            "http://stu.sen.go.kr/sts_sci_md01_001.do?"
            "schulCode=B100000519&schulCrseScCode=4&schulKndScCode=04"
            "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
        )
    html = get_html(URL)
    
    element = html
   
    return element
    
    meal = get_diet(2, "2017.12.26")
    print (meal)