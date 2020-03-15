from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField("部件名称", max_length=255, unique=True)
    weight = models.FloatField("部件权重", default=1)
    collection = models.ForeignKey('Collection', db_column='', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="套装")
    rarity = models.ForeignKey('Rarity', db_column='', on_delete=models.PROTECT, null=False, blank=False, verbose_name="稀有度")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部件"
        verbose_name_plural = "部件"


class Collection(models.Model):
    name = models.CharField("套装名称", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "套装"
        verbose_name_plural = "套装"


class Rarity(models.Model):
    name = models.CharField("稀有度名称", max_length=255)
    weight = models.FloatField("稀有度权重", blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "稀有度"
        verbose_name_plural = "稀有度"

class Log(models.Model):
    qq = models.CharField("qq号", max_length=20)
    item = models.ForeignKey('Item', db_column='', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="部件")
    time = models.DateTimeField()


class UserCollection(models.Model):
    qq = models.CharField("qq号", max_length=20)
    collection = models.ForeignKey('Collection', db_column='', on_delete=models.PROTECT, null=False, blank=False, verbose_name="套装")
    time = models.DateTimeField()

