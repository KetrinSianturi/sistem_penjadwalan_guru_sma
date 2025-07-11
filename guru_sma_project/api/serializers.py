from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from guru.models import Guru
from guru.models import Kelas
from guru.models import JadwalMengajar

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guru
        fields = ['id', 'nama', 'nip', 'mapel']  
    
    def create(self, validated_data):
        return Guru.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nama = validated_data.get('nama', instance.nama)
        instance.nip = validated_data.get('nip', instance.nip)
        instance.mapel = validated_data.get('mapel', instance.mapel)
        instance.save()
        return instance
    
class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = ['id', 'tingkat', 'nama_kelas'] 
    
    def create(self, validated_data):
        return Kelas.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tingkat = validated_data.get('tingkat', instance.tingkat)
        instance.nama_kelas = validated_data.get('nama_kelas', instance.nama_kelas)
        instance.save()
        return instance

class JadwalSerializer(serializers.ModelSerializer):

    class Meta:
        model = JadwalMengajar
        fields = ['id', 'guru', 'kelas', 'hari','jam_mulai','jam_selesai']  
    
    def create(self, validated_data):
        return JadwalMengajar.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.guru = validated_data.get('guru', instance.guru)
        instance.hari = validated_data.get('hari', instance.hari)
        instance.kelas = validated_data.get('kelas', instance.kelas)
        instance.jam_mulai = validated_data.get('jam_mulai', instance.jam_mulai)
        instance.jam_selesai = validated_data.get('jam_selesai', instance.jam_selesai)
        
        instance.save()
        return instance
