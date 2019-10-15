string = 'cristian'
print(string.capitalize())  # Transforma la primer letra a mayusculas.
print(string.upper())  # Mayusculas
print(string.lower())  # Minusculas

string_2 = 'CRIStian'
# Invierte lo que este en upper en lower y viceversa
print(string_2.swapcase())


string_3 = 'cadena de caracteres'
# Transfroma las primerasletras de cada palabara en mayusculas.
print(string_3.title())
# Cunata cuantos caracteres hay del tipo que le asignemos
print(string_3.count("a"))
# Busca la palabra
print(string_3.find("de"))
# Valida la letra inicial de la cadena
print(string_3.startswith("c"))
print(string_3.startswith("f"))
# Valida la letra final de la cadena
print(string_3.endswith("c"))
print(string_3.endswith("s"))

# Remplzar valores en la cadena
buscar = "nombre y apellido"
reemplazar_por = "Cristian Hernandez"
print("Estimado Sr. nombre y apellido".replace(buscar, reemplazar_por))

# Sacar espacios vacíos
string_4 = "    Hola mundo      "
print(string_4)
print(string_4.strip())
