from visitantes.visitantes import Visitantes
from animales.animales import Animales
from datetime import datetime
from zoo.zoo import Zoo
from administracion.administracion import Administracion
from usuario.utils.rol import Rol
from veterinario.veterinario import Veterinario
from mantenimiento.mantenimiento import Mantenimiento
from guia.guia import Guia
from enfermedades.enfermedades import Enfermedades
from alimentacion.alimentacion import Alimentacion

zoo= Zoo()

class Main: 
    

    while True:
            print("\nBIENVENIDO AL ZOO")
            
            
            print("\n1. Registrar")
            print("2. Mostrar")
            print("3. Modificar")
            print("4. Eliminar")
            
            opcion_menu = input("\nIngresa la opcion que deseas: ")
            
            if opcion_menu == "1": ##MENU REGISTRAR
                
                print("\n1. Registrar animal") #done
                print("2. Registrar visitante") #done
                print("3. Registrar personal (vet, guia, manten, admin)") #done
                print("4. Registrar visita")
                
                
                opcion_registro = input("\nIngresa la opcion que deseas: ")
                
                if opcion_registro == "1":  ##ANIMALES (R)
                    tipo = input("Ingresa el tipo  ")
                    id = zoo.generar_id_animal(tipo)
                    vacunas = bool(input("Ingresa TRUE si tiene vacunas o FALSE en caso de que no: "))
                    ano_nacimiento= int(input("Ingresa el año de nacimiento  "))
                    mes_nacimiento = int(input("Ingresa el mes de nacimiento  "))
                    dia_nacimiento = int(input("Ingresa el dia de nacimiento  "))
                    fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                    fecha_llegada = datetime.now().day
                    peso = input("Ingresa el peso  ")
                    frecuencia_de_alimentacion=  input("Ingresa la frecuencia de alimentacion: ")
                    animales = Animales(id=id, tipo=tipo, fecha_de_nacimiento=fecha_nacimiento, fecha_llegada=fecha_llegada, peso=peso, vacunas=vacunas, frecuencia_alimentacion=frecuencia_de_alimentacion)
                    while True:
                        enfermedades= input("REGISTRAR ENFERMEDAD si/no")
                        if enfermedades == "si":
                            zoo.registrar_enfermedades(animales, enfermedades)
                            zoo.reg_e(enfermedades)
                            mas=input("quiere añadir mas yes/no    ")
                            if mas == "no":
                                break
                        
                    zoo.registrar_animales(animales)
                    print("\n Animal registrado correctamente ")
                    
                elif opcion_registro == "2": ##VISITANTES (R)
                    nombre = input("Ingresa el nombre: ")
                    apellido = input("Ingresa el apellido: ")
                    curp = input("Ingresa el curp: ")
                    ano = int(input("Ingresa el año de registro: "))
                    mes = int(input("Ingresa el mes de registro: "))
                    dia = int(input("Ingresa el dia de registro: "))
                    fecha_registro = datetime(ano, mes, dia)
                    ano_nacimiento = int(input("Ingresa el año de nacimineto: "))
                    mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                    dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                    fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                    id_visitante = zoo.id_visitante(nombre=nombre)
                    
                    visitante = Visitantes(id_visitante=id_visitante ,nombre=nombre, apellido= apellido, curp=curp, fecha_registro=fecha_registro, fecha_nacimiento=fecha_nacimiento)
                    zoo.registrar_visitante(visitante)
                    print("Visitante registrado correctamente")
                
                elif opcion_registro == "3": ##PERSONAL
                    print("***Elegiste registrar a personal***")
                    nombre= input("Ingresa el nombre: ")
                    apellido=input("Ingresa el apellido: ")
                    
                    ano_nacimiento= int(input("Ingresa el año de nacimiento: "))
                    mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                    dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                    fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                    ano_ingreso= int(input("Ingresa el año de ingreso: "))
                    mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                    dia_ingreso = int(input("Ingresa el dia de ingreso: "))
                    fecha_ingreso_trabajador = datetime(ano_ingreso, mes_ingreso, dia_ingreso)
                    rfc=input("Ingresa el RFC: ")
                    curp=input("Ingresa el CURP: ")
                    salario=int(input("Ingresa el salario: "))
                    
                    horario_entrada_in=input("Ingresa la  hora de entrada (HH:MM): ")
                    horario_salida_in=input("Ingresa la hora de salida (HH:MM): ")
                    horario_entrada= datetime.strptime(horario_entrada_in, "%H:%M")
                    horario_salida= datetime.strptime(horario_salida_in, "%H:%M")
                    
                    hora_entrada = horario_entrada.strftime('%I:%M').lstrip('0')
                    hora_salida = horario_salida.strftime('%I:%M').lstrip('0')
                    
                    horario=f"{horario_entrada} - {horario_salida}"
            
                    print("\n1. Para registrar como veterinario")
                    print("2. Para registrar como guia") 
                    print("3. Para registrar como mantenimiento")
                    print("4. Para registrar como administracion")
                    
                    opcion_trabajador= input("\nIngresa la opcion que desees: ")
                    
                    if opcion_trabajador == "1":
                        id_trabajador= zoo.generar_id_trabajador(nombre=nombre,rol=Rol.VETERINARIO)
                        veterinario= Veterinario(id_trabajador=id_trabajador, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol)
                    
                        zoo.registrar_veterinario(veterinario)
                    
                        print("\nVeterinario registrado correctamente")
                    
                    elif opcion_trabajador == "2":
                        id_trabajador = zoo.generar_id_trabajador(nombre, rol=Rol.GUIA)
                        guia = Guia(id_trabajador=id_trabajador, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol)

                        zoo.registrar_guia(guia)
                        print("\nGuia registrado correctamente")
                        
                    elif opcion_trabajador == "3":
                        id_trabajador= zoo.generar_id_trabajador(nombre=nombre,rol=Rol.MANTENIMIENTO)
                        mantenimiento= Mantenimiento(id_trabajador=id_trabajador , nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol)
                    
                        zoo.registrar_mantenimiento(mantenimiento)
                    
                        print("\nTrabajador de mantenimiento registrado correctamente")
                    
                    elif opcion_trabajador == "4": 
                        id_trabajador= zoo.generar_id_trabajador(nombre=nombre,rol=Rol.ADMINISTRACION)
                        administracion= Administracion(id_trabajador=id_trabajador ,nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol)
                    
                        zoo.registrar_administracion(administracion)
                    
                        print("\nTrabajador de administracion registrado correctamente")
                        
                elif opcion_registro == "3":
                    ##REGISTRAR VISITANTE
                    nombre = input("\nIngresa el nombre: ")
                    apellido = input("Ingresa el apellido: ")
                    curp = input("Ingresa el curp: ")
                    ano = int(input("Ingresa el año de registro: "))
                    mes = int(input("Ingresa el mes de registro: "))
                    dia = int(input("Ingresa el dia de registro: "))
                    fecha_registro = datetime(ano, mes, dia)
                    ano_nacimiento = int(input("Ingresa el año de nacimineto: "))
                    mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                    dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                    fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                    id_visitante = zoo.id_visitante(nombre=nombre)
                    
                    visitante = Visitantes(id_visitante=id_visitante ,nombre=nombre, apellido= apellido, curp=curp, fecha_registro=fecha_registro, fecha_nacimiento=fecha_nacimiento)
                    zoo.registrar_visitante(visitante)
                    print("\nVisitante registrado correctamente")
                
            if opcion_menu == "2": ##MENU MOSTRAR
                
                print("\n1. Mostrar animal") #done
                print("2. Mostrar veterinario") #done
                print("3. Mostrar guia") #done
                print("4. Mostrar mantenimiento") #done
                print("5. Mostrar administracion") #done
                
                opcion_mostrar =input("Ingresa la opcion que deseas: ")
                
                if opcion_mostrar == "1":
                    print("***ANIMALES***")
                    zoo.listar_animales()
                
                elif opcion_mostrar == "2":
                    print("***VETERINARIOS***")
                    zoo.listar_veterinaros()
            
                elif opcion_mostrar == "3":
                    print("***GUIAS***")
                    zoo.listar_guia()
    
                    
                elif opcion_mostrar == "4":
                    print("***MANTENIMIENTO***")
                    zoo.listar_mantenimiento()
                    
                elif opcion_mostrar == "5":
                    print("***ADMINISTRACION***")
                    zoo.listar_administracion()
             
            if opcion_menu == "3" : ##MENU MODIFICAR
                
                print("1. Modificar animal")
                print("2. Modificar visitante")
                print("3. Modificar veterinario")
                print("4. Modificar guia")
                print("5. Modificar trabajador de mantenimiento")
                print("6. Modificar trabajador de adminisracion")
                
                opcion_modificar = input("Ingresa la opcion que deseas: ")
                
                if opcion_modificar == "1": ##MODIFICAR ANIMAL
                    print("\nSeleccionaste la opción para modificar un animal")
                    id = input("Ingresa el id del animal a modificar")
                    animales = zoo.checar_id(id=id)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_tipo = None
                    nuevo_nacimiento = None
                    nuevo_llegada = None
                    nuevo_peso = None
                    nuevo_alimentacion = None
                    nuevas_vacunas = None
                    nueva_enfermedad = None
                    nueva_medicina = None
                    
                    while True:
                        print("\n1. Tipo")
                        print("2. Peso")
                        print("3. Fecha de llegada")
                        print("4. Fecha de nacimiento")
                        print("5. Vacunas")
                        print("6. Alimentación")
                        print("7. Enfermedad")
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_tipo = input("Ingresa el nuevo tipo: ")

                        elif modify == "5":
                            nuevas_vacunas = input("¿Tiene vacunas? (si/no): ").lower() == "si"

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de llegada: "))
                            mes_llegada = int(input("Ingresa el mes de llegada: "))
                            dia_llegada = int(input("Ingresa el día de llegada: "))
                            nuevo_llegada = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "2":
                            nuevo_peso = float(input("Ingresa el nuevo peso: "))

                        elif modify == "6":
                            nuevo_alimentacion = input("Ingresa la nueva frecuencia de alimentación: ")

                        elif modify == "7":  
                            nueva_enfermedad = input("Ingresa la nueva enfermedad: ")
                            enfermedades = Enfermedades(enfermedad=nueva_enfermedad)
                            zoo.registrar_enfermedades(animales, enfermedades)
                            mas=input("quiere añadir mas yes/no    ")
                            if mas == "no":
                                break

                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_animales(id=id, nuevo_tipo=nuevo_tipo, nuevo_peso=nuevo_peso, nuevas_vacunas=nuevas_vacunas,
                                        nuevo_nacimiento=nuevo_nacimiento, nuevo_llegada=nuevo_llegada, nuevo_alimentacion=nuevo_alimentacion)
                        
                    
                elif opcion_modificar == "2":  ##MODIFICAR VISITANTE (ESTÀ MAL)
                    print("\nSeleccionaste la opción para modificar un visitante")
                    id_visitante = input("Ingresa el id del visitante a modificar")
                    zoo.obtener_visitante_por_id(id_visitante=id_visitante)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_nombre= None 
                    nuevo_apellido= None 
                    nuevo_nacimiento= None
                    nuevo_ingreso= None
                    nuevo_visitas= None
                    nuevo_curp= None

                    while True:
                        print("\n1. Nombre")
                        print("2. Apellido")
                        print("3. Fecha de registro")
                        print("4. Fecha de nacimiento")
                        print("5. CURP")
                        print("6. Visitas")
                        
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_nombre = input("Ingresa el nuevo nombre: ")

                        elif modify == "2":
                            nuevo_apellido = input("Ingresa el nuevo apellido: ")

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de registro: "))
                            mes_llegada = int(input("Ingresa el mes de registro: "))
                            dia_llegada = int(input("Ingresa el día de registro: "))
                            nuevo_ingreso = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "5":
                            nuevo_curp = input("Ingresa el nuevo curp")
                        elif modify == "6":
                            nuevo_visitas = input("Ingresa el numero de visitas correcto: ")
                        
                        
                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_visitante(
                        id_trabajador=id_trabajador,
                        nuevo_nombre=nuevo_nombre,
                        nuevo_apellido=nuevo_apellido,
                        nuevo_nacimiento=nuevo_nacimiento,
                        #nuevo_ingreso_trabajador=nuevo_ingreso_trabajdor,
                        #nuevo_rfc=nuevo_rfc,
                        #nuevo_curp=nuevo_curp,
                        #nuevo_salario=nuevo_salario,
                        #nuevo_horario=nuevo_horario
                        )   
            
                elif opcion_modificar == "3": ##MODIFICAR VETERINARIO
                     
                    print("\nSeleccionaste la opción para modificar un veterinario")
                    id_trabajador = input("Ingresa el id del veterinario a modificar")
                    zoo.checar_id_vet(id_trabajador=id_trabajador)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_nombre= None 
                    nuevo_apellido= None 
                    nuevo_nacimiento= None
                    nuevo_ingreso_trabajador= None
                    nuevo_rfc= None
                    nuevo_curp= None
                    nuevo_salario= None 
                    nuevo_horario= None

                    while True:
                        print("\n1. Nombre")
                        print("2. Apellido")
                        print("3. Fecha de ingreso")
                        print("4. Fecha de nacimiento")
                        print("5. CURP")
                        print("6. RFC")
                        print("7. Salario")
                        print("8. Horario")
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_nombre = input("Ingresa el nuevo nombre: ")

                        elif modify == "2":
                            nuevo_apellido = input("Ingresa el nuevo apellido: ")

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de llegada: "))
                            mes_llegada = int(input("Ingresa el mes de llegada: "))
                            dia_llegada = int(input("Ingresa el día de llegada: "))
                            nuevo_ingreso_trabajador = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "8":
                            horario_entrada_in=input("Ingresa la  hora de entrada (HH:MM): ")
                            horario_salida_in=input("Ingresa la hora de salida (HH:MM): ")
                            horario_entrada= datetime.strptime(horario_entrada_in, "%H:%M")
                            horario_salida= datetime.strptime(horario_salida_in, "%H:%M")
                    
                            hora_entrada = horario_entrada.strftime('%I:%M').lstrip('0')
                            hora_salida = horario_salida.strftime('%I:%M').lstrip('0')
                    
                            nuevo_horario=f"{horario_entrada} - {horario_salida}"

                        elif modify == "5":
                            nuevo_curp = input("Ingresa el nuevo curp")
                        elif modify == "6":
                            nuevo_rfc = input("Ingresa el RFC correcto: ")
                        
                        elif modify == "7":
                            nuevo_salario = float(input("Ingresa el nuevo salario: "))

                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_vet(
                        id_trabajador=id_trabajador,
                        nuevo_nombre=nuevo_nombre,
                        nuevo_apellido=nuevo_apellido,
                        nuevo_nacimiento=nuevo_nacimiento,
                        nuevo_ingreso_trabajador=nuevo_ingreso_trabajador,
                        nuevo_rfc=nuevo_rfc,
                        nuevo_curp=nuevo_curp,
                        nuevo_salario=nuevo_salario,
                        nuevo_horario=nuevo_horario)
                        
                elif opcion_modificar == "4":  ##MODIFICAR GUIA
                    
                    print("\nSeleccionaste la opción para modificar un guia")
                    id_trabajador = input("Ingresa el id del guia a modificar")
                    zoo.checar_id_guia(id_trabajador=id_trabajador)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_nombre= None 
                    nuevo_apellido= None 
                    nuevo_nacimiento= None
                    nuevo_ingreso_trabajador= None
                    nuevo_rfc= None
                    nuevo_curp= None
                    nuevo_salario= None 
                    nuevo_horario= None

                    while True:
                        print("\n1. Nombre")
                        print("2. Apellido")
                        print("3. Fecha de ingreso")
                        print("4. Fecha de nacimiento")
                        print("5. CURP")
                        print("6. RFC")
                        print("7. Salario")
                        print("8. Horario")
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_nombre = input("Ingresa el nuevo nombre: ")

                        elif modify == "2":
                            nuevo_apellido = nuevo_apellido = input("Ingresa el nuevo apellido: ")

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de llegada: "))
                            mes_llegada = int(input("Ingresa el mes de llegada: "))
                            dia_llegada = int(input("Ingresa el día de llegada: "))
                            nuevo_ingreso_trabajador = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "8":
                            horario_entrada_in=input("Ingresa la  hora de entrada (HH:MM): ")
                            horario_salida_in=input("Ingresa la hora de salida (HH:MM): ")
                            horario_entrada= datetime.strptime(horario_entrada_in, "%H:%M")
                            horario_salida= datetime.strptime(horario_salida_in, "%H:%M")
                    
                            hora_entrada = horario_entrada.strftime('%I:%M').lstrip('0')
                            hora_salida = horario_salida.strftime('%I:%M').lstrip('0')
                    
                            nuevo_horario=f"{horario_entrada} - {horario_salida}"

                        elif modify == "5":
                            nuevo_curp = input("Ingresa el nuevo curp")
                        elif modify == "6":
                            nuevo_rfc = input("Ingresa el RFC correcto: ")
                        
                        elif modify == "7":
                            nuevo_salario = float(input("Ingresa el nuevo salario: "))

                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_guia(
                        id_trabajador=id_trabajador,
                        nuevo_nombre=nuevo_nombre,
                        nuevo_apellido=nuevo_apellido,
                        nuevo_nacimiento=nuevo_nacimiento,
                        nuevo_ingreso_trabajador=nuevo_ingreso_trabajador,
                        nuevo_rfc=nuevo_rfc,
                        nuevo_curp=nuevo_curp,
                        nuevo_salario=nuevo_salario,
                        nuevo_horario=nuevo_horario)
                
                elif opcion_modificar == "5": ##MODIFICAR MANTENIMIENTO
                    
                    print("\nSeleccionaste la opción para modificar un trabajador de mantenimiento")
                    id_trabajador = input("Ingresa el id del trabajador de mantenimiento a modificar")
                    zoo.checar_id_matenimiento(id_trabajador=id_trabajador)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_nombre= None 
                    nuevo_apellido= None 
                    nuevo_nacimiento= None
                    nuevo_ingreso_trabajador= None
                    nuevo_rfc= None
                    nuevo_curp= None
                    nuevo_salario= None 
                    nuevo_horario= None

                    while True:
                        print("\n1. Nombre")
                        print("2. Apellido")
                        print("3. Fecha de ingreso")
                        print("4. Fecha de nacimiento")
                        print("5. CURP")
                        print("6. RFC")
                        print("7. Salario")
                        print("8. Horario")
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_nombre = input("Ingresa el nuevo nombre: ")

                        elif modify == "2":
                            nuevo_apellido = input("Ingresa el nuevo apellido: ")

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de llegada: "))
                            mes_llegada = int(input("Ingresa el mes de llegada: "))
                            dia_llegada = int(input("Ingresa el día de llegada: "))
                            nuevo_ingreso_trabajador = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "8":
                            horario_entrada_in=input("Ingresa la  hora de entrada (HH:MM): ")
                            horario_salida_in=input("Ingresa la hora de salida (HH:MM): ")
                            horario_entrada= datetime.strptime(horario_entrada_in, "%H:%M")
                            horario_salida= datetime.strptime(horario_salida_in, "%H:%M")
                    
                            hora_entrada = horario_entrada.strftime('%I:%M').lstrip('0')
                            hora_salida = horario_salida.strftime('%I:%M').lstrip('0')
                    
                            nuevo_horario=f"{horario_entrada} - {horario_salida}"

                        elif modify == "5":
                            nuevo_curp = input("Ingresa el nuevo curp")
                        elif modify == "6":
                            nuevo_rfc = input("Ingresa el RFC correcto: ")
                        
                        elif modify == "7":
                            nuevo_salario = float(input("Ingresa el nuevo salario: "))

                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_mantenimiento(
                        id_trabajador=id_trabajador,
                        nuevo_nombre=nuevo_nombre,
                        nuevo_apellido=nuevo_apellido,
                        nuevo_nacimiento=nuevo_nacimiento,
                        nuevo_ingreso_trabajador=nuevo_ingreso_trabajador,
                        nuevo_rfc=nuevo_rfc,
                        nuevo_curp=nuevo_curp,
                        nuevo_salario=nuevo_salario,
                        nuevo_horario=nuevo_horario)
                    
                elif opcion_modificar == "5": ##MODIFICAR ADMIN
                    
                    print("\nSeleccionaste la opción para modificar un administrador")
                    id_trabajador = input("Ingresa el id del administrador a modificar")
                    zoo.checar_id_admin(id_trabajador=id_trabajador)
                    print("\nQue dato quieres modificar?")
                    
                    nuevo_nombre= None 
                    nuevo_apellido= None 
                    nuevo_nacimiento= None
                    nuevo_ingreso_trabajador= None
                    nuevo_rfc= None
                    nuevo_curp= None
                    nuevo_salario= None 
                    nuevo_horario= None

                    while True:
                        print("\n1. Nombre")
                        print("2. Apellido")
                        print("3. Fecha de ingreso")
                        print("4. Fecha de nacimiento")
                        print("5. CURP")
                        print("6. RFC")
                        print("7. Salario")
                        print("8. Horario")
                        
                        modify = input("Ingresa la opción que deseas: ")

                        if modify == "1":
                            nuevo_nombre = input("Ingresa el nuevo nombre: ")

                        elif modify == "2":
                            nuevo_apellido = input("Ingresa el nuevo apellido: ")

                        elif modify == "4":
                            ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                            mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                            dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                            nuevo_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)

                        elif modify == "3":
                            ano_llegada = int(input("Ingresa el año de llegada: "))
                            mes_llegada = int(input("Ingresa el mes de llegada: "))
                            dia_llegada = int(input("Ingresa el día de llegada: "))
                            nuevo_ingreso_trabajador = datetime(ano_llegada, mes_llegada, dia_llegada)

                        elif modify == "8":
                            horario_entrada_in=input("Ingresa la  hora de entrada (HH:MM): ")
                            horario_salida_in=input("Ingresa la hora de salida (HH:MM): ")
                            horario_entrada= datetime.strptime(horario_entrada_in, "%H:%M")
                            horario_salida= datetime.strptime(horario_salida_in, "%H:%M")
                    
                            hora_entrada = horario_entrada.strftime('%I:%M').lstrip('0')
                            hora_salida = horario_salida.strftime('%I:%M').lstrip('0')
                    
                            nuevo_horario=f"{horario_entrada} - {horario_salida}"

                        elif modify == "5":
                            nuevo_curp = input("Ingresa el nuevo curp")
                        elif modify == "6":
                            nuevo_rfc = input("Ingresa el RFC correcto: ")
                        
                        elif modify == "7":
                            nuevo_salario = float(input("Ingresa el nuevo salario: "))

                        continuar = input("¿Deseas modificar otro dato? (si/no): ")
                        if continuar.lower() == "no":
                            break

                    zoo.modificar_admin(
                        id_trabajador=id_trabajador,
                        nuevo_nombre=nuevo_nombre,
                        nuevo_apellido=nuevo_apellido,
                        nuevo_nacimiento=nuevo_nacimiento,
                        nuevo_ingreso_trabajador=nuevo_ingreso_trabajador,
                        nuevo_rfc=nuevo_rfc,
                        nuevo_curp=nuevo_curp,
                        nuevo_salario=nuevo_salario,
                        nuevo_horario=nuevo_horario)
                    
            if opcion_menu =="4": ##ELIMINAR
                
                print("1. Eliminar animal")
                print("2. Eliminar veterinario")
                print("3. Eliminar guia")
                print("4. Eliminar trabajador de mantenimiento")
                print("5. Eliminar trabajador de administracion")
                
                
                opcion_eliminar = input("Ingresa la opcion que deseas")
                
                if opcion_eliminar =="1":
                    print("\nSeleccionaste la opción para eliminar un animal")
                    id = input("Ingresa el id del animal")
                    zoo.eliminar_animales(id=id)
                    print("Animal eliminado")
                    
                elif opcion_eliminar =="2":
                    print("\nSeleccionaste eliminar veternario")
                    id_trabajador = input("Ingresa ID de veterinario")
                    zoo.eliminar_veterinarios(id_trabajador=id_trabajador)
                    print("Veterinario eliminado")   
                     
                elif opcion_eliminar =="3":
                    print("\nSeleccionaste eliminar guia")
                    id_trabajador = input("Ingresa ID del guia")
                    zoo.eliminar_guia(id_trabajador=id_trabajador)
                    print("Guia eliminado")    
                
                elif opcion_eliminar =="4":
                    print("\nSeleccionaste eliminar trabajador de mantenimiento")
                    id_trabajador = input("Ingresa ID del trabajador de mantenimiento")
                    zoo.eliminar_mantenimiento(id_trabajador=id_trabajador)
                    print("Trabajador de mantenimiento eliminado")  
                      
                elif opcion_eliminar =="5":
                    print("\nSeleccionaste eliminar trabajador de administracion")
                    id_trabajador = input("Ingresa ID del trabajador de administracion")
                    zoo.eliminar_administracion(id_trabajador=id_trabajador)
                    print("Trabajador de administracion eliminado")    
                

                
                
                
                            
                    
                            
                    #############################################################################PRUEBAS













