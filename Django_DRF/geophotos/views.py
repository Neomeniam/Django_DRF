import logging
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import GeoPhoto
from .serializers import GeoPhotoSerializer
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

logger = logging.getLogger(__name__)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = GeoPhoto.objects.all()
    serializer_class = GeoPhotoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}[{current_time}] Received new photo upload request{Style.RESET_ALL}")
        logger.info(f"{Fore.GREEN}Received data: {request.data}{Style.RESET_ALL}")
        logger.info(f"{Fore.GREEN}Received FILES: {request.FILES}{Style.RESET_ALL}")
        
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            logger.error(f"{Fore.RED}Serializer errors: {serializer.errors}{Style.RESET_ALL}")
            return Response({
                "timestamp": current_time,
                "status": "error",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print(f"{Fore.GREEN}{Back.BLACK}{Style.BRIGHT}[{current_time}] Photo uploaded successfully{Style.RESET_ALL}")
            return Response({
                "timestamp": current_time,
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            logger.exception(f"{Fore.RED}Error occurred while saving the photo{Style.RESET_ALL}")
            return Response({
                "timestamp": current_time,
                "status": "error",
                "detail": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)