from django.contrib import admin
from . import models


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_rarity', 'weight', 'get_collection']

    def get_collection(self, obj):
        return obj.collection

    def get_rarity(self, obj):
        return obj.rarity

    get_collection.short_description = "套装"
    get_rarity.short_description = "稀有度"


class ItemInline(admin.StackedInline):
    model = models.Item


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ItemInline, ]


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight']


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Rarity, DictionaryAdmin)
