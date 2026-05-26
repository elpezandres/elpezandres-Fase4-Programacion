from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import *

import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== SOFTWARE FJ ===")


# SIMULACION 1
try:

    cliente1 = Cliente("Fredy", "fredy@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 50000, 3)

    reserva1 = Reserva(cliente1, servicio1)

    reserva1.confirmar()

    print(reserva1.mostrar())

except Exception as e:

    print(e)
    logging.error(e)


# SIMULACION 2
try:

    cliente2 = Cliente("", "correo@gmail.com")

except ClienteError as e:

    print("Error:", e)
    logging.error(e)


# SIMULACION 3
try:

    cliente3 = Cliente("Carlos", "carlosgmail.com")

except ClienteError as e:

    print("Error:", e)
    logging.error(e)


# SIMULACION 4
try:

    servicio2 = ReservaSala("Sala Básica", 30000, -2)

except Exception as e:

    print("Error:", e)
    logging.error(e)


# SIMULACION 5
try:

    reserva2 = Reserva(None, None)

except ReservaError as e:

    print("Error:", e)
    logging.error(e)


# SIMULACION 6
try:

    cliente4 = Cliente("Narly", "narly@gmail.com")

    servicio3 = Asesoria("Asesoría Python", 100000, 2)

    reserva3 = Reserva(cliente4, servicio3)

    reserva3.confirmar()

    print(reserva3.mostrar())

except Exception as e:

    print(e)
    logging.error(e)


# SIMULACION 7
try:

    cliente5 = Cliente("Juan", "juan@gmail.com")

    servicio4 = AlquilerEquipo("Laptop Gamer", 70000, 4)

    reserva4 = Reserva(cliente5, servicio4)

    reserva4.cancelar()

    print(reserva4.mostrar())

except Exception as e:

    print(e)
    logging.error(e)


# SIMULACION 8
try:

    cliente6 = Cliente("Laura", "laura@gmail.com")

except ClienteError as e:

    print(e)

else:

    print("Cliente creado correctamente")

finally:

    print("Proceso terminado")


# SIMULACION 9
try:

    try:

        numero = int("abc")

    except ValueError as e:

        raise ClienteError("Conversión inválida") from e

except ClienteError as error:

    print(error)
    logging.error(error)


# SIMULACION 10
try:

    servicio5 = None

    if servicio5 is None:
        raise ServicioError("Servicio no disponible")

except ServicioError as e:

    print(e)
    logging.error(e)