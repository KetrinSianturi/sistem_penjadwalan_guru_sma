
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from guru.models import Guru
from guru.models import Kelas
from guru.models import JadwalMengajar
from .serializers import GuruSerializer
from .serializers import KelasSerializer
from .serializers import JadwalSerializer
from rest_framework.permissions import IsAdminUser
from .serializers import JadwalSerializer

class GuruList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        guru_list = Guru.objects.all()
        serializer = GuruSerializer(guru_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Successfully added teacher.',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Validation failed.',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

class GuruDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get_object(self, pk):
        return get_object_or_404(Guru, pk=pk)

    def put(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = GuruSerializer(guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Guru updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = GuruSerializer(guru, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Guru partially updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        guru = self.get_object(pk)
        guru.delete()
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'Guru deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)     

class KelasList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        kelas_list = Kelas.objects.all()
        serializer = KelasSerializer(kelas_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KelasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Successfully added kelas.',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Validation failed.',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

class KelasDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get_object(self, pk):
        return get_object_or_404(Kelas, pk=pk)

    def put(self, request, pk, format=None):
        kelas = self.get_object(pk)
        serializer = KelasSerializer(kelas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Kelas updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        kelas = self.get_object(pk)
        serializer = KelasSerializer(kelas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Kelas partially updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        kelas = self.get_object(pk)
        kelas.delete()
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'Kelas deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)    
        
class JadwalList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        jadwal_list = JadwalMengajar.objects.all()
        serializer = JadwalSerializer(jadwal_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JadwalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Successfully added Jadwal.',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Validation failed.',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

class JadwalDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get_object(self, pk):
        return get_object_or_404(JadwalMengajar, pk=pk)

    def put(self, request, pk, format=None):
        jadwal = self.get_object(pk)
        serializer = JadwalSerializer(jadwal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'jadwal updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        jadwal = self.get_object(pk)
        serializer = JadwalSerializer(jadwal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Jadwal partially updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        jadwal = self.get_object(pk)
        jadwal.delete()
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'jadwal deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)
        