from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
import rest_framework.status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from user.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class StreamKey(ListAPIView):
    def post(self, request):

        username = self.request.data.get('username')
        try:
            streamKey = User.objects.get(username=username).stream_key
        except User.DoesNotExist:
            return Response({'detail': rest_framework.status.HTTP_404_NOT_FOUND})
        return Response({'privateStreamKey': streamKey, 'detail': rest_framework.status.HTTP_200_OK})
