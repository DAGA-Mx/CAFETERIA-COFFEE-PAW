from models import *

print("REGISTRO DE INVENTARIO Y USUARIOS: COFFE PAW!!")

### 7 DE MARZO DEL 2026

print(">>> CARGANDO MENÚ DE BEBIDAS...")
# Mezcla de clásicos, refrescantes y especialidades
b1 = Bebida(101, "Flat White", 65.0, "Chico", "CALIENTE", ["Leche de avena"])
b2 = Bebida(102, "Dirty Chai Latte", 75.0, "Grande", "CALIENTE", ["Shot extra de espresso"])
b3 = Bebida(103, "Matcha Tonic", 70.0, "Mediano", "FRIA", ["Rodaja de limón", "Hielo"])
b4 = Bebida(104, "Affogato Especial", 85.0, "Chico", "FRIA", ["Helado de vainilla", "Nuez"])
b5 = Bebida(105, "Cold Brew Lavanda", 65.0, "Grande", "FRIA", ["Jarabe de lavanda"])
b6 = Bebida(106, "Frappé de Taro", 80.0, "Grande", "FRIA", ["Crema batida", "Perlas de tapioca"])
b7 = Bebida(107, "Espresso Romano", 45.0, "Chico", "CALIENTE", ["Piel de limón"])
b8 = Bebida(108, "Caramel Macchiato", 70.0, "Grande", "CALIENTE", ["Extra caramelo"])
b9 = Bebida(109, "Limonada de Café", 55.0, "Mediano", "FRIA", ["Menta fresca"])
b10 = Bebida(110, "Chocolate Abuelita", 50.0, "Grande", "CALIENTE", ["Malvaviscos", "Canela"])


print(b1.mostrar_detalle())
print(b2.mostrar_detalle())
print(b3.mostrar_detalle())
print(b4.mostrar_detalle())
print(b5.mostrar_detalle())
print(b6.mostrar_detalle())
print(b7.mostrar_detalle())
print(b8.mostrar_detalle())
print(b9.mostrar_detalle())
print(b10.mostrar_detalle())


print("\n>>> CARGANDO MENÚ DE POSTRES (10 OBJETOS)")
p1 = Postre(201, "Avocado Toast con Huevo", 95.0, False, False)
p2 = Postre(202, "Galleta Choco-Sea Salt", 35.0, False, False)
p3 = Postre(203, "Cruasán de Almendras", 55.0, False, False)
p4 = Postre(204, "Brownie de Matchay Chocolate", 65.0, True, False)
p5 = Postre(205, "Muffin Keto de Berries", 60.0, False, True)
p6 = Postre(206, "Panqué de Plátano y Nuez", 45.0, True, False)
p7 = Postre(207, "Tarta de Frutos Rojos", 75.0, False, True)
p8 = Postre(208, "Babka de Chocolate", 55.0, False, False)
p9 = Postre(209, "Quiche de Tomate Deshidratado", 85.0, False, False)
p10 = Postre(210, "New York Cheesecake con Maracuyá", 80.0, False, False)

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())

### MARZO 8

print("\n>>> ALTA CLIENTES...")
c1 = Cliente(301, "Dilan Gonzalez", "dilan@gmail.com", 150)
c2 = Cliente(302, "Edgar Martinez", "carlos@email.com", 50)
c3 = Cliente(303, "Ana Sanchez", "ana@email.com", 300)
c4 = Cliente(304, "Willem Kmetsch", "willem@leprechaun.com", 500)
c5 = Cliente(305, "Jimena Rodriguez", "Jimez0@gmail.com", 20)
c6 = Cliente(306, "Scott Pilgrim", "pilgrim@sxbmb.com", 100)
c7 = Cliente(307, "Gerardo Lopez", "Gerry@gmail.com", 80)
c8 = Cliente(308, "Carlos Santana", "carl00sx@datacracks.com", 250)
c9 = Cliente(309, "Minerva Díaz", "minne@centlop.com", 180)
c10 = Cliente(310, "Pedro Perez", "peperez@email.com", 10)

print(c1.mostrar_detalle())
print(c2.mostrar_detalle())
print(c3.mostrar_detalle())
print(c4.mostrar_detalle())
print(c5.mostrar_detalle())
print(c6.mostrar_detalle())
print(c7.mostrar_detalle())
print(c8.mostrar_detalle())
print(c9.mostrar_detalle())
print(c10.mostrar_detalle())


print("\n>>> DANDO DE ALTA EMPLEADOS...")
# Estructura: (ID, Nombre, Email, Código, Puesto)
e1 = Empleado(401, "Carmy Berzatto", "carmy@cafeteria.com", "EMP01", "GERENTE")
e2 = Empleado(402, "Sydney Adamu", "sydney@cafeteria.com", "EMP02", "BARISTA")
e3 = Empleado(403, "Ted Lasso", "ted@cafeteria.com", "EMP03", "MESERO")
e4 = Empleado(404, "Claire Dunphy", "claire@cafeteria.com", "EMP04", "GERENTE")
e5 = Empleado(405, "Richie Jerimovich", "richie@cafeteria.com", "EMP05", "MESERO")
e6 = Empleado(406, "Marcus Brooks", "marcus@cafeteria.com", "EMP06", "BARISTA")
e7 = Empleado(407, "Donna Paulsen", "donna@cafeteria.com", "EMP07", "GERENTE")
e8 = Empleado(408, "Nick Miller", "nick@cafeteria.com", "EMP08", "BARISTA")
e9 = Empleado(409, "April Ludgate", "april@cafeteria.com", "EMP09", "MESERO")
e10 = Empleado(410, "Gunther", "gunther@cafeteria.com", "EMP10", "BARISTA")

print(e1.mostrar_detalle())
print(e2.mostrar_detalle())
print(e3.mostrar_detalle())
print(e4.mostrar_detalle())
print(e5.mostrar_detalle())
print(e6.mostrar_detalle())
print(e7.mostrar_detalle())
print(e8.mostrar_detalle())
print(e9.mostrar_detalle())
print(e10.mostrar_detalle())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---\n")


print(">>> INICIANDO PROCESO DE PEDIDO...")

### 9 DE MARZO

inventario_hoy = Inventario({"Café": 1000, "Leche": 500, "Azúcar": 200, "Hielo": 300})


print(f"Empleado en caja: {e2.nombre} ({e2.rol})")
print(f"Cliente: {c1.nombre} (Puntos: {c1.puntosFidelidad})")


print("\n[SISTEMA]: Seleccionando productos...")
productos_pedido = [b1, b6, p3]
for prod in productos_pedido:
    print(f" - Agregado: {prod.nombre}")


nuevo_pedido = Pedido(995, productos_pedido, "PENDIENTE", 0.0)
print(nuevo_pedido.validarStock(inventario_hoy))


print("\n>>> APLICANDO GESTIÓN COMERCIAL...")
print(nuevo_pedido.calcularTotal())
print("¿Desea canjear puntos a crédito?: SI (Canjeando 50 puntos = $50 de descuento)")
c1.canjearPuntos(50)
total_con_descuento = nuevo_pedido.total - 50.0
print(f"[SISTEMA]: ¡ÉXITO! - Descuento aplicado.")


print(f"\n[COCINA]: {e6.cambiarEstadoPedido('PREPARANDO')}")
print(f"[COCINA]: {e6.cambiarEstadoPedido('ENTREGADO')}")

print(f"\nResumen de Pedido #{nuevo_pedido.idPedido}:")
print(f"Cliente: {c1.nombre}")
print(f"Atendió: {e2.nombre}")
print(f"Artículos: {[p.nombre for p in nuevo_pedido.productos]}")
print(f"Total Final: ${total_con_descuento:.2f}")
print(f"Estado: PAGADO. Ticket generado en PDF.")
print(f"IMPRIMIENDO TICKET...")