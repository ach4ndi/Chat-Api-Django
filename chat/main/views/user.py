from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from main.serializers.user import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth.models import User

class UserCreationView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserLoginView(generics.GenericAPIView):
    permission_classes = ()
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        if user.check_password(request.data['password']):
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({
                "error": "Login Invalid"
            })
        

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserAllProfileView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        users = self.get_object()
        
        return Response(users)