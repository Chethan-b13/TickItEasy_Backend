from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,*args,**kwargs):
        data = self.request.data
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']

        try:
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'Error':'User with this email already exist'})
                else:
                    if len(password1) < 6 :
                        return Response({'Error':"Password Length should be greater than 6."})
                    else:
                        user = User.objects.create_user(email=email,password=password1)
                        user.save()
                        return Response({'Success':"User Created SuccessFully."})
            else:
                return Response({'Error':"Password didn't match."})       
        except Exception as ex:
            return Response({'Error':str(ex)})

class MakeAdminApi(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self,request,*args,**kwargs):
        req_user = request.user
        username = request.data['username']
        if req_user.is_staff and req_user.is_superuser:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return Response({
                "Success":"User Made as Admin"
            })
        else:
            return Response({
                "ForBidden":"You aren't an admin"
            })