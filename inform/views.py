from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone
from parser import *
import datetime, json 
import json
 
def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['Today','Tomorrow']
                })
 
@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        recevied_json_data = json.loads(json_str)
        datacontent = recevied_json_data['content']
        
        #date

        #Today
        dt1 = datetime.datetime.today()

        local_date(1) = dt1.strftime("%Y.%m.%d")
        local_weekday1 = dt1.weekday()
        #Today

        #Tomorrow
        dt2 = datetime.datetime.today() + datetime.timedelta(days=1)

        local_date2 = dt2.strftime("%Y.%m.%d")
        local_weekday2 = dt2.weekday)()
        #Tomorrow
        #date
        
        if datacontent == 'Today':
                
                #Time
                meal_date = str(local_date1)
                1_wkday = int(local_weekday1)
                #Time

                #Parsing
                1_1 = get_diet(2, meal_date, 1_wkday)
                #Parsing

        if len(1_1) == 1:
                lunch = "급식이 없습니다."
        else:
                lunch = meal_date + l_l

        return JsonResponse({
                'message': {
                        'text': "Today's lunch is "+'\n'+lunch
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['Today','Tomorrow']
                }
        })
