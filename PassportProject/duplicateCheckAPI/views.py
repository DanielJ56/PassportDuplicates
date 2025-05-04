from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from duplicateCheckAPI.models import PERSON
from duplicateCheckAPI.serializers import PERSONSerializer
from django.http import JsonResponse
from django.http import HttpResponse
import json
# Create your views here.

@csrf_exempt
def check_duplicate_passnum(request):
    if (request.method == "POST"):
        #get user's passport number
        request_data = request.body
        request_json = json.loads(request_data)
        new_passnum = request_json["new_passport_num"]
        
        
       #retrieve previous passport number
        existing_users = PERSON.objects.all()
        person_serializer = PERSONSerializer(existing_users,many=True)
        list_of_passnum = []
        
        for i in person_serializer.data:
            parameters = list(i.items())
            
            passport_num = parameters[9][1]
            list_of_passnum.append(passport_num)
            
        if (new_passnum in list_of_passnum):
            json_response = {"duplicate_status":"True"}
            return JsonResponse(json_response)
        else:
            json_response = {"duplicate_status":"False"}
            return JsonResponse(json_response)
        