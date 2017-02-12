from django.http import JsonResponse
import random


def getRequest(request):
    response_data = {}
    response_data['color'] = 'green'
    response_data['message'] = getMessage()
    response_data['notify'] = 'false'
    response_data['message_format'] = 'text'

    return JsonResponse(response_data)


def getMessage():
    message = ['u r an asshole', 'u r a dick', 'u r manboob']
    num = random.randint(0, len(message) - 1)
    return message[num]
