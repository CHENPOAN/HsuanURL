'''
    自定義 Management Commands
'''
from django.core.management.base import BaseCommand, CommandError

from shortener.models import HsuanURL  # 引入需使用的model

class Command(BaseCommand):
    '''
    執行此 Command
    '''
    help = 'Refresh all HsuanURL shortcodes'

    def add_arguments(self, parser):
        '''
        加入 Command 後的參數
        '''
        parser.add_argument('items', type=int)  # 如果參數名前加'--',則Command要下'--參數名'

    def handle(self, *args, **options):
        '''
        執行此 Command 後的動作
        :param args:
        :param options: 參數集合(dicts)
        :return: 回傳 HsuanURL 裡的動作
        '''
        return HsuanURL.objects.refresh_shortcodes(items=options['items'])