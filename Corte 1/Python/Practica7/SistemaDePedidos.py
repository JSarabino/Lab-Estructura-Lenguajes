from Producto import Producto
from Pedido import Pedido
from Cliente import Cliente
from Pago import Pago
from Estatus import Estatus
from enum import Enum
from DetallePedido import DetallePedido
from Efectivo import Efectivo
from Cheque import Cheque
from datetime import datetime

import sys

class SistemaDePedidos:

    #Atributos
    clientes = []
    productos = []
    pedidos = []

    #Otros metodos

    def addProductos(self):
        
        #Pedir datos
        idProducto = int(input("\nIngrese el id del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        #Crear objeto
        objProducto = Producto(idProducto,nombre,marca,precio,cantidad)

        #Agregar a la lista
        self.productos.append(objProducto)


    def addClientes(self):
        #Pedir datos

        ident = int(input("\nIngrese la identificacion: "))
        nombreCompleto = input("Ingrese el nombre completo: ")
        direccion = input("Ingrese la direccion: ")

        #Crear objeto
        objCliente = Cliente(ident,nombreCompleto,direccion)

        #Agregar a la lista
        self.clientes.append(objCliente)

    def crearPedidos(self):
        #Cliente
        cliente = None
        idCliente = int(input("Ingrese el id del cliente: "))
        for i in range(len(self.clientes)):
            if (self.clientes[i].get_Identificacion() == idCliente):
                cliente = self.clientes[i]
                break
        
        if cliente != None:
            #POST: el cliente existe
            #Pedido
            idPedido = int(input("\nIngrese el id del pedido: "))
            fechaPedido = datetime.now()
            montoTotal = 0
            montoPagado = 0
            estatus = Estatus.noPagado
            pedido = Pedido(idPedido,fechaPedido,montoTotal,montoPagado,estatus,cliente.get_Identificacion())

            #Detalles
            cantidadDetalles = int(input("\nDigite la cantidad de productos a pedir: ")) #Numero de detalles o productos a registrar
            for i in range(cantidadDetalles):

                producto = None
                idProducto = int(input("Ingrese el id del producto " + str(i+1) + ": "))
                for j in range(len(self.productos)):
                    if (self.productos[j].get_IdProducto() == idProducto):
                        producto = self.productos[j]
                        break

                if producto != None:
                    #POST: encontro el producto a registrar
                    cantidadProducto = producto.get_Cantidad() # Validar cantidad
                    while True:
                        print("Cantidad del producto disponible: ", cantidadProducto)
                        cantidadDetalle = int(input("Ingrese la cantidad a pedir del producto: "))
                        if cantidadDetalle <= cantidadProducto:
                            break

                    #Crear detalle
                    detalle = DetallePedido(cantidadDetalle,pedido,producto)

                    #Agregar detalle al pedido
                    pedido.set_Detalles(detalle)

                    #Actualizar monto total
                    pedido.set_MontoTotal(pedido.get_MontoTotal() + detalle.get_montoDetalle())

                    #Actualizar las cantidades
                    producto.set_Cantidad(cantidadProducto-cantidadDetalle)

                    #Agregar pedido a la lista del sistema
                    self.pedidos.append(pedido)
                else:
                    print("\Producto no encontrado.")

            #Agregar pedido al cliente
            cliente.set_Pedidos(pedido)
        else:
            print("\nCliente no encontrado.")

    def mostrarPedidosCliente(self, ident):
        cliente = None

        for i in range(len(self.clientes)):
            if (self.clientes[i].get_Identificacion() == ident):
                cliente = self.clientes[i]
                break
        
        #Datos de los pedidos
        if cliente != None:
            print("Pedidos del cliente: ", len(cliente.get_Pedidos()))
            for i in cliente.get_Pedidos():
                print(i.mostrarPedido())
        else:
            print("\nCliente no encontrado.")

    def realizarPago(self, idPedido, tipoPago, monto):
        pedido = None
        for i in range(len(self.pedidos)):
            if (self.pedidos[i].get_IdPedido() == idPedido):
                pedido = self.pedidos[i]
                break
        
        if pedido != None:
            if pedido.get_Estatus() != Estatus.pagado:
                idPago = int(input("Ingrese el id del pago: "))
    
                #Tipo de pago
                pago = None
                if tipoPago == 1:
                    pago = Efectivo(idPago,monto,pedido.get_IdPedido())
                else: 
                    entidad = input("Ingrese la entidad: ")
                    titular = input("Ingrese el titular: ")
                    chequeNro = input("Ingrese el chequeNro: ")
                    pago = Cheque(idPago, monto,pedido.get_IdPedido(),entidad,titular,chequeNro)
                
                #Cuanto a pagado antes del pedido
                totalPedido = pedido.get_MontoTotal()
                pagado = pedido.get_MontoPagado()
                debe = totalPedido - pagado

                #Si el monto es mayor o igual a lo que debe
                if monto >= debe:
                    pedido.set_Estatus(Estatus.pagado)
                else:
                    pedido.set_Estatus(Estatus.abonado)
                
                pedido.set_Pagos(pago)
                #Actualizar el monto pagado
                pedido.set_MontoPagado(pedido.get_MontoPagado() + monto)

            else:
                print("\nPedido ya pagado.")
        else:
            print("\nPedido no encontrado.")

    def mostrarPedidoEstatus(self, estatus):
        # 1 es para pagados, 2 para no pagados y 3 para abonados

        if estatus == 1:
            print("\nPedidos pagados.")
            for p in self.pedidos:
                if p.get_Estatus() == Estatus.pagado:
                    p.mostrarPedido()
        elif estatus == 2:
            print("\nPedidos NO pagados.")
            for nP in self.pedidos:
                if nP.get_Estatus() == Estatus.noPagado:
                    nP.mostrarPedido()
        elif estatus == 3:
            print("\nPedidos abonados.")
            for a in self.pedidos:
                if a.get_Estatus() == Estatus.abonado:
                    a.mostrarPedido()
        else:
            print("Error!. El tipo de estatus no existe.")

#-----Menu------
# Elegir opcion del menu principal
def opMenuPrincipal():
    obj = SistemaDePedidos()
    while True:
        print("\nMenu Principal.")
        print("1. Agregar producto. \n2. Agregar cliente. \n3. Crear pedido. \n4. Mostrar pedidos de cliente. \n5. Realizar pago. \n6. Mostrar pedidos por estatus. \n7. Salir")
        op = int(input("\nDigite la opcion a realizar: "))
        if op > 0 and op < 9:
            menuPrincipal(op,obj)

# Menu Principal
def menuPrincipal(op,obj):
    match op:
        case 1: obj.addProductos()   
        case 2: obj.addClientes() 
        case 3: obj.crearPedidos()
        case 4: 
            ident = int(input("\nIngrese el id del cliente: "))
            obj.mostrarPedidosCliente(ident)
        case 5: 
            idPedido = int(input("\nIngrese el id del pedido: "))
            tipoPago = int(input("Ingrese el tipo de pago (1. efectivo / 2.Cheque): "))
            monto = float(input("Ingrese el monto: "))
            obj.realizarPago(idPedido,tipoPago,monto)
        case 6: 
            estatus = int(input("1. Para pagados / 2. Para no pagados / 3. para abonados "))
            obj.mostrarPedidoEstatus(estatus)
        case 7: salir()

# Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)

if __name__ == '__main__':
    opMenuPrincipal()
