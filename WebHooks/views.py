from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie


IntentFulfilmentText = {
    "DjangoTest" : ["Dit is vanuit 1", "This is a test"], 
    "DjangoTest2" : ["Dit is vanuit 2", "This is a test"],
    }

# Create your views here.
@csrf_exempt
def TestRepsonse(request):
    req = json.loads(request.body)
    IntentName = req["queryResult"]["intent"]["displayName"]
    FulfilmentText = IntentFulfilmentText[IntentName][0]
    print(IntentName, FulfilmentText)
    return JsonResponse({"fulfillmentText": FulfilmentText}, safe=False)