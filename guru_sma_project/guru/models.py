from django.db import models

class Guru(models.Model):
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=20, unique=True)
    mapel = models.CharField(max_length=50)

class Kelas(models.Model):
    tingkat = models.CharField(max_length=10)
    nama_kelas = models.CharField(max_length=20)

class JadwalMengajar(models.Model):
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    hari = models.CharField(max_length=10)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
