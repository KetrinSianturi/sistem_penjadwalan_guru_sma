from django.urls import path
from .views import GuruList
from .views import GuruDetail
from .views import KelasList
from .views import KelasDetail
from .views import JadwalDetail
from .views import JadwalList

app_name = 'api'

urlpatterns = [
    path('guru/', GuruList.as_view(), name='guru-list'),
    path('guru/<int:pk>/', GuruDetail.as_view(), name='guru-detail'),
    path('kelas/', KelasList.as_view(), name='kelas-list'),
    path('kelas/<int:pk>/', KelasDetail.as_view(), name='kelas-detail'),
    path('jadwal/', JadwalList.as_view(), name='jadwal-list'),
    path('jadwal/<int:pk>/', JadwalDetail.as_view(), name='jadwal-detail'),
]