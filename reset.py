import os
import xlrd

if __name__ == "__main__":
    # 在默认的环境中运行（第一个参数是Django运行的配置文件，第二个参数是当前项目运行的配置文件）
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybot.settings")

    # 导入Django
    import django
    django.setup()

    from django.contrib.auth.models import User
    # 运行Django项目

    # 对数据库中的表的相关操作
    d = User.objects.get(pk=3)
    d.set_password("yanyanyan")
    d.save()
