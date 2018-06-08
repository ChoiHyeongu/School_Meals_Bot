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
        'buttons': ['오늘 급식', '내일 급식']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

     #오늘
    todays = datetime.datetime.today()

    local_today = todays.strftime("%Y.%m.%d")
    local_toweekday = todays.weekday()
    #오늘

    #내일
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

    local_tomorrow = tomorrow.strftime("%Y.%m.%d")
    local_tmweekday = tomorrow.weekday()
    #내일

    if datacontent == '오늘 급식':

        today_meal = str(local_today)
        today_wkday = int(local_toweekday)

        #파싱
        tolunch = get_diet(2, today_meal, today_wkday)
        #파싱

        if len(tolunch) == 1:
            print_tomeal = "오늘 점심이 없습니다!" + "\n\n["+today_meal+"]"
        else:
            print_tomeal = "오늘 점심입니다!\n\n" + tolunch + "\n["+today_meal+"]"
            
        return JsonResponse({
            'message': {
                'text':print_tomeal
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 급식', '내일 급식']
            }

        })

    elif datacontent == "내일 급식":
        
        tomorrow_meal = str(local_tomorrow)
        tomorrow_wkday = int(local_tmweekday)

        #파싱
        tmlunch = get_diet(2, tomorrow_meal, tomorrow_wkday)
        #파싱
        
        if len(tmlunch) == 1:
             print_tmmeal = "내일 점심이 없습니다!" + "\n\n["+tomorrow_meal+"]"
        else:
            print_tmmeal = "내일 점심입니다!\n\n" + tmlunch + "\n["+tomorrow_meal+"]"

        return JsonResponse(
            {
                'message': {
                    'text': print_tmmeal
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘 급식', '내일 급식']
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
                    'buttons': ['오늘 급식', '내일 급식']
                }
            }
        )




