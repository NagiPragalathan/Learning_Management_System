import random, time, datetime, openai, json, os

from django.shortcuts import render, redirect
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ..models import Faculty_details, Users, Room, Message, RoomMember, ClassRooms, class_enrolled
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from bing_image_downloader import downloader
from LMS.settings import BASE_DIR


def base(request):
    return render(request,"sample.html")
