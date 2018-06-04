from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
import datetime, json  # datetime 모듈 import
from parser import *  # parser.py import


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    # date
    # 오늘
    dt1 = datetime.datetime.today()

    local_date1 = dt1.strftime("%Y.%m.%d")
    local_weekday1 = dt1.weekday()
    # 오늘

    # 내일
    dt2 = datetime.datetime.today() + datetime.timedelta(days=1)

    local_date2 = dt2.strftime("%Y.%m.%d")
    local_weekday2 = dt2.weekday()
    # 내일
    # date

    if datacontent == '오늘':

        # 시간 관련
        meal_date = str(local_date1)
        l_wkday = int(local_weekday1)
        # 시간 관련

        # 파싱
        l_l = get_diet(2, meal_date, l_wkday)
        d_d = get_diet(3, meal_date, l_wkday)
        # 파싱

        if len(l_l) == 1:
            lunch = "급식이 없습니다."
            dinner = ""
        elif len(d_d) == 1:
            lunch = meal_date + " 중식\n" + l_l
            dinner = ""
        else:
            lunch = meal_date + " 중식\n" + l_l
            dinner = meal_date + " 석식\n" + d_d

        return JsonResponse({
            'message': {
                'text': lunch + dinner
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })

    if datacontent == '내일':

        # 시간 관련
        meal_date = str(local_date1)
        l_wkday = int(local_weekday1)
        # 시간 관련

        # 파싱
        l_l = get_diet(2, meal_date, l_wkday)
        d_d = get_diet(3, meal_date, l_wkday)
        # 파싱

        if len(l_l) == 1:
            lunch = "급식이 없습니다."
            dinner = ""
        elif len(d_d) == 1:
            lunch = meal_date + " 중식\n" + l_l
            dinner = ""
        else:
            lunch = meal_date + " 중식\n" + l_l
            dinner = meal_date + " 석식\n" + d_d

        return JsonResponse({
            'message': {
                'text': lunch + dinner
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })