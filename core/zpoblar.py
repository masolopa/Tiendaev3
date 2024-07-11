import sqlite3
from django.contrib.auth.models import User, Permission
from django.db import connection
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()

    crear_usuario(
        username='cevans',
        tipo='Cliente', 
        nombre='Chris', 
        apellido='Evans', 
        correo=test_user_email if test_user_email else 'cevans@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='25.747.200-0',	
        direccion='123 Main Street, Los Angeles, \nCalifornia 90001 \nEstados Unidos', 
        subscrito=True, 
        imagen='perfiles/cevans.jpg')

    crear_usuario(
        username='eolsen',
        tipo='Cliente', 
        nombre='Elizabeth', 
        apellido='Olsen', 
        correo=test_user_email if test_user_email else 'eolsen@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='12.202.357-5', 
        direccion='Albert Street, New York, \nNew York 10001 \nEstados Unidos', 
        subscrito=True, 
        imagen='perfiles/eolsen.jpg')

    crear_usuario(
        username='tholland',
        tipo='Cliente', 
        nombre='Tom', 
        apellido='Holland', 
        correo=test_user_email if test_user_email else 'tholland@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='11.991.600-3', 
        direccion='105 Apple Park Way, \nCupertino, CA 95014 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/tholland.jpg')

    crear_usuario(
        username='sjohansson',
        tipo='Cliente', 
        nombre='Scarlett', 
        apellido='Johansson', 
        correo=test_user_email if test_user_email else 'sjohansson@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='350 5th Ave, \nNew York, NY 10118 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/sjohansson.jpg')

    crear_usuario(
        username='cpratt',
        tipo='Administrador', 
        nombre='Chris', 
        apellido='Pratt', 
        correo=test_user_email if test_user_email else 'cpratt@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='19.441.980-5', 
        direccion='10 Pine Road, Miami, \nFlorida 33101 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/cpratt.jpg')
    
    crear_usuario(
        username='mruffalo',
        tipo='Administrador', 
        nombre='Mark', 
        apellido='Ruffalo', 
        correo=test_user_email if test_user_email else 'mruffalo@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='21.708.052-5', 
        direccion='1600 Pennsylvania Avenue NW, \nWashington, D.C. \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/mruffalo.jpg')

    crear_usuario(
        username='super',
        tipo='Superusuario',
        nombre='Robert',
        apellido='Downey Jr.',
        correo=test_user_email if test_user_email else 'rdowneyjr@marvel.com',
        es_superusuario=True,
        es_staff=True,
        rut='13.029.317-4',
        direccion='15 Oak Street, Los Angeles, \nCalifornia 90001 \nEstados Unidos',
        subscrito=False,
        imagen='perfiles/rdowneyjr.jpg')
    
    categorias_data = [
        { 'id': 1, 'nombre': 'Bottom'},
        { 'id': 2, 'nombre': 'Top'},
        { 'id': 3, 'nombre': 'Overall y conjuntos'},
        { 'id': 4, 'nombre': 'Accesorios y calzado'},
    ]

    print('Crear categorías')
    for categoria in categorias_data:
        Categoria.objects.create(**categoria)
    print('Categorías creadas correctamente')

    productos_data = [

        {
            'id': 1,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Pantalón de lino',
            'descripcion': 'Nuestro pantalón de lino es la elección ideal para días calurosos. Ligero, fresco y elegante, ofrece comodidad y estilo en cada uso. Su diseño versátil se adapta a cualquier ocasión, desde eventos formales hasta salidas casuales. ¡Añádelo a tu guardarropa y disfruta de su suavidad y frescura!',
            'precio': 10990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000001.jpg'
        },
        {
            'id': 2,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Overall a cuadros',
            'descripcion': 'Este overall a cuadros rojo y blanco combina estilo y comodidad. Con un diseño llamativo y fresco, es perfecto para un look casual y divertido. Versátil y cómodo, ideal para cualquier ocasión. ¡Añade un toque de originalidad a tu guardarropa!',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000002.jpg'
        },
        {
            'id': 3,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Baggy jeans',
            'descripcion': 'Estos baggy jeans combinan estilo y comodidad a la perfección. Con un corte amplio y relajado, son ideales para un look casual y moderno. Versátiles y fáciles de combinar, se convertirán en tu prenda favorita para cualquier ocasión. ¡Atrévete a lucir con actitud!',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000003.jpg'
        },
        {
            'id': 4,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Camisa',
            'descripcion': 'Nuestra camisa es una pieza esencial en cualquier guardarropa. Confeccionada con materiales de alta calidad, ofrece un ajuste cómodo y un estilo versátil. Perfecta para combinar con cualquier atuendo, desde formal hasta casual. ¡Añade elegancia y frescura a tu día a día!',
            'precio': 9990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000004.jpg'
        },
        {
            'id': 5,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Falda',
            'descripcion': 'Esta falda larga negra es un clásico atemporal. Con su elegante caída y diseño versátil, es perfecta para cualquier ocasión, desde eventos formales hasta salidas casuales. Comodidad y estilo se unen en esta prenda imprescindible. ¡Luce sofisticad@ y chic con cada paso!',
            'precio': 9990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 20,
            'imagen': 'productos/000005.jpg'
        },
        {
            'id': 6,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Chaqueta',
            'descripcion': 'Nuestra chaqueta de cuero sintético aporta un toque rebelde y moderno a cualquier atuendo. Con un diseño elegante y resistente, es perfecta para cualquier temporada. Ideal para un look urbano y sofisticado. ¡Hazla tu prenda de referencia y destaca con estilo!',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000006.jpg'
        },
        {
            'id': 7,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Vestido',
            'descripcion': 'Este vestido holgado es la definición de comodidad y estilo. Con su corte amplio y fluido, es perfecto para cualquier ocasión, desde días relajados hasta salidas especiales. Fresco, versátil y elegante, es una pieza esencial en tu guardarropa. ¡Siéntete libre y fabulos@ en cada momento!',
            'precio': 9990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000007.jpg'
        },
        {
            'id': 8,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Camiseta estampada',
            'descripcion': 'Nuestra camiseta estampada añade un toque de personalidad a tu look diario. Confeccionada con materiales suaves y transpirables, ofrece comodidad y estilo. Perfecta para combinar con jeans o faldas, es una prenda versátil que destaca en cualquier ocasión. ¡Expresa tu estilo único con esta camiseta!',
            'precio': 7990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000008.jpg'
        },

        {
            'id': 9,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Vestón',
            'descripcion': 'Nuestro vestón aporta un toque de sofisticación y elegancia a tu atuendo. Con un diseño clásico y un ajuste impecable, es perfecto para ocasiones formales y eventos especiales. Confeccionado con materiales de alta calidad, ofrece comodidad y estilo duradero. ¡Destaca con confianza en cualquier ocasión!',
            'precio': 59990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000009.jpg'
        },
        {
            'id': 10,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Chaleco de punto',
            'descripcion': 'Este chaleco de punto es la capa perfecta para añadir calidez y estilo a tu atuendo. Suave y cómodo, ideal para cualquier temporada. Versátil y elegante, complementa tanto looks formales como casuales. ¡Incorpora esta pieza esencial a tu colección!',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 20,
            'imagen': 'productos/000010.jpg'
        },
        {
            'id': 11,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Pantalones',
            'descripcion': 'Nuestros pantalones cargo combinan funcionalidad y estilo. Con múltiples bolsillos y un diseño resistente, son perfectos para un look casual y práctico. Versátiles y cómodos, ideales para cualquier aventura. ¡Añade un toque utilitario a tu guardarropa!',
            'precio': 18990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000011.jpg'
        },
        {
            'id': 12,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Vest',
            'descripcion': 'Este vest es la prenda ideal para añadir un toque de elegancia a cualquier atuendo. Con un diseño clásico y versátil, es perfecto para ocasiones formales y casuales. Confeccionado con materiales de alta calidad, ofrece comodidad y estilo en cada uso. ¡Incorpora esta pieza esencial a tu guardarropa!',
            'precio': 12990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000012.jpg'
        },
        {
            'id': 13,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Cartera',
            'descripcion': 'Nuestra cartera es el accesorio perfecto para complementar tu estilo. Con un diseño elegante y espacioso, ofrece funcionalidad y sofisticación. Ideal para llevar tus esenciales diarios con comodidad y clase. ¡Añádelo a tu colección y luce impecable en cualquier ocasión!',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000013.jpg'
        },
        {
            'id': 14,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Chaleco de punto',
            'descripcion': 'Este chaleco de punto con flores añade un toque de encanto y calidez a tu look. Su diseño floral y tejido suave lo hacen perfecto para cualquier temporada. Versátil y elegante, es ideal para combinar con tus prendas favoritas. ¡Incorpora esta pieza única a tu guardarropa!',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000014.jpg'
        },
        {
            'id': 15,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Conjunto de 2 piezas',
            'descripcion': 'Un conjunto elegante y moderno en tonos de verde y azul a cuadros. Incluye una camisa de manga largo medio y pantalones coordinados, ambos con un diseño cómodo y contemporáneo. Perfecto para quienes buscan estilo y versatilidad en su vestimenta diaria.',
            'precio': 21990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000015.jpg'
        },
        {
            'id': 16,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Camisa',
            'descripcion': 'Una camisa de manga corta con estampados inspirados en el kimono japonés. Diseñada para brindar estilo y confort, esta prenda combina patrones tradicionales con un corte moderno y versátil. Ideal para quienes buscan una opción única y sofisticada en su vestimenta diaria.',
            'precio': 9990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000016.jpg'
        },
        {
            'id': 17,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Cartera',
            'descripcion': 'Una cartera elegante y funcional, diseñada para complementar cualquier estilo.',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000017.jpg'
        },
        {
            'id': 18,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Corbata',
            'descripcion': 'Una corbata clásica y sofisticada, perfecta para añadir un toque de estilo a cualquier conjunto.',
            'precio': 5990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000018.jpg'
        },
        {
            'id': 19,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Mocasines',
            'descripcion': 'Mocasines que destacan por su estampado de leopardo, ideales para quienes buscan un estilo audaz y distinguido en calzado.',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000019.jpg'
        },
        {
            'id': 20,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Vestido',
            'descripcion': 'Un vestido elegante y sin tirantes, ideal para ocasiones especiales y eventos formales.',
            'precio': 14990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000020.jpg'
        }
    ]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['25.747.200-0', '11.991.600-3']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Vendido':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Despachado':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

