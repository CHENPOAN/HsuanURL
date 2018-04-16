'''
    新增修改models.py後必執行
    python manage.py makemigrations
    python manage.py migrate
'''
from django.conf import settings
from django.db import models

# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

# Create your models here.

from .validator import validate_url
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)  # 尋找settings.py裡參數'SHORTCODE_MAX'是否存在,不存在則使用預設值15


class HsuanURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(HsuanURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = HsuanURL.objects.filter(id__gte=1)  # id大於等於1(gte=greater than equal)
        if items is not None and isinstance(items, int):
            qs = qs.order_by("id")[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id, q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class HsuanURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)  # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) # when model was created
    active      = models.BooleanField(default=True)
    # empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    # shortcode = models.CharField(max_length=15, null=False)  # 此欄位可以為空值
    # shortcode = models.CharField(max_length=15, default='defaultshortcode')  設預設值

    objects = HsuanURLManager()  # 呼叫HsuanURLManager並指配給objects(可自行改變指定對象)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)  # 將物件傳入method
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(HsuanURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path