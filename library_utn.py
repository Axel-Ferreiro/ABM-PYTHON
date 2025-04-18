
import os
from validaciones import *
import json
from turno import *



def clear_console():
    """
    The function `clear_console` prompts the user to press Enter to continue and then clears the console
    screen based on the operating system.
    """
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    

def UTN_messenger(message: str, message_type: str = None, new_line: bool = False) -> None:
    """
    This is a Python function that prints a message with a specific color and message type.
    
    :param message: The message that needs to be displayed in the console
    :param message_type: The type of message being passed, which can be 'Error', 'Success', 'Info',
    or None. If None, the message will be printed without any formatting
    """
    _b_red: str = '\033[41m'
    _b_green: str = '\033[42m'
    _b_blue: str = '\033[44m'
    _f_white: str = '\033[37m'
    _no_color: str = '\033[0m'
    message_type = message_type.strip().capitalize()
    new_line_char = '\n'
    final_message = f'{new_line_char if new_line else ""}'
    match message_type:
        case 'Error':
            final_message += f'{_b_red}{_f_white}> Error: {message}{_no_color}'
        case 'Success':
            final_message += f'{_b_green}{_f_white}> Success: {message}{_no_color}'
        case 'Info':
            final_message += f'{_b_blue}{_f_white}> Information: {message}{_no_color}'
        case _:
            final_message += message
    print(final_message)

def mostar_menu():
    print("Bienvenidos al menu.\n1. Alta paciente.\n2. Alta turno.\n3. Ordenar turnos.\n4. Mostrar pacientes en espera.\n5. Atender pacientes.\n6. Cobrar atenciones.\n7. Cerrar caja.\n8. Mostrar informe\n9. Mostrar pacientes.\n10. Mostrar turnos.\n11. Salir")

def encontrar_id_maximo(lista) -> int:
    """
    La función `encontrar_id_maximo` encuentra el ID máximo en una lista de diccionarios y devuelve uno
    mayor que ese ID máximo.

    :param lista: La función `encontrar_id_maximo` toma una lista de diccionarios como entrada. Cada
    diccionario de la lista representa un proyecto y contiene una clave "id" con un valor numérico. La
    función recorre la lista para encontrar el valor máximo de "id" entre todos los proyectos y devuelve
    el máximo
    :return: La función `encontrar_id_maximo` devuelve el valor máximo de la clave "id" en la lista de
    diccionarios `lista`, incrementado en 1.
    """
    bandera = True
    if lista:
        for proyecto in lista:
            numero = proyecto["id"]
            if bandera == True:
                maximo = proyecto["id"]
                bandera = False

            if maximo < numero:
                maximo = numero

        return maximo + 1
    else:
        return 1

def alta_paciente(lista_pacientes: list,clinica: object):
    """
    Funcion para cargar los datos de un paciente
    retorna una clase de paciente
    """

    mostrar_pacientes_tabla(lista_pacientes)
    while True:
        id = encontrar_id_maximo(lista_pacientes)
        nombre = validar_nombre()
        apellido = validar_apellido()
        dni = validar_dni()
        dni_2 = False
        for paciente in lista_pacientes:
            if paciente["dni"] == dni:
                print("no se puede cargar un paciente con mismo dni")
                dni_2 = True
                break
        if dni_2:
            break
        edad = validar_edad()
        fecha_de_registro = ingresar_fecha_de_registro()
        obra_social = validar_obra_social(edad).capitalize()
        

        clinica.cargar_paciente(id,nombre,apellido,dni,edad,fecha_de_registro,obra_social,lista_pacientes)
        break

def alta_turno(lista_pacientes: list,lista_turnos : list ,clinica: object):
    """
    Funcion para cargar los datos de un turno y crear una clase
    retorna una clase de turno
    """
    while True:
        mostrar_pacientes_tabla(lista_pacientes)
        id_a_buscar = validar_numero("Ingrese id del paciente para asignar un turno: ")
        diccionario = buscar_proyecto_por_id(lista_pacientes,id_a_buscar)
        if not mostrar_paciente_tabla(diccionario):
            break
        id = encontrar_id_maximo(lista_turnos)
        id_paciente = id_a_buscar
        especialidad = validar_especialidad()
        monto_a_pagar = calcular_monto_a_pagar(diccionario)
        estado_turno = "Activo"
        clinica.alta_turno(id, id_paciente, especialidad, monto_a_pagar, estado_turno,lista_turnos)
        break

def buscar_proyecto_por_id(lista_proyectos: list[dict], id_a_buscar: int) -> dict:
    # El código itera a través de una lista de proyectos (`lista_proyectos`) y verifica si `id_a_buscar`
    # coincide con el `id` de algún proyecto en la lista. Si se encuentra una coincidencia, a la variable
    # `proyecto_a_buscar` se le asigna el proyecto con el ID coincidente y se sale del bucle usando
    # `break`. Finalmente, el código devuelve el proyecto encontrado o "Ninguno" si no se encontró ningún
    # proyecto coincidente.
    proyecto_a_buscar = None

    for proyecto in lista_proyectos:
        if id_a_buscar == proyecto["id"]:
            proyecto_a_buscar = proyecto
            break

    return proyecto_a_buscar 

def mostrar_pacientes_activos(lista_pacientes:list, lista_turnos:list):
    """
    Esta funcion filtra y muestra los pacientes que tienen turnos activos
    """

    lista_activos_turnos = list(filter(lambda turno: turno['estado_turno'] == "Activo",lista_turnos))#aca obtengo la lista con turnos activos

    ids_pacientes_con_turnos_activos = []#aca obtengo el id de los pacientes

    list(map(lambda ids: ids_pacientes_con_turnos_activos.append(ids['id_paciente']), lista_activos_turnos))

    lista_pacientes_activos =  list(filter(lambda paciente: paciente['id'] in ids_pacientes_con_turnos_activos, lista_pacientes))

    if len(lista_pacientes_activos) == 0:
        print("No hay pacientes Activos para mostrar.")
    elif len(lista_pacientes_activos) == 1:
        mostrar_paciente_tabla(lista_pacientes_activos[0])
    else:
        mostrar_pacientes_tabla(lista_pacientes_activos)

def atender_pacientes(lista_pacientes:list, lista_turnos:list) -> bool:
    """
    Esta funcion atiende a los pacientes cambiando el estado de sus turnos "Activo" a "Finalizado"
    Retorna un bool
    """
    retorno = False
    contador = 0
    for paciente in lista_pacientes:
        for turno in lista_turnos:
            if  turno['estado_turno'] == "Activo":
                    if paciente["id"] == turno['id_paciente']:
                        if contador < 2:
                            turno["estado_turno"] = "Finalizado"
                            mostrar_paciente_tabla(paciente)
                            contador += 1
                            retorno = True

    return retorno

def cobrar_atenciones(lista_pacientes:list, lista_turnos:list,Clinica:object):
    """
    Esta funcion cobra las atenciones finalizadas a los pacientes y actualiza la recaudacion total en la instancia clinica
    Imprime un mensaje indicando la cantidad de pacientes a los que se les cobraron atenciones correctamente
    """
    recaudacion_total = 0
    contador = 0

    for paciente in lista_pacientes:
        for turno in lista_turnos:
            if paciente['id'] == turno['id_paciente']:
                if turno['estado_turno'] == "Finalizado":
                    turno["estado_turno"] = "Pagado"
                    plata = turno['monto_a_pagar']
                    recaudacion_total += plata
                    contador += 1 


    if contador == 0:
        print("Hay pacientes por atender.")
    elif contador == 1:
        print(f'Se cobraron atenciones correctamente de {contador} paciente.')
    else:
        print(f'Se cobraron atenciones correctamente de {contador} pacientes.')

    
    Clinica.recaudacion = recaudacion_total

def cerrar_caja(lista_pacientes:list, lista_turnos:list,clinica:object) -> bool:
    """
    Esta funcion cierra la caja de la clinica verificando si hay al menos un turno pagado para cada paciente
    Retorna True si hay al menos un turno pagado para algun paciente, False si no hay ningun turno pago.
    """
    retorno = False
    for paciente in lista_pacientes:
        for turno in lista_turnos:
            if paciente['id'] == turno['id_paciente']:
                if turno['estado_turno'] == "Pagado":
                    retorno = True

    clinica.guardar_pacientes(lista_pacientes)
    clinica.guardar_turnos(lista_turnos)

    return retorno

def calcular_monto_a_pagar(diccionario: dict)-> float:
    """
    Esta funcion calcula el costo de una consulta medica basandose en la obra social del paciente y su edad
    Retorna el monto calculado a pagar por la consulta medica, un float.
    """
    precio_base = 4000

    monto = 0
    
    
    if diccionario["obra social"] == "Swiss Medical":
        swis = precio_base * 0.6
        monto = swis
        if diccionario["edad"] > 18 and diccionario["edad"] < 60:
            monto = monto * 0.9
    elif diccionario["obra social"] == "Apres":
        apres = precio_base * 0.75
        monto = apres
        if diccionario["edad"] > 26 and diccionario["edad"] < 59:
            monto = monto * 0.97
    elif diccionario["obra social"] == "PAMI":
        resul_pami = precio_base * 0.4
        monto = resul_pami
        if diccionario["edad"] > 80:
            monto = monto * 0.97
    else:
        particular = precio_base * 1.05
        monto = particular
        if diccionario["edad"] > 40 and diccionario["edad"] < 60:
            monto = monto * 1.15

    return monto

def mostar_informe(lista_pacientes:list, lista_turnos:list):
    """
    Esta función se encarga de calcular la recaudación total de cada obra social
    y determinar cuál es la que menos recaudó. Luego muestra esta información.
    """
    recaudacion_swis = 0
    recaudacion_apres = 0
    recaudacion_pami = 0
    recaudacion_particular = 0

    for paciente in lista_pacientes:
        for turno in lista_turnos:
            if paciente['id'] == turno['id_paciente']:
                if paciente["obra social"] == "Swiss Medical":
                    plata = turno['monto_a_pagar']
                    recaudacion_swis += plata
                elif paciente["obra social"] == "Apres":
                    plata = turno['monto_a_pagar']
                    recaudacion_apres += plata
                elif paciente["obra social"] == "PAMI":
                    plata = turno['monto_a_pagar']
                    recaudacion_pami += plata
                elif paciente["obra social"] == "Particular":
                    plata = turno['monto_a_pagar']
                    recaudacion_particular += plata


    if recaudacion_swis < recaudacion_apres < recaudacion_pami < recaudacion_particular:
        print(f'La obra social que menos recaudo fue Swiss Medical con un monto de {recaudacion_swis}')
    elif recaudacion_apres < recaudacion_pami < recaudacion_particular:
        print(f'La obra social que menos recaudo fue Apres con un monto de {recaudacion_apres}')
    elif recaudacion_pami < recaudacion_particular:
        print(f'La obra social PAMI fue la que menos recuado con un monto de {recaudacion_pami}')
    else:
        print(f'Los pacientes particulares fueron los que menos recaudaron con un monto de {recaudacion_particular}')

def imprimir_linea_separar(guion="-", ancho=158) -> str:
    print(guion * ancho)

def mostrar_pacientes_tabla(lista_pacientes):
    """
    Muestra la lista de todos los pacientes en formato de tabla.
    """
    imprimir_linea_separar()

    print(f"| {'ID':5} | {'Nombre':15} | {'Apellido':15} | {'DNI':10} | {'Edad':5} | {'Fecha de Registro':15} | {'Obra Social':15} |\n")
    for paciente in lista_pacientes:
        print(f"| {paciente['id']:5} | {paciente['nombre']:15} | {paciente['apellido']:15} | {paciente['dni']:10} | {paciente['edad']:5} | {paciente['fecha de registro']:15} | {paciente['obra social']:15} |")

    imprimir_linea_separar()

def mostrar_paciente_tabla(paciente):
    """
    Muestra los detalles de un solo paciente en formato de tabla.
    """
    retorno = False
    imprimir_linea_separar()
    if paciente:
        print(f"| {'ID':5} | {'Nombre':15} | {'Apellido':15} | {'DNI':10} | {'Edad':5} | {'Fecha de Registro':15} | {'Obra Social':15} |\n")
        print(f"| {paciente['id']:5} | {paciente['nombre']:15} | {paciente['apellido']:15} | {paciente['dni']:10} | {paciente['edad']:5} | {paciente['fecha de registro']:15} | {paciente['obra social']:15} |")
        retorno = True
    else:
        print("No hay ningun paciente para mostrar.")
        retorno = False
    
    return retorno
    imprimir_linea_separar()

def mostrar_turno_tabla(turno):
    """
    Muestra los detalles de un solo turno en formato de tabla.
    """
    imprimir_linea_separar()
    
    print(f"| {'ID':5} | {'ID Paciente':12} | {'Especialidad':15} | {'Monto a Pagar':14} | {'Estado':10} |\n")
    print(f"| {turno['id']:5} | {turno['id_paciente']:12} | {turno['especialidad']:15} | ${turno['monto_a_pagar']:12} | {turno['estado_turno']:10} |")
    
    imprimir_linea_separar()

def mostrar_varios_turnos_tabla(lista_turnos):
    """
    Muestra la lista de todos los turnos en formato de tabla.
    """
    imprimir_linea_separar()
    
    print(f"| {'ID':5} | {'ID Paciente':12} | {'Especialidad':15} | {'Monto a Pagar':14} | {'Estado':10} |\n")
    for turno in lista_turnos:
        print(f"| {turno['id']:5} | {turno['id_paciente']:12} | {turno['especialidad']:15} | ${turno['monto_a_pagar']:12} | {turno['estado_turno']:10} |")
    
    imprimir_linea_separar()

def ordenar_turnos(lista_pacientes: list,lista_turnos: list) -> bool:
    """
    La función "ordenar_proyectos" ordena una lista de proyectos según criterios seleccionados por el
    usuario, como nombre, presupuesto o fecha de inicio, en orden ascendente o descendente.

    :param lista_proyectos: La función `ordenar_proyectos` toma como entrada una lista de diccionarios
    `lista_proyectos`. Cada diccionario de la lista representa un proyecto y contiene información como
    el nombre del proyecto, el presupuesto y la fecha de inicio
    :type lista_proyectos: list[dict]
    """

    print("Ordenar turnos:\n1. Por obra social ascendente. \n2. Por monto descendente.\n")
    

    respuesta = validar_numero("Ingrese la opcion q desea: ")

    retorno = False

    match respuesta:
            case 1:
                ids_pacientes = []

                list(map(lambda ids: ids_pacientes.append(ids['id_paciente']), lista_turnos))

                lista_pacientes_2 =  list(filter(lambda paciente: paciente['id'] in ids_pacientes, lista_pacientes))
                for i in range(len(lista_pacientes_2) - 1):
                    for j in range(i + 1, len(lista_pacientes_2)):
                        if lista_pacientes_2[i]["obra social"] > lista_pacientes_2[j]["obra social"]:
                            aux = lista_pacientes_2[i]
                            lista_pacientes_2[i] = lista_pacientes_2[j]
                            lista_pacientes_2[j] = aux

                mostrar_pacientes_tabla(lista_pacientes_2)

                retorno = True                

            case 2:

                for i in range(len(lista_turnos) - 1):
                    for j in range(i + 1, len(lista_turnos)):
                        if lista_turnos[i]["monto_a_pagar"] < lista_turnos[j]["monto_a_pagar"]:
                            aux = lista_turnos[i]
                            lista_turnos[i] = lista_turnos[j]
                            lista_turnos[j] = aux

                mostrar_varios_turnos_tabla(lista_turnos)
                retorno = True


    return retorno
