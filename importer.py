import os
import xlrd

if __name__ == "__main__":
    # 在默认的环境中运行（第一个参数是Django运行的配置文件，第二个参数是当前项目运行的配置文件）
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybot.settings")

    # 导入Django
    import django

    # 运行Django项目
    django.setup()

    # 对数据库中的表的相关操作
    from lottery import models

    a = xlrd.open_workbook("工作簿.xlsx")
    sheet = a.sheet_by_name("Sheet1")
    for i in range(1, sheet.nrows):
        rarity = sheet.cell_value(i, 0)
        collection = sheet.cell_value(i, 1)
        name = sheet.cell_value(i, 2)
        object = models.Item.objects.filter(name=name)
        if not object.exists():
            r = models.Rarity.objects.filter(name=rarity)
            if len(collection)==0:
                c=[None, ]
            else:
                c = models.Collection.objects.filter(name=collection)
                if not c.exists():
                    d = models.Collection.objects.create(name=collection)
                    d.save()
                    c = [d,]
            if c[0] is None:
                i = models.Item.objects.create(name=name, weight=1, rarity=r[0])
            else:
                i = models.Item.objects.create(name=name, weight=1, collection=c[0], rarity=r[0])
            i.save()
