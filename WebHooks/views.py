from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

from users import models as UserModels
from blog import models as BlogModels

import json
import datetime

IntentFulfilmentText = [
    "Is_er_vandaag_iets_bijzonders", 
    "Wat_moet_er_voor_morgen_gebeuren",
    "Wat zijn de laatste updates",
    "Wie_is_er_vandaag_jarig",
    "Wie_is_er_deze_maand_jarig",
    ""
    ]

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

def getResonse(IntentName):
    if(IntentName in IntentFulfilmentText):
        if("Wie_is_er_vandaag_jarig" == IntentName):
            # UserModels.Profile.user.username
            AllUser = UserModels.Profile.objects.all()
            BirthDaytoday = []
            ToDay = datetime.datetime.today()
            for item in AllUser:
                if(item.month == ToDay.month):
                    BirthDaytoday.append(item.Name)
            result = "Deze maand zijn er {len(BirthDaytoday)} mensen jarig, deze mensen zijn jarig: "
            for name in BirthDaytoday:
                result = result + name + " " 
            return result
    return "Something went wrong!"

