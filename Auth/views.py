from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

@swagger_auto_schema(request_body=RegisterSerializer)
class RegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,*args,**kwargs):
        try:
            data = self.request.data
            email = data['email']
            role = data['role']
            password1 = data['password1']
            password2 = data['password2']
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'Error':'User with this email already exist'})
                else:
                    if len(password1) < 6 :
                        return Response({'Error':"Password Length should be greater than 6."})
                    else:
                        user = User.objects.create_user(email=email,password=password1,role=role)
                        user.save()
                        return Response({'Success':"User Created SuccessFully."})
            else:
                return Response({'Error':"Password didn't match."})       
        except Exception as ex:
            return Response({'Error':str(ex)})

@swagger_auto_schema()
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

@swagger_auto_schema(request_body=UserSerializer)
class UserDetails(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data,status.HTTP_200_OK)
    