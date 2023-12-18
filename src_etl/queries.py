query_insertar_ventas = "INSERT INTO ventas (id_venta, id_cliente, id_producto, fecha_venta, cantidad, total) VALUES (%s, %s, %s, %s, %s)"

query_insertar_clientes = "INSERT INTO clientes (id_cliente, first_name, last_name, email, gender, city, country, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_productos = "INSERT INTO productos (id_producto, nombre_producto, categoría, precio, origen, descripción) VALUES (%s, %s, %s, %s, %s, %s)"
