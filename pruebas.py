import library_utn as utn
from clinica import Clinica
from paciente import Paciente
from turno import Turno
import json
from validaciones import *


clinica = Clinica("UTN-Medical center",[],[],{},{},float,False)

a = clinica.cargar_pacientes()
b = clinica.cargar_turnos()



# def mostrar_pacientes_activos(lista_pacientes:list, lista_turnos:list):
#     lista_activos_turnos = list(filter(lambda turno: turno['estado_turno'] == "Activo",lista_turnos))
#     #[{'id': 1, 'id_paciente': 3, 'especialidad': 'Perez', 'monto_a_pagar': 1, 'estado_turno': 'Activo'}]

#     ids_pacientes_con_turnos_activos = [turno['id_paciente'] for turno in lista_activos_turnos]

#     lista_pacientes_activos =  list(filter(lambda paciente: paciente['id'] in ids_pacientes_con_turnos_activos, lista_pacientes))

#     print(lista_pacientes_activos)


# mostrar_pacientes_activos(a,b)

def mostrar_pacientes_activos(lista_pacientes:list, lista_turnos:list):

    lista_activos_turnos = list(filter(lambda turno: turno['estado_turno'] == "Activo",lista_turnos))#aca obtengo la lista con turnos activos

    ids_pacientes_con_turnos_activos = []#aca obtengo el id de los pacientes

    list(map(lambda ids: ids_pacientes_con_turnos_activos.append(ids['id_paciente']), lista_activos_turnos))

    lista_pacientes_activos =  list(filter(lambda paciente: paciente['id'] in ids_pacientes_con_turnos_activos, lista_pacientes))

    print(lista_pacientes_activos)


mostrar_pacientes_activos(a,b)

[
    {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Pérez",
        "dni": 35439054,
        "edad": 33,
        "fecha de registro": "01-01-2020",
        "obra social": "Particular"
    },
    {
        "id": 2,
        "nombre": "María",
        "apellido": "Gómez",
        "dni": 28764123,
        "edad": 45,
        "fecha de registro": "15-08-2019",
        "obra social": "Swiss Medical"
    },
    {
        "id": 3,
        "nombre": "Luis",
        "apellido": "Fernández",
        "dni": 39874561,
        "edad": 28,
        "fecha de registro": "20-02-2023",
        "obra social": "PAMI"
    },
    {
        "id": 4,
        "nombre": "Sofía",
        "apellido": "López",
        "dni": 45681239,
        "edad": 52,
        "fecha de registro": "10-11-2021",
        "obra social": "Apres"
    },
    {
        "id": 5,
        "nombre": "Pedro",
        "apellido": "Martínez",
        "dni": 28765412,
        "edad": 40,
        "fecha de registro": "05-05-2022",
        "obra social": "Swiss Medical"
    },
    {
        "id": 6,
        "nombre": "Ana",
        "apellido": "García",
        "dni": 36547891,
        "edad": 35,
        "fecha de registro": "30-09-2023",
        "obra social": "Particular"
    },
    {
        "id": 7,
        "nombre": "Miguel",
        "apellido": "Rodríguez",
        "dni": 21458796,
        "edad": 48,
        "fecha de registro": "12-04-2020",
        "obra social": "Apres"
    },
    {
        "id": 8,
        "nombre": "Lucía",
        "apellido": "Sánchez",
        "dni": 39875421,
        "edad": 25,
        "fecha de registro": "08-07-2021",
        "obra social": "PAMI"
    },
    {
        "id": 9,
        "nombre": "Carlos",
        "apellido": "Ramírez",
        "dni": 36548975,
        "edad": 30,
        "fecha de registro": "25-12-2022",
        "obra social": "Swiss Medical"
    },
    {
        "id": 10,
        "nombre": "Laura",
        "apellido": "Torres",
        "dni": 21459876,
        "edad": 42,
        "fecha de registro": "18-03-2023",
        "obra social": "Particular"
    },
    {
        "id": 11,
        "nombre": "a",
        "apellido": "a",
        "dni": 19,
        "edad": 19,
        "fecha de registro": "01-01-2023",
        "obra social": "apres"
    }
]

[
    {
        "id": 1,
        "id_paciente": 3,
        "especialidad": "Perez",
        "monto_a_pagar": 1,
        "estado_turno": "Finalizado"
    },
    {
        "id": 2,
        "id_paciente": 1,
        "especialidad": "Perez",
        "monto_a_pagar": 10,
        "estado_turno": "Activo"
    },
    {
        "id": 3,
        "id_paciente": 2,
        "especialidad": "Perez",
        "monto_a_pagar": 1,
        "estado_turno": "Pagado"
    },
    {
        "id": 4,
        "id_paciente": 4,
        "especialidad": "odontologia",
        "monto_a_pagar": 10,
        "estado_turno": "Activo"
    }
]