from collections import namedtuple
import csv
import os
switch = True
diccionario = {}
ventas = namedtuple('ventas', 'desc_articulo, cantidad, precio, fecha, total ')
while True:
    print('')
    print(' ** MENU ** ')
    print('Registrar una venta[1]')
    print('Consultar una venta[2]')
    print('Salir[3]')
    op = input('Introduzca la opcion: ')
    if op == '1':
        while True:
            folio = input('Introduzca folio: ')
            if folio in diccionario:
                print('Ese folio ya esta registrado, intente con otro')
            else: 
                fecha = input('Introduzca fecha de la venta d/m/y: ')
                desc_articulo = input('Describa el articulo: ')
                cantidad = int(input('Cantidad de piezas vendidas: '))
                precio = float(input('Precio de venta: '))
                datos = ventas(desc_articulo,cantidad,precio)
                diccionario[folio] = datos
                total = precio * cantidad
                print(f'Precio total a pagar ${total}')
                iva = total * .16
                print(f'Total del iva aplicable a la venta: {iva} ')
                agregar = input('Desea seguir agregando[S/N]: ')
                if agregar == 'N':
                   with open('ventas.csv','w',newline='') as archivo:
                    grabador = csv.writer(archivo)
                    grabador.writerow(('folio','desc_articulo','cantidad','precio'))
                    grabador.writerows([(folio, datos.desc_articulo, datos.cantidad, datos.precio) for folio, datos in diccionario.items()])
                    print(f'\ngrabado exitoso en {os.getcwd()}')
                    break
    elif op == '2':
        busqueda = input('Introduzca el folio a buscar: ')
        if busqueda in diccionario.keys():
           print(f'Descripcion del articulo: {diccionario[busqueda].desc_articulo}' )
           print(f'Cantidad vendida: {diccionario[busqueda].cantidad} ')
           print(f'Precio de venta: {diccionario[busqueda].precio} ')
           print(f'Fecha de la venta: {diccionario[busqueda].fecha}')
           print(f'Precio total con iva: {diccionario[busqueda].total}')
           print("")
        else:
            print('')
            print(' ** NO ESTA **')
            print('')
    elif op == '3':
        break
