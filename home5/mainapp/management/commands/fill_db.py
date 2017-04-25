from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Teach, Work, Hobby
from datetime import date

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        works = [
            {'organization': 'ОАО "ПетерСтар', 'region': 'Санкт-Петербург',
             'site': 'http://peterstar.ru', 'sfera': 'Телекоммуникации', 'position': 'Менеджер по продажам',
             'duties': 'Поиск клиентов, презентация услуг, подписание договоров', 'period': '3',
             'datestart': '2006 г.', 'dateend': '2009 года'
            },
            {'organization': 'Orenge Business Servises', 'region': 'Санкт-Петербург',
            'site': 'http://orange-business.ru', 'sfera': 'Телекоммуникации', 'position': 'Менеджер по продажам',
            'duties': 'Поиск клиентов, презентация услуг, подписание договоров',
            'period': '3', 'datestart': '2009 г.', 'dateend': 'по настоящее время'
            }
        ]
        teachs = [
            {'universitet': 'БГТУ "ВОЕНМЕХ"', 'specials': 'Испытание техники',
            'site': 'http://voenmech.ru', 'datestart': '2001 год',
            'dateend': '2006 год'
            },
            {'universitet': '"Международный Банковский Институт"', 'specials': 'Стратегический менеджмент',
            'site': 'http://www.ibispb.ru', 'datestart': '2009 год',
            'dateend': '2011 год'
            }
        ]
        hobbis = [
            {'hobbyname': 'Плавание', 'hobbytext': 'Занимался плаванием более 10 лет. Достиг разряда КМС'
            },
            {'hobbyname': 'Полиатлон', 'hobbytext': 'Полиалон - это многоборье. Есть зимний полиатлон: лыжи, стрельба и подтягивание. В этом виде я достиг разряда КМС. '
                                                    'Есть летний полиатлон: может включать различные виды.'
             }
        ]
        for work in works:
            work = Work(**work)
            work.save()
        for teach in teachs:
            teach = Teach(**teach)
            teach.save()
        for hobby in hobbis:
            hobby = Hobby(**hobby)
            hobby.save()