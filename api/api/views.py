from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Work, Artist, Client
from .serializers import WorkSerializer, ArtistSerializer
# from django.db.models import Q

class WorkListAPIView(APIView):
    def get(self, request, format=None):
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

class WorkFilterAPIView(APIView):
    def get(self, request, format=None):
        artist_name = request.GET.get('artist')
        work_type = request.GET.get('work_type')
        if artist_name is not None:
            works = Work.objects.filter(artist__name__icontains=artist_name)
        elif work_type is not None:
            works = Work.objects.filter(work_type__iexact=work_type)
        else:
            works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)



class ArtistSearchAPIView(APIView):
    def get(self, request, format=None):
        artist_name = request.GET.get('artist')
        artists = Artist.objects.filter(name__icontains=artist_name)
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        print('ok wait i am creating a user')
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(username=username, password=password)
            # client = Client(user_instance=user)
            # client.save()
        except:
            return Response({'error': 'User registration failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'success': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
