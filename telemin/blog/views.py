from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class Post(APIView):
    def get(self, request, format=None):
        usernames = None