from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
import datetime , json
import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


def get_diet(code, ymd, weekday):
    schMmealScCode = code #int
    schYmd = ymd #str

    num = weekday + 1
    URL = (
            "http://stu.sen.go.kr/sts_sci_md01_001.do?"
            "schulCode=B100000593&schulCrseScCode=4&schulKndScCode=04"
            "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
        )
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all("tr")
    element = element[2].find_all('td')
    try:
        element = element[num] #num
        element = str(element)
        element = element.replace('[', '')
        element = element.replace(']', '')
        element = element.replace('<br/>', '\n')
        element = element.replace('<td class="textC last">', '')
        element = element.replace('<td class="textC">', '')
        element = element.replace('</td>', '')
        element = element.replace('(h)', '')
        element = element.replace('.', '')
        element = re.sub(r"\d", "", element)
    except:
        element = " "
    return element

def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘 급식', '내일 급식', '주간 급식', '학사일정', '봇 정보']
    })

def get_meal(dt, weekday):

    local_date = dt.strftime("%Y.%m.%d")

    lunch = get_diet(2, local_date, weekday)

    if len(lunch) == 1:
        print_lunch = " 급식이 없습니다!"
    else:
        print_lunch = " 급식입니다!\n" + "──────────────\n" +lunch + "──────────────"

    return print_lunch

def ret_proc(output, date, return_key):

    if return_key == 1:
        return JsonResponse({
            'message': {
                'text': date + output
         },
          @csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '주간 급식':

         return JsonResponse(
            {
                'message': {
                    'text': "요일을 고르세요!"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['월요일', '화요일', '수요일','목요일', '금요일', '나가기']
                }
            }
        )

    elif datacontent == "오늘 급식":

        t_lunch = datetime.datetime.today()
        t_weekday1 = t_lunch.weekday()
        diet = get_meal(t_lunch, t_weekday1)
        return ret_proc(diet, "오늘", 0)

    elif datacontent == "내일 급식":

        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        t_weekday2 = tomorrow.weekday()
        diet = get_meal(tomorrow, t_weekday2)
        return ret_proc(diet, "내일", 0)


    elif datacontent == "월요일":

        weekday1 = datetime.datetime.today();
        diet = get_meal(weekday1, 0)
        return ret_proc(diet, "월요일", 1)

    elif datacontent == "화요일":

        weekday2 = datetime.datetime.today();
        diet = get_meal(weekday2, 1)
        return ret_proc(diet, "화요일", 1)

         'keyboard': {
             'type': 'buttons',
             'buttons': ['월요일', '화요일', '수요일','목요일', '금요일', '나가기']
         }
     })
    else:
         return JsonResponse({
            'message': {
                'text': date + output
         },
         'keyboard': {
             'type': 'buttons',
             'buttons': ['오늘 급식', '내일 급식', '주간 급식', '봇 정보']
         }
     })
    
    elif datacontent == "수요일":

        weekday3 = datetime.datetime.today();
        diet = get_meal(weekday3, 2)
        return ret_proc(diet, "수요일", 1)

    elif datacontent == "목요일":

        weekday4 = datetime.datetime.today();
        diet = get_meal(weekday4, 3)
        return ret_proc(diet, "목요일", 1)

    elif datacontent == "금요일":

        weekday5 = datetime.datetime.today();
        diet = get_meal(weekday5, 4)
        return ret_proc(diet, "금요일", 1)

    elif datacontent == "나가기":

       return JsonResponse(
            {
                'message': {
                    'text': "나가기를 누르셨습니다!"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘 급식', '내일 급식', '주간 급식', '봇 정보']
                }
            }
       )


