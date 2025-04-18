
import library_utn as utn
from clinica import Clinica
from validaciones import *

RUTA_CONFIGS = "configs.json"
RUTA_PACIENTES = "lista_pacientes.json"
RUTA_TURNOS = "lista_turnos.json"

def main_app():
    """
    Aplicacion principal del Segundo Parcial de Laboratorio 1
    """

    clinica = Clinica("UTN-Medical center",[],[],{},{},float,False)
    a = clinica.cargar_pacientes()
    b = clinica.cargar_turnos()
    while True:
        utn.mostar_menu()
        selected_option = utn.validar_numero("Seleccione una opcion del menu: ")
        
        match selected_option:
            case 1: # Alta paciente
                utn.alta_paciente(a,clinica)
            case 2: # Alta turno
                utn.alta_turno(a,b,clinica)
            case 3: # Ordenar turnos
                if utn.ordenar_turnos(a,b):
                    print("PROYECTO ORDENADO CORRECTAMENTE.")
                else:
                    print("NO SE PUDO ORDENAR EL PROYECTO")
            case 4: # Mostrar pacientes en espera
                utn.mostrar_pacientes_activos(a,b)
            case 5: # Atender pacientes
                if utn.atender_pacientes(a,b):
                    print("Se atendieron pacientes correctamente.")
                else:
                    print("No hay pacientes por atender.")
            case 6: # Cobrar atenciones
                utn.cobrar_atenciones(a,b,clinica)
            case 7: # Cerrar caja
                if utn.cerrar_caja(a,b,clinica):
                    print(f'Caja cerrada con un total de {clinica.recaudacion} pesos.')
                else:
                    print("Todavia hay pacientes por atender.")
            case 8: # Mostrar informe
                utn.mostar_informe(a,b)
            case 9:
                if len(a) == 1:
                    utn.mostrar_paciente_tabla(a[0])
                elif len(a) > 1:
                    utn.mostrar_pacientes_tabla(a)
                else:
                    print("No hay pacientes para mostrar")
            case 10:
                if len(b) == 1:
                    utn.mostrar_turno_tabla(b[0])
                else:
                    utn.mostrar_varios_turnos_tabla(b)
            case 11: # Salir
                break
            case _:
                utn.UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        utn.clear_console()
            
main_app()