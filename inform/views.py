# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
from meal import *
import datetime, json, sys  

plasterMessage = "#연속동일요청입니다. 나중에 다시 시도해주세요."

def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘 급식', '내일 급식', '날씨']
    })

class user_chk():
    
    def __init__(self):
        self.pre_key = ""  #previous user_key
        self.now_key = ""  #now user_key

    def check(self, key):
        self.now_key = key

        if self.pre_key == self.now_key :
            passcode = 1
        else :
            self.pre_key = self.now_key
            passcode = 0
        return passcode

u0 = user_chk()
u1 = user_chk()
u2 = user_chk()

def get_meal(dt):
    
    local_date = dt.strftime("%Y.%m.%d")
    local_weekday = dt.weekday()

    lunch = get_diet(2, local_date, local_weekday)

    if len(lunch) == 1:
        print_lunch = "급식이 없습니다!\n" + "["+local_date+"]"
    else:
        print_lunch = "오늘 점심입니다!\n\n" + lunch + "\n["+local_date+"]"

    return print_lunch

def ret_proc(output, date):
    
    return JsonResponse({
        'message': {
            'text': date + output
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['오늘 급식', '내일 급식', '날씨']
        }
    })    



@csrf_exempt
def answer(request):
    
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    user_key = received_json_data['user_key']


    if datacontent == '오늘 급식':
        if u0.check(user_key):
            return ret_proc(plasterMessage, "")

        today = datetime.datetime.today()
        diet = get_meal(today)
        return ret_proc(diet, "오늘 ")


    elif datacontent == "내일 급식":
       
        if u1.check(user_key):
            return ret_proc(plasterMessage, "")

        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        diet = get_meal(tomorrow)
        return ret_proc(diet, "내일 ")

    
    elif datacontent == "날씨":

        return JsonResponse(
            {
                'message': {
                    'text': "아직 구현되지 않았습니다. 조금만 기다려주세요!"
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘 급식', '내일 급식', '날씨']
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
                    'buttons': ['오늘 급식', '내일 급식', '날씨']
                }
            }
        )




