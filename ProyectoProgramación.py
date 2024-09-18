import os
import shutil
from datetime import datetime

#Definicion de funciones
def crear_o_existente(Suborden3):
    if Suborden3 == 2:
        Dir_destino= input("Ingrese el directorio en el cual va a copiar los archivos")

        if not os.path.exists(Dir_destino):
                os.makedirs(Dir_destino)

        NDT= Dir_destino
        
    elif Suborden3 == 1:
        nombre_nueva_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
    
        # Define la ruta del nuevo directorio
        NDT = os.path.join(os.getcwd(), nombre_nueva_carpeta)
    
        # Crear el nuevo directorio si no existe
        if not os.path.exists(NDT):
            os.mkdir(NDT)
            print(f"Carpeta '{NDT}' creada exitosamente.")
        else:
            print(f"La carpeta '{NDT}' ya existe.")
    
        # Verificar que NDT está definido correctamente
            if NDT is None:
                print("Error: NDT es None")
            else:
                print(f"NDT está definido: {NDT}")
    return NDT
            
def copia_por_tipo_archivos(DDT):
    TA= input("Escriba el tipo de archivo del cual desea copiar los archivos")
    
    NDT = crear_o_existente(Suborden3)    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            if file.endswith(TA):
                try:
                    path = os.path.join(root, file)
                    shutil.copy(path, NDT)
                    print(f"Archivo '{file}' copiado a '{NDT}'")

                except shutil.SameFileError:
                             
                    print(f"Error: El archivo '{file}' no se copió porque es el mismo archivo.")

                except Exception as e:

                    print(f"Error al copiar el archivo '{file}': {e}")
                    
def copia_por_peso(DDT):
    
    Suborden4= input("""Desea que se copien los archivos con:
                        1.Tamaño menor o igual al designado.
                        2.Tamaño igual al designado.
                        3.Tamaño mayor o igual al designado.\n""")
        
    TD=input("Designe el tamaño (en MB y sin usar unidades, ejemplo: 10)\n")
    
    NDT = crear_o_existente(Suborden3) 
    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            if Suborden4 == "1":
                file_path = os.path.join(root, file)
                tamaño = os.stat(file_path).st_size

                # Convertir el tamaño deseado a bytes
                tamaño_deseado = float(TD) * 1000000

                if tamaño <= tamaño_deseado:
                    
                    copia(NDT, file_path, file)

            elif Suborden4 == "2":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    # Convertir el tamaño deseado a bytes
                    tamaño_deseado = float(TD) * 1000000

                    if tamaño == tamaño_deseado:
                        
                        copia(NDT, file_path, file)

            elif Suborden4 == "3":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    tamaño_deseado = float(TD) * 1000000

                    if tamaño >= tamaño_deseado:
                        
                        copia(NDT, file_path, file)

def copia_por_fecha(DDT):   
    
    NDT = crear_o_existente(Suborden3)  
      
    fecha_input= input("Ingrese la fecha límite en formato YYYY-MM-DD: ")

    try:
        fecha_limite= datetime.strptime(fecha_input, '%Y-%m-%d')

    except ValueError:
        print("El formato de fecha no es válido. Asegúrese de usar YYYY-MM-DD.")
        exit()
        
    Suborden4 = input("""Desea que se copien los archivos con:
                        1.Fechas antes o igual a la fecha designada.
                        2.Fecha igual a la designada.
                        3.Fechas despues o igual\n""")
        
    for root, subdirs, files in os.walk(DDT):
                for file in files:
                    file_path = os.path.join(root, file)

                    mod_time = os.stat(file_path).st_mtime
                    mod_time_formatted = datetime.fromtimestamp(mod_time)

                    
        
                    if Suborden4 == "1" and mod_time_formatted < fecha_limite:

                        copia(NDT, file_path, file)
                        
                    elif Suborden4 == "2" and mod_time_formatted == fecha_limite:
                        
                        copia(NDT, file_path, file)
                
                    elif Suborden4 == "3" and mod_time_formatted >= fecha_limite:
                        
                        copia(NDT, file_path, file)

def eliminar_por_tipo(DDT):
   
    TA= input("Escriba el tipo de archivo del cual desea eliminar")
    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            # Comprueba si el archivo termina con el tipo especificado
            if file.endswith(TA):
                try:
                    path = os.path.join(root, file)  # Ruta completa del archivo
                    os.remove(path)  # Elimina el archivo
                    print(f"Archivo '{file}' eliminado de '{root}'")

                except FileNotFoundError:
                    print(f"Error: El archivo '{file}' no se encontró.")

                except Exception as e:
                    print(f"Error al eliminar el archivo '{file}': {e}")
                    
def eliminar_por_peso(DDT):
    Suborden4= input("""Desea que se eliminen los archivos con:
                        1.Tamaño menor o igual al designado.
                        2.Tamaño igual al designado.
                        3.Tamaño mayor o igual al designado.\n""")
        
    TD=input("Designe el tamaño (en MB y sin usar unidades, ejemplo: 10)\n")
    
     
    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            if Suborden4 == "1":
                file_path = os.path.join(root, file)
                tamaño = os.stat(file_path).st_size

                # Convertir el tamaño deseado a bytes
                tamaño_deseado = float(TD) * 1000000

                if tamaño <= tamaño_deseado:
                    
                    eliminar(file, file_path)

            elif Suborden4 == "2":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    # Convertir el tamaño deseado a bytes
                    tamaño_deseado = float(TD) * 1000000

                    if tamaño == tamaño_deseado:
                        
                        eliminar(file, file_path)

            elif Suborden4 == "3":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    tamaño_deseado = float(TD) * 1000000

                    if tamaño >= tamaño_deseado:
                        
                        eliminar(file, file_path)
                        
def eliminar_por_fecha(DDT):
    
     
      
    fecha_input= input("Ingrese la fecha límite en formato YYYY-MM-DD: ")

    try:
        fecha_limite= datetime.strptime(fecha_input, '%Y-%m-%d').date()

    except ValueError:
        print("El formato de fecha no es válido. Asegúrese de usar YYYY-MM-DD.")
        exit()
        
    Suborden4 = input("""Desea que se eliminen los archivos con:
                        1.Fechas antes o igual a la fecha designada.
                        2.Fecha igual a la designada.
                        3.Fechas despues o igual\n""")
    
    print(f"Orden: {Suborden4}")
    DDT = os.getcwd()    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            file_path = os.path.join(root, file)
            
            
            if not os.path.exists(file_path):
                print(f"El archivo '{file}' no existe. Saltando...")
                continue

            
            mod_time = os.stat(file_path).st_mtime
            mod_time_formatted = datetime.fromtimestamp(mod_time).date()  # Convertir a fecha
            
            
            print(f"\nEvaluando archivo: {file_path}")
            print(f"Fecha de modificación del archivo: {mod_time_formatted}")
            print(f"Comparando con fecha límite: {fecha_limite}")

            
            if Suborden4 == "1" and mod_time_formatted <= fecha_limite:
                print(f"Eliminando archivo '{file}' (modificación antes o igual a {fecha_limite})")
                eliminar(file, file_path)
            elif Suborden4 == "2" and mod_time_formatted == fecha_limite:
                print(f"Eliminando archivo '{file}' (modificación igual a {fecha_limite})")
                eliminar(file, file_path)
            elif Suborden4 == "3" and mod_time_formatted >= fecha_limite:
                print(f"Eliminando archivo '{file}' (modificación después o igual a {fecha_limite})")
                eliminar(file, file_path)
            else:
                print(f"Archivo '{file}' no cumple las condiciones de eliminación.")
 
def mover_por_tipo(DDT):
    
    TA= input("Escriba el tipo de archivo del cual desea mover los archivos")
    
    NDT = crear_o_existente(Suborden3)    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            if file.endswith(TA):
                try:
                    path = os.path.join(root, file)
                    shutil.move(path, NDT)
                    print(f"Archivo '{file}' movido a '{NDT}'")

                except shutil.SameFileError:
                             
                    print(f"Error: El archivo '{file}' no se movió porque es el mismo archivo.")

                except Exception as e:

                    print(f"Error al mover el archivo '{file}': {e}")

def mover_por_peso(DDT):
    
    Suborden4= input("""Desea que se eliminen los archivos con:
                        1.Tamaño menor o igual al designado.
                        2.Tamaño igual al designado.
                        3.Tamaño mayor o igual al designado.\n""")
        
    TD=input("Designe el tamaño (en MB y sin usar unidades, ejemplo: 10)\n")
    
    NDT = crear_o_existente(Suborden3) 
    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            if Suborden4 == "1":
                file_path = os.path.join(root, file)
                tamaño = os.stat(file_path).st_size

                # Convertir el tamaño deseado a bytes
                tamaño_deseado = float(TD) * 1000000

                if tamaño <= tamaño_deseado:
                    
                    mover(NDT, file_path, file)

            elif Suborden4 == "2":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    # Convertir el tamaño deseado a bytes
                    tamaño_deseado = float(TD) * 1000000

                    if tamaño == tamaño_deseado:
                        
                        mover(NDT, file_path, file)

            elif Suborden4 == "3":
                    file_path = os.path.join(root, file)
                    tamaño = os.stat(file_path).st_size

                    tamaño_deseado = float(TD) * 1000000

                    if tamaño >= tamaño_deseado:
                        
                        mover(NDT, file_path, file)

def mover_por_fecha(DDT):
    
    NDT = crear_o_existente(Suborden3)  
      
    fecha_input= input("Ingrese la fecha límite en formato YYYY-MM-DD: ")

    try:
        fecha_limite= datetime.strptime(fecha_input, '%Y-%m-%d').date()

    except ValueError:
        print("El formato de fecha no es válido. Asegúrese de usar YYYY-MM-DD.")
        exit()
        
    Suborden4 = input("""Desea que se muevan los archivos con:
                        1.Fechas antes o igual a la fecha designada.
                        2.Fecha igual a la designada.
                        3.Fechas despues o igual\n""")
    if not os.path.exists(NDT):
        print(f"El directorio '{NDT}' no existe.")
        exit()
       
    
    for root, subdirs, files in os.walk(DDT):
        for file in files:
            file_path = os.path.join(root, file)

            if not os.path.exists(file_path):
                print(f"El archivo '{file}' no existe. Saltando...")
                continue
            
            mod_time = os.stat(file_path).st_mtime
            mod_time_formatted = datetime.fromtimestamp(mod_time).date()

            print(f"\nEvaluando archivo: {file_path}")
            print(f"Fecha de modificación del archivo: {mod_time_formatted}")
            print(f"Comparando con fecha límite: {fecha_limite}")        
        
            if Suborden4 == "1" and mod_time_formatted < fecha_limite:
                print(f"Moviendo archivo '{file}' (modificación antes o igual a {fecha_limite})")
                mover(NDT, file_path, file)
                        
            elif Suborden4 == "2" and mod_time_formatted == fecha_limite:
                print(f"Moviendo archivo '{file}' (modificación igual a {fecha_limite})")        
                mover(NDT, file_path, file)
                
            elif Suborden4 == "3" and mod_time_formatted >= fecha_limite:
                print(f"Moviendo archivo '{file}' (modificación después o igual a {fecha_limite})")        
                mover(NDT, file_path, file)
            else:
                print(f"Archivo '{file}' no cumple las condiciones para ser movido.")
                       
def copia(NDT, file_path, file):
        try:
            shutil.copy(file_path, NDT)
            print(f"Archivo '{file}' copiado a '{NDT}'")
        except shutil.SameFileError:
            print(f"Error: El archivo '{file}' no se copió porque es el mismo archivo.")
        except Exception as e:
            print(f"Error al copiar el archivo '{file}': {e}")
            
def eliminar(file, file_path):
    try:
        os.remove(file_path)  # Eliminar el archivo en lugar de copiarlo
        print(f"Archivo '{file}' eliminado de '{file_path}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{file}' no se encontró.")
    except Exception as e:
        print(f"Error al eliminar el archivo '{file}': {e}")
        
def mover(NDT, file_path, file):
    try:
        shutil.move(file_path, NDT)  # Mover el archivo al nuevo directorio
        print(f"Archivo '{file}' movido a '{NDT}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{file}' no se encontró en la ruta '{file_path}'.")
    except Exception as e:
        print(f"Error al mover el archivo '{file}': {e}")   
 
           
#Tomar directorio
DDT = os.getcwd()
print(DDT)

DDT = input("Ingrese el directorio de trabajo")
existe = os.path.exists(DDT)

if existe == True:
    os.chdir(DDT)
else:
    print("Carpeta no encontrada")

print("Directorio cambiado a:",DDT ,sep= " ")

print("Estado actual del directorio:", os.listdir() )   

#Empezar con el trabajo

#Mover copiar, mover o eliminar
while True:
           
        while True:
            try:
                # Solicitar la entrada del usuario
                orden = int(input("""¿Qué desea realizar con sus archivos? (Marque el número de la función que desea usar)
                    1. Copiar archivos
                    2. Mover archivos
                    3. Eliminar archivos
                    4. Salir (Escoja cualquiera de las siguientes opciones)\n"""))
                
                
                if orden not in [1, 2, 3, 4]:
                    print("Opción no válida. Intente de nuevo.")
                elif orden == 4:
                    print("Saliendo...")
                    exit() 
                else:
                    print(f"Has seleccionado la opción {orden}.")
                    break

            
            except ValueError:
                print("Por favor, ingrese un número válido (1-4).")

            break
        #Peso,tipo o fecha

        while True:
            
            try:
                
                Suborden2= int(input("""Desea:
                                1.Trabajar por tipo de archivo.
                                2.Trabajar por el peso del archivo
                                3.Trabajar por la fecha del archivo"""))    
                
                
                if Suborden2 not in [1, 2, 3]:
                    print("Opción no válida. Intente de nuevo.")
                     
                
                else:

                    print(f"Has seleccionado la opción {Suborden2}.")
                    break
            except ValueError:
                print("Por favor, ingrese un número válido (1-3).")
                
            break
        
        while True:
            try:    
                Suborden3= int(input("""Desea:
                            1.Crear una carpeta nueva con los archivos.
                            2.Copiar archivos a carpeta existente.
                            3.Si eligio eliminar, escoja esta opcion.\n"""))
                
                if Suborden3 not in [1, 2, 3]:
                    print("Opción no válida. Intente de nuevo.")
                    
                
                else:
                    print(f"Has seleccionado la opción {Suborden3}.")
                    break
            except ValueError:
                print("Por favor, ingrese un número válido (1-3).")

        #Empieza a modificar archivos
        
        if orden == 1:
            if Suborden2 == 1:
                copia_por_tipo_archivos(DDT)
            elif Suborden2 == 2:
                copia_por_peso(DDT)
            elif Suborden2 ==3:
                copia_por_fecha(DDT)
        elif orden == 2:
            if Suborden2 == 1:
                mover_por_tipo(DDT)
            elif Suborden2 == 2:
                mover_por_peso(DDT)
            elif Suborden2 ==3:
                mover_por_fecha(DDT)
                
        elif orden == 3:
            if Suborden2 == 1:
                eliminar_por_tipo(DDT)
            elif Suborden2 == 2:
                eliminar_por_peso(DDT)
            elif Suborden2 ==3:
                eliminar_por_fecha(DDT)
                
        elif orden == 4:
            
            print("Saliendo del programa")
            break #Cierre
                        
                    # Preguntar si quiere volver al menú
        repetir = input("¿Deseas volver al menú? s o n: ").lower()

        if repetir != 's':
            print("Saliendo del programa.")
            break  