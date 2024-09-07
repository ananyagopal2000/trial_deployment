from django.shortcuts import render
import requests

def home(requests):
    print('inside views-home function')
    return render('authentication/home.html')