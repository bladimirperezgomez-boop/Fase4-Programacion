



from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria

print("OPERACION 1")
cliente1 = Cliente("Bladimir Perez", 12345678, "bladimir@email.com")
print("Cliente creado")

print("\nOPERACION 2")
try:
    Cliente("", 123, "correo@email.com")
except Exception as e:
    print("Error:", e)

print("\nOPERACION 3")
try:
    Cliente("Pedro", -1, "correo@email.com")
except Exception as e:
    print("Error:", e)

print("\nOPERACION 4")
try:
    Cliente("Luis", 12345, "correoinvalido")
except Exception as e:
    print("Error:", e)

print("\nOPERACION 5")
sala = ServicioSala(3)
print(sala.describir())

print("\nOPERACION 6")
equipo = ServicioEquipo(2)
print(equipo.describir())

print("\nOPERACION 7")
asesoria = ServicioAsesoria(4)
print(asesoria.describir())

print("\nOPERACION 8")
print("Costo normal:", sala.calcular_costo())

print("\nOPERACION 9")
print("Costo con IVA:", sala.calcular_costo(0.19))

print("\nOPERACION 10")
servicios = [sala, equipo, asesoria]

for servicio in servicios:
    print(servicio.describir())
    print("Costo:", servicio.calcular_costo())
