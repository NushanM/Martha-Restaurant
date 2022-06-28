from django.db import models

# Create your models here.

class MainDish(models.Model):
    #main_dish = models.CharField(max_length=200)
    dish = models.CharField(max_length=200)
    main_dish_price = models.FloatField()

    def __str__(self):
        return self.dish

class SideDishes(models.Model):
    side_dish = models.CharField(max_length=200)
    side_dish_price = models.FloatField()

    def __str__(self):
        return self.side_dish

class Dessert(models.Model):
    dessert = models.CharField(max_length=200)
    dessert_price = models.FloatField()

    def __str__(self):
        return self.dessert
    
class Order(models.Model):
    #main_dish = models.CharField(max_length=200)
    main_dish = models.ForeignKey(MainDish, on_delete=models.CASCADE)
    wadai = models.BooleanField()
    dhal = models.BooleanField()
    fish = models.BooleanField()
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date published')
    order_value = models.FloatField(default=0)

    def __str__(self):
        return self.main_dish.dish