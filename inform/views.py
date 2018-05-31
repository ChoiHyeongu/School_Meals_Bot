from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
import datetime , json #datetime 모듈 import
from parser import * #parser.py import
 
def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['오늘급식','내일급식']
                })
 
@csrf_exempt
def message(request):
        json_str = ((request.body).decode('utf-8'))
        recevied_json_data = json.loads(json_str)
        datacontent = recevied_json_data['content'].encode('utf-8')
        
        #date

        #Today
        dt1 = datetime.datetime.today()

        local_date = dt1.strftime("%Y.%m.%d")
        local_date1 = dt1.strftime("%Y.%m.%d")
        local_weekday1 = dt1.weekday()
        #Today

        #Tomorrow
        dt2 = datetime.datetime.today() + datetime.timedelta(days=1)

        local_date2 = dt2.strftime("%Y.%m.%d")
        local_weekday2 = dt2.weekday()
        #Tomorrow
        #date
        
        if datacontent == '오늘급식':
                
                #Time
                meal_date = str(local_date1)
                l_wkday = int(local_weekday1)
                #Time

                #Parsing
                l_l = get_diet(2, meal_date, l_wkday)
                d_d = ged_diet(3, meal_date, l_wkday)
                #Parsing

        if len(l_l) == 1:
                lunch = "급식이 없습니다."
                dinner = ""
        elif len(d_d) == 1:
                lunch = meal_date + " 중식\n"+l_l
                dinner = ""
        else:
                lunch = meal_date + " 중식\n"+l_l
                dinner = meal_dae + " 석식\n"+d_d

        return JsonResponse({
                'message': {
                        'text': lunch + dinner
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['오늘급식','내일급식']
                }
        })
