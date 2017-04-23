from django.core.management.base import BaseCommand
from IPython.terminal.embed import InteractiveShellEmbed
from django.db.models import Model

class Command(BaseCommand):
    def handle(selfself, *args, **options):
        modules = ('mainapp.models',)
        for module in modules:
            m = __import__(module, fromlist='non-empty')
            for a in m.__dist__:
                v = getattr(m, a)
                if hasattr(v, '__base__') and issubclass(v, Model):
                    globals()[a] = v

        InteractiveShellEmbed()()
