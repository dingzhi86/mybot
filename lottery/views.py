from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Rarity, Item, Collection, Log, UserCollection
from random import choices
from django.core import serializers
import json
import arrow
import datetime

MAX_DRAWOUT = 11

def draw(data: list, k: int = 1):
    weights = [x.weight for x in data]
    return choices(data, weights=weights, k=k)


# Create your views here.
def index(request, qq, k):
    now = arrow.now()
    cnt = Log.objects.filter(qq=qq, time__gte=datetime.date.today()).count()
    # Log.objects.filter(qq=qq, item__collection=).distinct()
    if cnt + k > MAX_DRAWOUT:
        raise Http404
    print(qq)
    rarities = Rarity.objects.all()
    rarity_result = draw(rarities, k=k)
    ret = []
    collections = set()
    for rarity in rarity_result:
        items = Item.objects.filter(rarity=rarity)
        item = draw(items, k=1)[0]
        ret.append({"name": item.name, "rarity": item.rarity.name})
        log = Log.objects.create(qq=qq, item=item, time=now.format("YYYY-MM-DD HH:mm:ss"))
        log.save()
        collections.add(item.collection_id)
    cc = []
    for c in collections:
        cnt = UserCollection.objects.filter(qq=qq, collection_id=c)
        if cnt.exists():
            continue
        a = Log.objects.filter(qq=qq, item__collection_id=c).select_related("item").distinct()
        ids = set()
        for i in a:
            ids.add(i.item.id)
        print(a)
        if len(ids) == Item.objects.filter(collection_id=c).count():
            obj = Collection.objects.get(id=c)
            cc.append(obj.name)
            UserCollection.objects.create(qq=qq, collection_id=c, time=now.format("YYYY-MM-DD HH:mm:ss")).save()

    print("套装", cc)
    result = {
        "item": ret,
        "collection": cc
    }
    return JsonResponse(result, safe=False)
