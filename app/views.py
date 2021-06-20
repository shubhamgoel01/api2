from django.http import HttpResponse
from django.shortcuts import render
from api import urls
import json
import requests
# Create your views here.
def home(request):   
    response=requests.get('https://reqres.in/api/users?page=1').json() 


    response_length = len(response['data'])
    print(response_length)   # lenght of key : data 6 user
    for i in range(response_length):
        print(response['data'][i])        
  

    context = {
        'title': 'Shubham , lets start api',    
        'response':response
    }
    return render(request,'app/home.html',context)

 
