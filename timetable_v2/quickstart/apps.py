from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'quickstart'

# it seem that you can only make models with the same name as the module you are working on
class SnippetsConfig(AppConfig):
    name = 'quickstart'
