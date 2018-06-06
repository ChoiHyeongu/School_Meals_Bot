# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
from meal import *
import datetime, json  # datetime 모듈 import

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    #오늘
    dt1 = datetime.datetime.today()

    local_date1 = dt1.strftime.today()
    local_weekday1 = dt1.weekday()
    #오늘

    #내일
    dt2 = datetime.datetime.today() + datetime.timedelta(days=1)

    local_date2 = dt2.strftime("%Y.%m.%d")
    local_weekday2 = dt2.weekday()
    #내일

    if datacontent == '오늘':

        meal_date = str(local_date1)
        l_wkday = int(local_weekday1)

        l_l = get_diet(2, meal_date, l_wkday)

        if len(l_l) == 1:
            lunch = "급식이 없습니다."
        else:
            lunch = meal_date + "중식\n" + l_l

        return JsonResponse({
            'message': {
                'text': lunch
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })

    elif datacontent == "내일":
        
        answer = get_diet(2, "2018.06.08", 3)
        return JsonResponse(
            {
                'message': {
                    'text': answer
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘', '내일']
                }
            }
        )

    else:
        return JsonResponse(
            {
                'message': {
                    'text': '버튼이 아닙니다.'
                },
                'keyboard':{
                    'type': 'buttons',
                    'buttons': ['오늘', '내일']
                }
            }
        )




