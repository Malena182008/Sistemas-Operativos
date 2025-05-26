def organizador_de_tareas():
    tareas = []
    
    while True:
        print("\nGestor de Tareas:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Actualizar estado de tarea")
        print("5. Salir")
        
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            tarea = input("Ingresa el nombre de la tarea: ")
            tareas.append({"tarea": tarea, "estado": "Pendiente"})
        
        elif opcion == 2:
            tarea_eliminar = input("Ingresa el nombre de la tarea a eliminar: ")
            tareas = [t for t in tareas if t["tarea"] != tarea_eliminar]
        
        elif opcion == 3:
            print("\nTareas actuales:")
            for t in tareas:
                print(f"Tarea: {t['tarea']} | Estado: {t['estado']}")
        
        elif opcion == 4:
            tarea_actualizar = input("Ingresa el nombre de la tarea a actualizar: ")
            for t in tareas:
                if t["tarea"] == tarea_actualizar:
                    nuevo_estado = input("Ingresa el nuevo estado (Pendiente, En progreso, Completada): ")
                    t["estado"] = nuevo_estado
                    break
        
        elif opcion == 5:
            print("Saliendo del gestor de tareas...")
            break
        
        else:
            print("Opción no válida.")

organizador_de_tareas()
