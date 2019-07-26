from django.contrib import admin

from post.models import GunType, GunBrand, Gun, Rank, Personel, GunStorage, PersonelClass

admin.site.register(GunType)
admin.site.register(GunBrand)
admin.site.register(Gun)
admin.site.register(Rank)
admin.site.register(Personel)
admin.site.register(GunStorage)
admin.site.register(PersonelClass)


