from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import GeoPhoto
from .serializers import GeoPhotoSerializer
from .permissions import IsOwner

class GeoPhotoListView(generics.ListCreateAPIView):
    serializer_class = GeoPhotoSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        # Return only the photos that belong to the authenticated user
        return GeoPhoto.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the owner to the authenticated user
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeoPhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GeoPhotoSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        # Return only the photos that belong to the authenticated user
        return GeoPhoto.objects.filter(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)