from paciente import *
from library_utn import *

class Clinica:
    def __init__(self,razon_social, lista_pacientes, lista_turnos, especialidades, obras_sociales, recaudacion, hay_pacientes_sin_atencion):
        self.razon_social = ""
        self.lista_pacientes = []
        self.lista_turnos = []
        self.especialidades = {}
        self.obras_sociales = {}
        self.recaudacion = float
        self.hay_pacientes_sin_atencion = False



    def cargar_paciente(self, id, nombre, apellido, dni, edad, fecha_de_registro, obra_social,lista:list):


        paciente = {"id": id, "nombre": nombre, "apellido": apellido,
                "dni": dni, "edad": edad, "fecha de registro": fecha_de_registro, "obra social": obra_social}

            # mostrar_proyecto(proyecto)
        confirma = confirmacion("Desea confimar el alta (S/N): ",
                                "ERROR: Solo se acepta (S/N): ")
        mostrar_paciente_tabla(paciente)
        if confirma:
            lista.append(paciente)

    def alta_turno(self, id,id_paciente, especialidad, monto_a_pagar, estado_turno,lista: list):

        turno = {"id": id, "id_paciente": id_paciente, "especialidad": especialidad,
            "monto_a_pagar": monto_a_pagar,"estado_turno": "Activo"}

        confirma = confirmacion("Desea confimar el alta (S/N): ",
                                "ERROR: Solo se acepta (S/N): ")

        if confirma:
            lista.append(turno)
        

    def guardar_pacientes(self,lista_pacientes:list):

        lista_nueva = []
        
        for pacientes in lista_pacientes:
                paciente = {"id": pacientes["id"], "nombre": pacientes["nombre"], "apellido": pacientes["apellido"],
                "dni": pacientes["dni"], "edad": pacientes["edad"], "fecha de registro": pacientes["fecha de registro"], "obra social": pacientes["obra social"]}
                lista_nueva.append(paciente)


        with open("lista_pacientes.json", "w",encoding='UTF-8') as file:
            json.dump(lista_nueva, file, indent=4)

    def guardar_turnos(self,lista_pacientes:list):

        lista_nueva = []
        
        for pacientes in lista_pacientes:
                paciente = {"id": pacientes["id"], "id_paciente": pacientes["id_paciente"], "especialidad": pacientes["especialidad"],
                "monto_a_pagar": pacientes["monto_a_pagar"], "estado_turno": pacientes["estado_turno"]}
                lista_nueva.append(paciente)


        with open("lista_turnos.json", "w",encoding='UTF-8') as file:
            json.dump(lista_nueva, file, indent=4)

    def cargar_pacientes(self):
        try:
            with open("lista_pacientes.json", "r", encoding='UTF-8') as file:
                pacientes = json.load(file)
        except FileNotFoundError:
            pacientes = []
        return pacientes

    def cargar_turnos(self):
        try:
            with open("lista_turnos.json", "r", encoding='UTF-8') as file:
                turnos = json.load(file)
        except FileNotFoundError:
            turnos = []
        return turnos
    




