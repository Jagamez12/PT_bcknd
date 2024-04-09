from rest_framework import generics, authentication, permissions
from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import CustomUser
from rest_framework.authtoken.views import ObtainAuthToken 
# Create your views here.

class CreateUSerView(generics.CreateAPIView):
    serializer_class = UserSerializer

class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer