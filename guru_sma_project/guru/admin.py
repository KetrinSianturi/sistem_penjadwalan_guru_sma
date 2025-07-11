from django.contrib import admin

from .models import Guru, JadwalMengajar, Kelas
admin.site.register(Guru)
admin.site.register(Kelas)
admin.site.register(JadwalMengajar)
