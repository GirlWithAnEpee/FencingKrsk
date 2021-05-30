from django.db import models

# Create your models here.
class City(models.Model):
    """
    Модель - город
    """
    city = models.CharField(max_length=200, help_text="Введите город/иной населённый пункт (с большой буквы).")

    def __str__(self):
        return self.city

class Coach(models.Model):
    """
    Модель - тренер
    """
    fio = models.CharField(max_length=300, help_text="Введите фамилию, имя и отчество тренера (с большой буквы, полностью).")

    def __str__(self):
        return self.fio

class Place(models.Model):
    """
    Модель - место проведения соревнований
    """
    place = models.CharField(max_length=300, help_text="Введите название места (например, Спортзал №2 НГУ).")
    adres = models.CharField(max_length=200, help_text="Введите адрес (улица, дом, корпус при необходимости).")
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.place

class Sportclub(models.Model):
    """
    Модель - спортклуб (организация)
    """
    sportclub = models.CharField(max_length=300, help_text="Введите название спортклуба (например, Виктория).")
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.sportclub

class Category(models.Model):
    """
    Модель - возрастная категория
    """
    category = models.CharField(max_length=50, help_text="Введите название возрастной категории (например, дети).")
    ageto = models.IntegerField(help_text="Введите верхнюю границу возрастной категории в годах (например, 14).")

    def __str__(self):
        return self.category

class Level(models.Model):
    """
    Модель - уровень соревнований
    """
    level = models.CharField(max_length=100, help_text="Введите уровень соревнований (например, первенство города).")

    def __str__(self):
        return self.level

class Gender(models.Model):
    """
    Модель - пол
    """
    gender = models.CharField(max_length=10, help_text="Введите гендерную принадлежность спортсмена.")

    def __str__(self):
        return self.gender

class Rank(models.Model):
    """
    Модель - разряд/звание спортсмена
    """
    rank = models.CharField(max_length=5, help_text="Введите разряд/звание спортсмена (например, 1юн или МСМК)")

    def __str__(self):
        return self.rank

class Weapon(models.Model):
    """
    Модель - вид оружия
    """
    weapon = models.CharField(max_length=15, help_text="Введите вид оружия (например, шпага или рапира)")

    def __str__(self):
        return self.weapon

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Fencer(models.Model):
    """
    Модель - фехтовальщик.
    """
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    birthday = models.DateField()
    rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, null=True)
    coach = models.ForeignKey('Coach', on_delete=models.SET_NULL, null=True)
    sportclub = models.ForeignKey('Sportclub', on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField()

    def __str__(self):
        """
        """
        return self.surname+" "+self.name

    def get_absolute_url(self):
        """
        Возвращает url
        """
        return reverse('fencer-detail', args=[str(self.id)])

class Competition(models.Model):
    """
    Модель - соревнование.
    """
    title = models.CharField(max_length=500)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)
    weapon = models.ForeignKey('Weapon', on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
    datestart = models.DateField()
    dateend = models.DateField()

    def __str__(self):
        """
        """
        return self.title


    def get_absolute_url(self):
        """
        Возвращает url
        """
        return reverse('competition-detail', args=[str(self.id)])

class Result(models.Model):
    """
    Модель - результат.
    """
    fencer = models.ForeignKey('Fencer', on_delete=models.SET_NULL, null=True)
    competition = models.ForeignKey('Competition', on_delete=models.SET_NULL, null=True)
    result = models.IntegerField()

    def __str__(self):
        """
        """
        return self.fencer.surname+" "+self.fencer.name+" "+self.competition.title+" "+str(self.result)+" место"