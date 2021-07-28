from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from user.utils import create_key
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            stream_key=create_key('K1ug4r4W', f'rtmp://90.188.92.68:1935/app/{validated_data["username"]}', 'signature',
                                  'policy',
                                  '{\"url_expire\":7955089345000}'),
            watch_key={create_key('K1ug4r4W', f'ws://90.188.92.68:3333/app/{validated_data["username"]}', 'signature',
                                  'policy',
                                  '{\"url_expire\":7955089345000}'),
                       create_key('K1ug4r4W', f'ws://90.188.92.68:3333/app/{validated_data["username"]}_720_60',
                                  'signature', 'policy',
                                  '{\"url_expire\":7955089345000}'),
                       create_key('K1ug4r4W', f'ws://90.188.92.68:3333/app/{validated_data["username"]}_720_30',
                                  'signature', 'policy',
                                  '{\"url_expire\":7955089345000}')}
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
