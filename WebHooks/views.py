from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie


IntentFulfilmentText = {
    "Is_er_vandaag_iets_bijzonders" : ["Dit is vanuit 1", "This is a test"], 
    "Wat_moet_er_voor_morgen_gebeuren" : ["Dit is vanuit 2", "This is a test"],
    "Wat zijn de laatste updates" : ["Dit is vanuit 3"],
    "Wie_is_er_vandaag_jarig" : ["Dit is vanuit 4"],
    "" : "Something went wrong, try again later."
    }

# Create your views here.
@csrf_exempt
def TestRepsonse(request):
    req = json.loads(request.body)
    IntentName = None
    FulfilmentText = None
    try:
        IntentName = req["queryResult"]["intent"]["displayName"]
        FulfilmentText = IntentFulfilmentText[IntentName][0]
        print(IntentName, FulfilmentText)
    except:
        IntentName = ""
        FulfilmentText = "Something went wrong, please try again."
    finally:
        print(IntentName, FulfilmentText)
        return JsonResponse({"fulfillmentText": FulfilmentText}, safe=False)