# -*- coding: utf-8 -*-

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

    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == "오늘":
        return JsonResponse(
            {
                'message': {
                    'text': '오늘 급식입니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘', '내일']
                }
            }
        )
    elif datacontent == "내일":
        return JsonResponse(
            {
                'message': {
                    'text': '오늘 급식입니다!'
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




