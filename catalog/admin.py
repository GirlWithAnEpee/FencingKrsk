from django.contrib import admin

# Register your models here.
from .models import City, Coach, Place, Sportclub, Category, Level, Fencer, Competition, Result, Weapon, Rank, Gender

class FencerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'gender','birthday', 'rank', 'coach', 'rate')
    list_filter = ('gender', 'rank', 'coach')

# Register the admin class with the associated model
admin.site.register(Fencer, FencerAdmin)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'weapon', 'gender', 'category', 'place', 'datestart', 'dateend')
    fields = ['title', 'level', 'weapon', 'gender', 'category', 'place', ('datestart', 'dateend')]
    list_filter = ('level', 'weapon', 'gender')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    pass

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place', 'adres', 'city')
    
@admin.register(Sportclub)
class SportclubAdmin(admin.ModelAdmin):
    list_display = ('sportclub', 'city')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Competition)
#admin.site.register(Result)

