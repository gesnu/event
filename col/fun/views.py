import json
from django.shortcuts import render,redirect
from mongoengine import *
from certifi import *
from django.http import HttpResponse
from datetime import datetime
from . import document


mycert=where()
client=connect(host="mongodb+srv://gesnu:gesnu0512@cluster0.mqrrwjo.mongodb.net/?retryWrites=true&w=majority",db='poc',username='gesnu',password='gesnu0512',tlsCAFile=mycert)

# Create your views here.

def makeDelete(req,unique):
    receive=document.Event.objects(eveId=unique).first()
    receive.delete()
    return redirect('/fun/')

def makeEdit(req,num):
    if req.method=="POST":
        d=req.POST['eveid']
        nm=req.POST['evename']
        dt=req.POST['evedate']
        dp=req.POST['evedept']
        document.Event.objects(eveId=d).update_one(set__eveName=nm,set__eveDate=dt,set__eveDepartment=dp)
        return redirect('/fun/view')
    else:
        receive=document.Event.objects(eveId=num).first()
        return render(req,'edit.html',{"record":receive})

def makeRead(req,seriel):
    receive=document.Event.objects(eveId=seriel).first()
    return render(req,'one.html',{"data":receive})


def makecreate(req):
    if req.method=="POST":
        #print("POST accepted")
        nm=req.POST['evename']
        dt=req.POST['evedate']
        dp=req.POST['evedept']
        #print(nm,dt,dp)
        eve=document.Event()
        eve.initiate(nm,datetime.fromisoformat(dt),dp)
        #eve.initiate("Picconet11",datetime.fromisoformat("2022-12-20"),"CSE")
        eve.save()
        return render(req,'schedule.html',{"info":nm+" has scheduled"})
    else:
        return render(req,'schedule.html')
    #eve=document.Event()
    #eve.initiate(input("event name please:  "),datetime.fromisoformat(input("event date yyyy-mm-dd")),input("event organising department"))
    #eve.initiate("picconet11",datetime.fromisoform("2022-12-20"),"cse")
    #eve.save()
    #return HttpResponse('event has added')

def makelist(req):
    mine=document.Event.objects.all()
    '''for i in mine:
        print(i)'''
    '''return HttpResponse("event has listed")'''
    return render(req,'viewing.html',{"everything":mine})


def makepage(req):
    return render(req,"begin.html")
