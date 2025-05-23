'''
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas. (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
'''
# Tipos de datos por valor
my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30

print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)

print(my_list_a)
print(my_list_b)

# Funciones con datos por valor
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia
my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)
    
    my_list_d = my_list_e
    
    my_list_d.append(40)
    
    print(my_list_e)
    print(my_list_d)
    
my_list_func(my_list_c)
print(my_list_c)

print('----------------------------------------------------')
'''
DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia. Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas. Comprueba también que se ha conservado el valor original en las primeras.
'''
# Por valor
var1 = 2
var2 = 4
def prog1(var1: int, var2: int):
    var3 = var1
    var1 = var2
    var2 = var3
    print(var1, var2)

print(var1, var2)
prog1(var1, var2)

print('----------------------------------------------------')
# Por referencia
list1 = [1, 2]
list2 = [3, 4]

def prog2(list1: list, list2: list):
    list3 = list1
    list1 = list2
    list2 = list3
    
    print(list1, list2)

print(list1, list2)
prog2(list1, list2)