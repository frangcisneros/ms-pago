from app.repositories.pago_repository import PagoRepository
from app.models import Pago
from datetime import datetime
from app import cache


class PagoService:
    def __init__(self):
        self.pago_repository = PagoRepository()

    def crear_pago(self, producto_id, precio, medio_pago):
        pago = PagoRepository.crear_pago(producto_id, precio, medio_pago)
        cache.set(f'pago_{pago.id}', pago, timeout=15)
        return pago

    def obtener_pago(self, producto_id):
        """Obtiene un pago específico por producto_id."""
        return self.pago_repository.obtener_pago_por_producto_id(producto_id)

    def obtener_todos_los_pagos(self):
        result=cache.get('pagos')
        if result is None:
            result=PagoRepository.obtener_todos_los_pagos()
            cache.set('pagos',result,timeout=15)
        return result

    def eliminar_pago(self, pago_id):
        pago = self.pago_repository.obtener_pago_por_producto_id(pago_id)
        self.pago_repository.eliminar_pago(pago)
