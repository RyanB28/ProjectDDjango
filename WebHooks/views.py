from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def TestRepsonse(request):
    return JsonResponse({'fulfillmentText': 'This is Django test response from webhook.'}, safe=False)
    # # build a request object
    # req = json.loads(request.body)
    # # get action from json
    # action = req.get('queryResult').get('action')
    # # return a fulfillment message
    # fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    # # return response
    # return JsonResponse(fulfillmentText, safe=False)