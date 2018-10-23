from django.contrib import admin
from .models import Post
from .models import Tipo
from .models import MedPago
from .models import Incidencia

admin.site.register(Tipo)
admin.site.register(MedPago)
admin.site.register(Incidencia)
