


def confirmacion(mensaje: str, mensaje_error: str) -> bool:
    """

    """
    confirmar = input(mensaje).upper()

    while confirmar != "S" and confirmar != "N":
        confirmar = input(mensaje_error).upper()

    if confirmar == "S":
        retorno = True
    else:
        retorno = False

    return retorno

def validar_numero(mensaje:str) -> int:
    while True:
        numero = input(mensaje)
        if not numero.isdigit():
            print("ERROR. Ingrese un numero.")
            continue
        
        numero = int(numero)
        return numero

def validar_dni() -> int:
    while True:
        numero = input("Ingrese su dni: ")
        if not numero.isdigit():
            print("ERROR. Ingrese un numero.")
            continue
        numero = int(numero)
        if numero > 60000000:
            print("ERROR. El numero ingresado es demasiado largo.")
            continue
        numero = int(numero)
        return numero
    

def validar_dia() -> int:
    """
    Esta función de Python solicita al usuario que ingrese un día entre 1 y 31, valida la entrada y
    devuelve el día como un número entero.
    :return: La función `validar_dia()` devuelve un valor entero que representa el día validado
    ingresado por el usuario.
    """
    while True:
        dia = input("Ingrese dia (entre 1 y 31): ")
        try:
            dia = int(dia)
            while dia < 1 or dia > 32:
                dia = int(input("Error. Ingrese dia entre 1 y 31: "))
            return dia
        
        except:
            print("Error ingrese un numero. ")

def validar_mes() -> int:
    """
    Esta función de Python solicita al usuario que ingrese un mes entre 1 y 12, validando la entrada
    para garantizar que sea un número dentro del rango especificado.
    :return: La función `validar_mes()` devuelve un valor entero que representa un mes válido entre 1 y
    12 ingresado por el usuario.
    """
    while True:
        mes = input("Ingrese mes (entre 1 y 12): ")
        try:
            mes = int(mes)
            while mes < 1 or mes > 12:
                mes = int(input("Error. Ingrese mes entre 1 y 12: "))
            return mes
        
        except:
            print("Error ingrese un numero. ")          

def validar_ano() -> int:
    """
    Esta función de Python solicita al usuario que ingrese un año dentro de un rango específico y valida
    la entrada.
    :return: La función `validar_ano()` devuelve un valor entero que representa el año validado
    ingresado por el usuario.
    """
    while True:
        ano = input("Ingrese ano: ")
        try:
            ano = int(ano)
            while ano < 1800 or ano > 3000:
                ano = int(input("Error. Ingrese ano correcta: "))
            return ano
        
        except:
            print("Error ingrese un numero. ")   

def ingresar_fecha_de_registro():
    """
    La función `ingresar_fecha_de_inicio` solicita al usuario que ingrese una fecha de inicio y valida
    el día, mes y año antes de formatear la fecha.
    """

    print("Ingrese Fecha de inicio.")

    dia = validar_dia()
    mes = validar_mes()
    ano = validar_ano()
    fecha_registro = f'{dia}-{mes}-{ano}'

    return fecha_registro

def validar_nombre() -> str:
    """
    Esta funcion valida la entrada del nombre de un paciente asegurándose de que no supere los
    30 caracteres y contenga solo caracteres alfabéticos.
    :return: el nombre del paciente.
    """
    while True:
        nombre = input("ingrese nombre del paciente: ")

        if len(nombre) > 30:
            print("ERROR. El nombre no puede exceder los 30 caracteres.")
            continue

        nombre_sin_espacios = nombre.replace(" ","")
        if not nombre_sin_espacios.isalpha():
            print("ERROR. El nombre debe contener solo caracteres alfabeticos.")
            continue

        return nombre

def validar_apellido() -> str:
    """
    Esta funcion valida la entrada del nombre de un paciente asegurándose de que no supere los
    30 caracteres y contenga solo caracteres alfabéticos.
    :return: el nombre del paciente.
    """
    while True:
        apellido = input("ingrese apellido del paciente: ")

        if len(apellido) > 30:
            print("ERROR. El apellido no puede exceder los 30 caracteres.")
            continue

        apellido_sin_espacios = apellido.replace(" ","")
        if not apellido_sin_espacios.isalpha():
            print("ERROR. El apellido debe contener solo caracteres alfabeticos.")
            continue

        return apellido

def validar_edad() -> int:
    """
    La funcion solicita al usuario que ingrese su edad y valida que el numero sea entre 18 y 90.
    :return: Se devuelve un valor entero que representa la edad.
    """
    while True:
        respuesta = input("Ingrese su edad (entre 18 y 90): ")
        
        if  not respuesta.isdigit():
            print("Error. Ingrese un numero.")
            continue

        elif int(respuesta) < 18 or int(respuesta) > 90:
            print("Error. Ingrese una edad entre 18 y 90.")
            continue

        else:
            respuesta = int(respuesta)
            return respuesta

def validar_obra_social(edad: int) -> str:
    """
    Esta funcion solicita al usuario que ingrese su proveedor de seguro medico y valida la
    entrada con una lista predefinida de opciones.
    :return: el input del usuario para la obra social después de validarlo.
    """
    
    respuesta_pami = "Pami"

    if edad < 60:
        while True:
    
            respuesta = input("Ingrese su obra social (Swiss Medical, Apres, Particular): ")
            respuesta = respuesta.lower()
            
            if respuesta != "swiss medical" and respuesta != "apres" and respuesta != "particular":
                print("ERROR. Ingrese una obra social correcta(Swiss Medical, Apres, Pami, Particular): ")
                continue

            return respuesta
    else:
        

            print("Usted tiene mas de 60, la unica opcion disponible para su obra social es 'Pami'.")
            return respuesta_pami

def validar_especialidad() -> str:
    while True:

        respuesta = input("Seleccione una especialidad (Medico Clinico, Odontologia, Psicologia, Traumatologia): ")
        respuesta = respuesta.lower()

        if respuesta != "medico clinico" and respuesta != "odontologia" and respuesta != "psicologia" and respuesta != "traumatologia":
            print("ERROR. Ingrese (Medico Clinico, Odontologia, Psicologia, Traumatologia.)")
            continue

        return respuesta
