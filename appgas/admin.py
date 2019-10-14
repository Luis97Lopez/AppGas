from django.contrib import admin
from .models import Usuario, Gasera,Unidad,PedidosXEmpleado,Pedido,DetallesPedido


admin.site.register(Usuario)
admin.site.register(Gasera)
admin.site.register(Unidad)
admin.site.register(PedidosXEmpleado)
admin.site.register(Pedido)
admin.site.register(DetallesPedido)
