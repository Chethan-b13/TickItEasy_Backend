from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User


class RegisterApi(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

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