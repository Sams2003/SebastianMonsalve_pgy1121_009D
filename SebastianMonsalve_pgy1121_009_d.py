import funciones as fn

while True:
    fn.ver_menu()
    opcion=fn.validar_opcion()
    if opcion == 1:
        fn.comprar()
    elif opcion == 2:
        fn.ver_escenario()
    elif opcion == 3:
        fn.ver_asistente()
    elif opcion == 4:
        fn.ver_ganancia()
    else:
        fn.salir()
        break
        