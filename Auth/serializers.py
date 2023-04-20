from rest_framework import permissions,serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','password','email','role')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    # def create(self, validated_data):
    #     user = User.objects.create_user(password = validated_data['password']  ,
    #                                     email=validated_data['email'],role=validated_data['role'])
    #     return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only': True},
        }