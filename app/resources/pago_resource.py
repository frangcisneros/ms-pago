from flask import Blueprint, request, jsonify
from app.models.pago import Pago
from app.repositories.pago_repository import PagoRepository
from app.services.ms_pago import PagoService

pago_bp = Blueprint("pago", __name__)
pago_service = PagoService()
pago_repository = PagoRepository()


@pago_bp.route("/pago", methods=["GET"])
# agregar documentacion
def index():
    # agregar inventario index
    return ".", 200


# borrar
@pago_bp.route("/pago/eliminar/<int:pago_id>", methods=["DELETE"])
def eliminar_pago(pago_id):
    """Elimina un pago por id."""
    pago_service.eliminar_pago(pago_id)
    return jsonify({"message": "Pago eliminado"}), 200


@pago_bp.route("/pago", methods=["POST"])
def crear_pago():
    """Crea un nuevo pago."""
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    producto_id = data.get("producto_id")
    precio = data.get("precio")
    medio_pago = data.get("medio_pago")

    try:
        nuevo_pago = pago_service.crear_pago(producto_id, precio, medio_pago)
        return jsonify({"id": nuevo_pago.id}), 201
    except ValueError as e:
        return (
            jsonify({"error": str(e)}),
            400,
        )  # Manejo de errores para precios negativos


@pago_bp.route("/pago/<int:producto_id>", methods=["GET"])
def obtener_pago(producto_id):
    """Obtiene un pago por producto_id."""
    pago = pago_service.obtener_pago(producto_id)
    if pago is None:
        return jsonify({"error": "Pago no encontrado"}), 404
    return (
        jsonify(
            {
                "producto_id": pago.producto_id,
                "precio": pago.precio,
                "medio_pago": pago.medio_pago,
            }
        ),
        200,
    )


@pago_bp.route("/pago/todos", methods=["GET"])  # Nuevo endpoint
def obtener_todos_los_pagos():
    """Obtiene todos los pagos existentes."""
    pagos = pago_repository.obtener_todos_los_pagos()
    return jsonify(
        [
            {
                "id": pago.id,
                "producto_id": pago.producto_id,
                "precio": pago.precio,
                "medio_pago": pago.medio_pago,
            }
            for pago in pagos
        ]
    )
