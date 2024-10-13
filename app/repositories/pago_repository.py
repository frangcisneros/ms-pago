from app import db
from app.models.pago import Pago


class PagoRepository:

    @staticmethod
    def crear_pago(producto_id, precio, medio_pago):
        nuevo_pago = Pago(producto_id=producto_id, precio=precio, medio_pago=medio_pago)
        db.session.add(nuevo_pago)
        db.session.commit()
        return nuevo_pago

    @staticmethod
    def obtener_pago_por_producto_id(id):
        return Pago.query.filter(Pago.id == id).first()

    @staticmethod
    def obtener_todos_los_pagos():  # find_all
        return db.session.query(Pago).all()

    @staticmethod
    def eliminar_pago(pago):
        db.session.delete(pago)
        db.session.commit()
        return pago
