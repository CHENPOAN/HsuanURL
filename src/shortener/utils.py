import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)  # 尋找settings.py裡參數'SHORTCODE_MAX'是否存在,不存在則使用預設值15(APP重複利用性,不靠config)



def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase+string.digits):
    # new_code = ""
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return "".join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    '''

    :param instance: 呼叫該method的model實體物件
    :param size:
    :return:
    '''
    new_code = code_generator(size=size)
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    Klass = instance.__class__  # HsuanURL
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
