class Factura: 
    def __init__(self, id_factura, cliente, fecha = datetime.now()):
        self.id_factura = id_factura 
        self.cliente = cliente 
        self.fecha = fecha 
        self.detalles = [] 
        self.total = 0 
 
    def agregar_detalle(self, detalle_factura): 
        self.detalles.append(detalle_factura) 
        self.total += detalle_factura.total 
 
    def __str__(self): 
        detalles_str = "\n".join(str(detalle) for detalle in self.detalles) 
        return f'Factura #{self.id_factura} - Cliente: {self.cliente.nombre} - Total: ${self.total}\nDetalles:\n{detalles_str}' 
 