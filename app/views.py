from django.http import HttpResponse
from django.shortcuts import render
from api import urls
import json
import requests
# Create your views here.
def home(request):   
    count = 0
    temp = []    
    api_url = 'https://reqres.in/api/users?page='
    for i in range(1,13):
        response=requests.get(api_url + str(i)).json()  
        temp.append(response)
        count = count + len(response['data'])
        print(len(response['data']))  
        # print('\n',response[i])  
    return HttpResponse(count)
    



