import os
import re
import json
import csv
# Esta funcion pasa los datos del csv a una lista
def Cargar_csv():
    lista = []
    dic = {}

    with open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Insumos.csv", encoding='utf-8') as file:
        for linea in file:
            lista.append(linea.strip().split(","))
    return lista
#Esta funcion transfomra una lista en un diccionario
def Pasar_a_dict(list:list)->dict:
    lista = []
    for item in list:
        lista.append({'ID':item[0],'nombre':item[1],'marca':item[2],'precio':item[3],'caracteristicas':item[4]})
    return lista
#Esta funcion printeas el diccionario discriminando ciertos elementos
def Mostrar_insumos(lista:list,dicionario:dict, key:str)->None:
    for i in lista:
        for d in dicionario:
            if i == d[key]:
                print(d)
#Esta funcion elimina las repeticiones de una lista
def Sacar_repetidos(List:list)->list:
    conjunto = set(List)
    return conjunto
#Esta funcion aisla la marca que se requirio para asi posteriormente mostrar los productos
def Separar_mostrar_productos(dict:dict,list:set)->None:
    for marca in list:
        print("Marcas :" + marca)
        for producto in dict:
            if(producto['marca'] == marca):
                print(producto['marca'], producto['nombre'])
        print("----------------------------------------------------------")
#Esta funcion muestra los productos y el precio de una marca
def Separara_marca_precio(diccionario:dict,lista:set)->None:
    for marca in lista:
        print("Marcas :" + marca)
        for producto in diccionario:
            if(producto['marca'] == marca):
                print(producto['marca'], producto['nombre'], producto['precio'])
        print("----------------------------------------------------------")
#Esta funcion discrimina un diccionario por los nombres
def Separar_Por_nombres(diccionario:dict,lista:list)->dict:
    listaJson = []
    for Nombre in lista:
        for producto in diccionario:
            
            if Nombre == producto['nombre']:
                listaJson.append({producto['ID'],producto['nombre'],producto['marca'],producto['precio']})
        print("----------------------------------------------------------")
    return listaJson
#Esta funcion agrupa a los elementos de una misma marca en un diccionario
def Separar_marca(dict: dict, key:str)-> list:
    lista = []
    for nombre in dict:
        lista.append(nombre[key])
    conjunto = set(lista)
    return conjunto
#Esta funcion busca parecidos en las caracteristicas y devuelve en una lista los nombres de los elementos con coincidencias
def Buscar_insumo(dict: dict, key:str,key2)->list:
    lista = []
    caracteristica = re.compile(key)
    for item in dict:
        Similitud = caracteristica.search(item[key2])
        if Similitud:
            lista.append(item['nombre'])
        else:
            pass
    return lista
#Esta funcion busca parecidos en las caracteristicas y devuelve en una lista todo el diccionario de los elementos con coincidencias
def Buscar_insumo2(dict: dict, key:str,key2:str)->list:
    lista = []
    caracteristica = re.compile(key)
    for item in dict:
        Similitud = caracteristica.search(item[key2])
        if Similitud:
            lista.append(str({item['ID'],item['nombre'],item['marca'],item['precio'],item['caracteristicas']}))
        else:
            pass
    lista1 = str(lista)
    return lista1
#Esta funcion ordena alfabeticamente un diccionario
def Ordenar_alfabeticamente(dict:dict,lista:list)->list:
    Marca_ordenada = sorted(lista)
    return Marca_ordenada
#Esta funcion Crea un diccionario que ordena ascendentemente los precios
def Crear_diccionario_ordenado(lista:list,dict:dict)->dict:
    diccionario_ordenado = []
    id_anterior = []
    marca_anterior = None
    for marca in lista:
        for id in dict:
            if marca_anterior == id['marca']:
                if precio_anterior > id['precio']:
                    diccionario_ordenado.append(id)
                elif precio_anterior < id['precio']:
                    diccionario_ordenado.append(id_anterior)
            if id['marca'] == marca:
                marca_anterior= id['marca']
                precio_anterior = id['precio']
                id_anterior = id
                diccionario_ordenado.append(id_anterior)
    return diccionario_ordenado
#Esta funcion almacena el valor de los productos seleccionados para devolverlos en una lista
def Comprar_productos(diccionario:dict,key:str)->list:
    lista = []
    for marca in diccionario:
        if marca['marca'] == key:
            print(marca['nombre'],marca['precio'])
    compra = input("Que producto desea comprar")
    for nombre in diccionario:
        if compra == nombre['nombre'] and nombre['marca'] == key:
            print(nombre['nombre'],nombre['precio'])
            lista.append({"nombre" :nombre['nombre'],"precio":nombre['precio']})
    return lista
#Esta funcion suma los precios de una lista
def Sumar_precio(lista:list)->float:
    precio = 0
    for i in list:
        Pagar = float(i['precio'])
        precio+=Pagar
    return precio
#Esta funcion esta funcion pasa una lista a un arrays de strings
def Pasar_a_string(lista:list)->list:
    lista = []
    for palabra in lista:
      lista.append(str(palabra))
    lista_strings = str(lista)
    return lista_strings
#Esta funcion agrega un aumento porcentual al precio del diccionario
def Aumento_precio(diccionario:dict)->dict:
        lista = []
        precio_str = diccionario['precio'].replace("$","")
        precio = float(precio_str)
        precio_aumentado = precio*1.084
        diccionario['precio'] = precio_aumentado

        return diccionario
def menu():
        a = True
        bandera_Cargar_Datos = True
        bandera_json = True
        lista = []
        Comprado = []
        while True:
            a = input("pause")
            seguir = "si"
            os.system("cls")
            print(""" 
            **** Menu de opciones ***
                1-Cargar datos
                2-Listar cantidad de marcas
                3-Limiar insumos por marca
                4-Buscar insumos por caracteristicas
                5-Listar insumos ordenados
                6-Realizar compras
                7-Formar en formato JSON
                8-Leer desde el formato JSON
                9-Actualizar precios
                10- salir del programa
            """)
            Numero = int(input("Ingrese una opcion "))
            match(Numero):
                case 1:
                    lista = Cargar_csv()
                    diccionario = Pasar_a_dict(lista)
                    for i in diccionario:
                        print(i)
                    bandera_Cargar_Datos = False
                case 2:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        conjunto = Separar_marca(diccionario, 'marca')
                        Separar_mostrar_productos(diccionario,conjunto)
                case 3:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        conjunto = Separar_marca(diccionario, 'marca')
                        Separara_marca_precio(diccionario,conjunto)
                case 4:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        carac = input("Ingrese la caracteristica que desee en el producto: ")
                        Lista_caracteristicas_buscada = Buscar_insumo(diccionario,carac,'caracteristicas')
                        Mostrar_insumos(Lista_caracteristicas_buscada,diccionario,'nombre')
                case 5:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        conjunto = Separar_marca(diccionario, 'marca')
                        Alfabetico = Ordenar_alfabeticamente(diccionario,conjunto)
                        Diccionario_ordenado= Crear_diccionario_ordenado(Alfabetico,diccionario)
                        print(Diccionario_ordenado)
                case 6:
                    continuar = True
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        while seguir == "si":
                            compra = input("Ingrese la marca de la cual se quiere comprar podructos: ")
                            Comprado.append( Comprar_productos(diccionario, compra))
                            seguir = input("Desea seguir comprando")
                            print(Comprado)
                        file = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Compra.txt","w",encoding='utf-8')
                        archivo_compra = json.dumps(Comprado)
                        file.write(archivo_compra)
                        file.close
                        file = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Compra.txt","r",encoding='utf-8')
                        for linea in file:
                            print(linea)
                case 7:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        Lista_Json = Buscar_insumo2(diccionario,'Alimento','nombre')
                        JSON = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Archivo.json", "w",encoding='utf-8')
                        for i in Lista_Json:
                            JSON.write(i)
                        #JSON.write(Lista_Json)
                        JSON.close
                        JSON = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Archivo.json", "r",encoding='utf-8')
                        bandera_json = False
                case 8:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    elif bandera_json == True:
                        print("Cargue el documento Json")
                    else:
                        for linea in JSON:
                            print(linea)
                    
                case 9:
                    if bandera_Cargar_Datos == True:
                        print("Cargue los datos Por favor")
                    else:
                        Lista_aumento = list(map(Aumento_precio,diccionario))
                        for elemento in Lista_aumento:
                            print(elemento)
                        #csv_prueba = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Pruebas.csv","w", encoding='utf-8')
                        #csv_prueba.write(Lista_aumento)
                        #csv_prueba.close
                        #csv_prueba = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Pruebas.csv","r")
                        with open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Pruebas.csv", "w", newline="",encoding='utf-8') as archivo_csv:
                            escribir = csv.writer(archivo_csv)
                            escribir.writerow(['ID','nombre','marca','precio','caracteristica'])
                            for i in Lista_aumento:
                                    archivo_csv.write(i['ID'],)
                                    archivo_csv.write(i['nombre'])
                                    archivo_csv.write(i['marca'])
                                    archivo_csv.write(i['marca'])
                                    archivo_csv.write(i['caracteristicas'])
                                    archivo_csv.write("print \n")
                case 10:
                    break







    

