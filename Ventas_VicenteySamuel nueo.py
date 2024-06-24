import os
import pyfiglet 
os.system("cls") 

print(pyfiglet.figlet_format("CONFITES"))
print("                                         Integrantes:Samuel Urzua")
print("                                                     Vicente Osorio")
      
fecha=""
folio=10000

productos=[#   id    producto  tamaño stock precio 
            ["c001","Rocklets","Chico", 150,   900],
            ["c002","Rocklets","Grande",100,   1200],
            ["c003","Skittles","Normal",100,  1100],
            ["c004","Bolsa de Suny","Normal",100,1200],
            ["c005","Bolsa de Bon o Bon","Normal",150,1000],
            ["c006","Tifany's","Chico",150,300],
            ["c007","Tifany's","Grande",100,990],
            ["c008","Chubi","Chico",150,300],
            ["c009","Chubi","Grande",100,1000],
            ["c010","Gomitas Menthol","Chica",150,600]
] 

ventas= [#     folio     fecha      id     cantidad  total
            ["10001","10-05-2024","c001",60,54000],
            ["10002","30-05-2024","c004",50,60000],
            ["10003","25-06-2024","c006",55,16500],
            ["10004","27-06-2024","c003",25,27500],
            ["10005","28-06-2024","c005",30,36000],
            ["10006","28-06-2024","c006",35,10500],
            ["10007","28-06-2024","c007",35,34650],
            ["10008","29-06-2024","c008",40,12000],
            ["10009","29-06-2024","c009",50,50000],
            ["10010","30-06-2024","c010",45,27000],
            ["10011","30-07-2024","c002",35,42000],
            ["10012","31-07-2024","c001",50,45000],
            ["10013","01-07-2024","c003",50,55000],
            ["10014","02-07-2024","c004",40,48000],
            ["10015","03-07-2024","c007",50,49500], 
            ["10016","04-07-2024","c008",50,15000],
            ["10017","05-07-2024","c010",50,30000],
            ["10018","06-07-2024","c006",50,15000],
            ["10019","07-07-2024","c009",45,45000],
            ["10020","08-07-2024","c005",50,50000],
]
id=""
op=0 

def get_folio():
    elemento=len(ventas)-1
    return (ventas[elemento])[0]
    
    
def buscar_id(id):   
    p=0 

    for p in productos:
        if p[0] == id:           
           return p
    return -1   

while op<=4: 

    print("Ultimo folio: ",get_folio()) 

    print("""
                 --------------------------------
                         Sistema de ventas
       1.Vender productos
       2.Reportes.
       3.Mantenedores
       4.Administracion
       5.Salir                                                                   
          
          """ ) 
    
    op=int(input("Ingrese una opcion entre 1-4: "))
    match op:
            case 1:
                while True:
                    respuesta= "s"
                    os.system("cls")
                    print("          VENDER PRODUCTO                  \n")
                    #mostrar lista de productos #
                    producto=buscar_id(input("ingrese ID:"))
                    #print("encontrado en el elemento ",i)
                    print(producto[0]," ",producto[1]," ",producto[2]," ",producto[3]," ",producto[4])
                    cantidad=int(input("ingrese cantidad a comprar: "))
                    stock = producto[3]
                    valor = cantidad*producto[4]
                    producto[3]-=cantidad
                    if respuesta.lower() == "s":
                        if cantidad <= stock:
                            print(f"el valor de esta comprar por {cantidad} productos es de: {valor}")
                            respuesta = input("desea otra compra? [s]/[n]: ")
                            if respuesta.lower() == "n":
                                break
                        else:
                            print("error el stock no es suficiente")
                    else:
                            break    


                   

                
                                              
            case 2: 
                os.system("cls")
                op=0 
                while op<=4:
                    print("""
                                REPORTES
                    -------------------------------------
                    1.General de ventas (con total)
                    2-Ventas por fecha especifica (con total)
                    3.Ventas por rango de fecha (con total)
                    4.Salir al menu principal
                                    
                        """)      
                    op=int(input("ingrese una opcion entre 1-4: "))
                    
                    match op:
                        case 1:
                            
                            print("Ventas")
                            i=0
                            for venta in ventas:
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3])  
                                i = i + venta[3]
                                print("Total=",i)

                        case 2:
                            fecha=input("Ingrese la fecha de venta (dd-mm-aa)")
                            i=0

                            for venta in ventas:
                                if venta[1] == fecha:
                                    print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3])
                                    print("Fecha de venta") 
                                    i=i+venta[3] 
                                print("total= ",i)
                                    
                            
                    
                            
                        case 3:
                            fechain=(input("Ingrese la fecha de inicio (dd-mm-aaaa)"))
                            fechate=(input("Ingrese la fecha de termino (dd-mm-aaaa)"))

                            total=0
                    
                            for venta in ventas:
                                fecha_venta= venta[0]
                                
                                if fechain <= fecha_venta and fecha_venta <=fechate:
                                    print(venta[0]," ",venta[1]," ",venta[2],"",venta[3])
                                    total = total + venta[4]
                                    
                                    
    
            case 3:
                op=0
                while op <=6:
                    print("""
                        MANTENEDOR DE PRODUCTOS
                        1.Agregar
                        2.Buscar
                        3.Eliminar
                        4.Modificar
                        5.Listar
                        6.Salir al menu principal
                        
                        """)
                    op=int(input("Ingrese una opcion entre 1-6: "))

                    match op:
                        case 1:
                            print("\nAgregar\n")
                            id = input("Ingrese su id: ")
                            producto= input("Ingrese su nombre de producto: ")
                            tamaño =(input("Ingrese tamaño del producto: "))
                            stock = int(input("Ingrese stock del producto: "))
                            precio = int(input("Ingrese precio del producto: "))

                            productos.append([id,producto,tamaño,stock,precio])


                            print(productos)

                        case 2:
                            print("\n-------------------------------------------\n") 
                            id=input("Ingrese el id a buscar: ")
                            sw=0 #no existe
                            for p in productos:
                                if p [0]== id:
                                    sw=1 #existe, encontrado
                                    print(p[0]," ",p[1]," ",p[2]," ",p[3]," ",p[4])
                                    break 

                            if sw==0:
                                print("Error,id no existe")
                        case 3:
                            id=input("Ingrese id a buscar: ")
                            lista=buscar_id(id)

                            if lista != -1:
                                productos.remove(lista)
                                print(productos)
                            else:
                                print("Error, id no existe")

                        case 4:
                            id=input("Ingrese id a buscar: ")
                            nuevo_producto=(input("Ingrese el nuevo producto: "))
                            nuevo_tamaño=(input("Ingrese el nuevo tamaño: "))
                            nuevo_stock= int(input("Ingrese el nuevo stock: "))
                            nuevo_precio= int(input("Ingrese el nuevo precio: "))

                            lista=buscar_id(id)

                            if lista != -1:
                                lista[1]=nuevo_producto
                                lista[2]=nuevo_tamaño
                                lista[3]=nuevo_stock
                                lista[4]=nuevo_precio #actualizar/ modificar
                                print(productos)
                            else:
                                print("Error, id no existe")

                        case 5:
                            for p in productos:
                                print(p[0]," ",p[1]," ",p[2]," ",p[3]," ",p[4])
                            
                    if op==6:
                        break 
                    os.system("pause")
                else:
                    print("Error, debe ingresar un valor entre 1 y 6")
                    os.system("pause")
                print("Fin del menu") 
            case 4:
              break 
os.system("pause")
 
