from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import serializer
from github import Github
import pdb
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
import requests
import json
from django.conf import settings
# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     # pdb.set_trace()
#     queryset = User.objects.all()

#     # # using username and password
#     # g = Github("arpitsodhi", "")
#     # print(g)
#     # for repo in g.get_user().get_repos():
#     #     print(repo.name)
#     #     repo.edit(has_wiki=False)
#     #     # to see all the available attributes and methods
#     #     print(dir(repo))
#     # # or using an access token
#     # g = Github("access_token")

#     # # Github Enterprise with custom hostname
#     # g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
#     # myobj = {'client_id': 'b1d5f590f154fe86e3a8','client_secret':'b47e96898e0f905eb6170db4413366e61af83344','grant_type':'password','username':'arpitsodhi','password':'Fratabalas!1'}
#     # yoko = requests.post('https://github.com/login/oauth/authorize', data = myobj)
#     # yoko = requests.post('')
#     # context = yoko.text()
#     # print(yoko)      
#     serializer_class = serializer.UserSerializer

client_id = settings.G_ID
secret = settings.G_SECRET

def get_data(request):
    return HttpResponseRedirect(f"https://github.com/login/oauth/authorize?client_id={client_id}")

def get_ddata(request):

    code = request.GET['code']
    info = requests.post(f'https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={secret}&code={code}', headers={"Accept":"application/json"}).json()
    access_token = info['access_token']
    # info = requests.get('https://api.github.com/user/emails', headers={"Authorization": f"token {access_token}"}).json()
    info = requests.post('https://api.github.com/user/emails').json()

    print(info)
    return HttpResponse(str(info))