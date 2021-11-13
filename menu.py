import argparse
import sys

from cracker import cracker
from virustotal import total
from socketscript import socketd
from help import pwshell

def main():
    opcion = input("Escoge la opcion: 
    1)Escanear archivos maliciosos
    2)Crackear contraseñas
    3)IP
    4)help")
    if opcion == "1":
        url = argparse.ArgumentParser()
        url.add_argument('--x', type=str,help='escribe la url del archivo')
        args=url.parse_args()
        sys.stdout.write(total(args))
    elif opcion == "2":
        url = argparse.ArgumentParser()
        url.add_argument('--x', type=str,help='inserte la contraseña hasheada')
        url.add_argument('--y', type=str,help='escribe la url del archivo')
        args=url.parse_args()
        sys.stdout.write(str(cracker(args)))
    elif opcion == "3":
        socketd()
    else:
        pwshell()
if __name__ == "__main__":
    main()