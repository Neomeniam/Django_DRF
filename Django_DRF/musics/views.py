# Create your views here.
from musics.models import Music
from musics.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from rest_framework import viewsets, permissions
from .permissions import IsOwner

# Create your views here.
#class MusicViewSet(viewsets.ModelViewSet):
#    queryset = Music.objects.all()
#    serializer_class = MusicSerializer
    #permission_classes = (IsAuthenticated,)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class MusicsViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    #permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Ensure that the user can only see their own photos
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user as the owner of the photo
        serializer.save(owner=self.request.user)