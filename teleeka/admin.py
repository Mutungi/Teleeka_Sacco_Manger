from django.contrib import admin

from . models import *


admin.site.register(Client)
admin.site.register(Deposit)
admin.site.register(Withdrwal)
admin.site.register(Group)


