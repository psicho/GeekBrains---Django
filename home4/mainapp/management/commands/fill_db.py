from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Teach, Work
from datetime import date

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(selfself, *args, **options):
        works = [
            {'organization' = 'ОАО "ПетерСтар', 'sfere' = 'Телекоммуникации', 'region' = 'Санкт-Петербург',
            'site' = 'http://peterstar.ru','position' = 'Менеджер по продажам',
            'duties' = 'Поиск клиентов, презентация услуг, подписание договоров',
            'period' = '3 года', 'datestart' = '2006 г.', 'dateend' = '2009 года'
            },
            {'organization' = 'ОАО "ПетерСтар', 'sfere' = 'Телекоммуникации', 'region' = 'Санкт-Петербург',
            'site' = 'http://peterstar.ru', 'position' = 'Менеджер по продажам',
            'duties' = 'Поиск клиентов, презентация услуг, подписание договоров',
            'period' = '3 года', 'datestart' = '2009 г.', 'dateend' = 'по настоящее время'
            }
        ]
        teachs = [
            {'universitet' = 'БГТУ "ВОЕНМЕХ"', 'specials' = 'Испытание техники',
            'site' = 'http://voenmech.ru', 'datestart' = '2001 год',
            'dateend' = '2006 год'
            },
            {'universitet' = '"Международный Банковский Институт"', 'specials' = 'Стратегический менеджмент',
            'site' = 'http://www.ibispb.ru', 'datestart' = '2009 год',
            'dateend' = '2011 год'
            }
        ]
        for work in works:
            work = Work(**work)
            work.save()
        for teach in teachs:
            teach = Teach(**teach)
            teach.save()