from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BusinessAdminConfig(AppConfig):
    name = 'businessadmin'
    verbose_name = _("Business Admin")
    verbose_name_plural = verbose_name
