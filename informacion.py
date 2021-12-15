#Archivo de prueba
#Simulacion de datos para hacer pruebas

import platform

import getpass

import os

sistemaOperativo = platform.system()
versionSO = platform.win32_ver()
procesador = platform.processor()

usuario = getpass.getuser()

procesos = os.popen('wmic process get description, processid').read()

sistema = [
    {"SO": sistemaOperativo, "Version": versionSO, "Procesador": procesador}
]

usuario = [
    {"Username": usuario}
]

