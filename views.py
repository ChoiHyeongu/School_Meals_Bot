  else:
        print_lunch = " 급식입니다!\n" + "──────────────\n" +lunch + "──────────────"

    return print_lunch

def ret_proc(output, date, return_key):

    if return_key == 1:
        return JsonResponse({
            'message': {
                'text': date + output
         },
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

             
