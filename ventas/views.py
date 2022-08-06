from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTES',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)



def compra(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "compras/compras.html",data)

def proveedor(request):
  data = {
      'titulo':'GESTION DE PROVEEDORES',
      'crear_url': '/crearproveedor',
      'listar_url': '/proveedor',
  }
  return render(request, "compras/proveedores/listProveedor.html",data)

def crearProveedor(request):
  data = {
      'titulo':'MANTENIMIENTO DE PROVEEDORES',
      'crear_url':'/crearproveedor',
      'action':'add',
      'listar_url': '/proveedor',
  }
  return render(request, "compras/proveedores/formProveedor.html",data)

def producto(request):
  data = {
      'titulo':'GESTION DE PRODUCTOS',
      'crear_url': '/crearproducto',
      'listar_url': '/producto',
  }
  return render(request, "compras/productos/listProducto.html",data)

def crearProducto(request):
  data = {
      'titulo':'MANTENIMIENTO DE PRODUCTOS',
      'crear_url':'/crearproducto',
      'action':'add',
      'listar_url': '/proveedor',
  }
  return render(request, "compras/productos/formProducto.html",data)

def categoria(request):
  data = {
      'titulo':'GESTION DE CATEGORIAS',
      'crear_url': '/crearcategoria',
      'listar_url': '/categoria',
  }
  return render(request, "compras/categoria/listCategoria.html",data)

def crearCategoria(request):
  data = {
      'titulo':'MANTENIMIENTO DE CATEGORIAS',
      'crear_url':'/crearcategoria',
      'action':'add',
      'listar_url': '/categoria',
  }
  return render(request, "compras/categoria/formCategoria.html",data)

def factura(request):
  data = {
      'titulo':'GESTION DE FACTURAS',
      'crear_url': '/crearfactura',
      'listar_url': '/factura',
  }
  return render(request, "compras/factura/listFactura.html",data)

def crearFactura(request):
  data = {
      'titulo':'MANTENIMIENTO DE FACTURAS',
      'crear_url':'/crearfactura',
      'action':'add',
      'listar_url': '/factura',
  }
  return render(request, "compras/factura/formFactura.html",data)