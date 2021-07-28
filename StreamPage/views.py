from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
import requests
import rest_framework.status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User


def index(request):
    return render(request, 'main.html', )


class StreamName(APIView):
    def post(self, request):
        username = self.request.data.get('username')
        stream_name = self.request.data.get('stream_name')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': rest_framework.status.HTTP_404_NOT_FOUND})
        user.stream_name = stream_name
        user.save()
        return Response({'detail': rest_framework.status.HTTP_200_OK})


class StreamsOnline(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = requests.get("http://90.188.92.68:8081/v1/vhosts/default/apps/app/streams",
                                headers={'Authorization': 'Basic SzF1ZzRyNFc='})
        users = response.json()["response"]
        json = {}
        for username in users:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'detail': rest_framework.status.HTTP_404_NOT_FOUND})

            watch_keys = user.watch_key
            stream_name = user.stream_name
            json[f"{user.username}"] = [watch_keys, stream_name]


        return Response(json)
