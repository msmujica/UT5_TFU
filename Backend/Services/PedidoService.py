from Repositories.PedidoRepositories import PedidoRepository
from Controllers.PagoFactory import PagoFactory


class PedidoService:

    def __init__(self):
        self.pedido_repository = PedidoRepository()

    def obtener_pedidos_en_preparacion(self):
        pedidos = self.pedido_repository.obtener_pedidos_en_preparacion()
        return pedidos

    def obtener_pedidos_del_dia_por_estado(self):
        pedidos = self.pedido_repository.obtener_pedidos_del_dia()

        pedidos_por_estado = {
            "PENDIENTE": [],
            "EN_PREPARACION": [],
            "LISTO": [],
            "ENTREGADO": [],
            "CANCELADO": []
        }

        for pedido in pedidos:
            estado = pedido.estado

            if estado in pedidos_por_estado:
                pedidos_por_estado[estado].append(pedido)
            else:
                pedidos_por_estado[estado] = [pedido]

        return pedidos_por_estado

    def registrar_pedido(self, datos):
        ids = [item.id_producto for item in datos.items]
        productos_db = self.pedido_repository.obtener_productos_por_ids(ids)
        productos_map = {p["id_producto"]: p for p in productos_db}

        for item in datos.items:
            if item.id_producto not in productos_map:
                raise ValueError(f"Producto con id {item.id_producto} no encontrado")
            if not productos_map[item.id_producto]["activo"]:
                raise ValueError(f"Producto '{productos_map[item.id_producto]['nombre']}' no está disponible")

        items_calculados = []
        for item in datos.items:
            producto = productos_map[item.id_producto]
            precio_unitario = float(producto["precio"])
            subtotal = precio_unitario * item.cantidad
            items_calculados.append({
                "id_producto": item.id_producto,
                "nombre": producto["nombre"],
                "cantidad": item.cantidad,
                "precio_unitario": precio_unitario,
                "subtotal": subtotal
            })

        medio_pago = PagoFactory.crear(datos.medio_pago)

        pedido = self.pedido_repository.registrar_pedido(
            celular_cliente=datos.celular_cliente,
            id_empleado=datos.id_empleado,
            medio_pago=medio_pago,
            items_calculados=items_calculados
        )

        return pedido, items_calculados

    def cancelar_pedido(self, id_pedido):
        return self.pedido_repository.cancelar_pedido(id_pedido)