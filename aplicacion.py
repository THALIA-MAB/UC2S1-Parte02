# -*- coding: utf-8 -*-

import os
import sys

def recoger_archivo(archivo):
    archivo = open(archivo,"rt",encoding="utf8")
    recoger_archivo = archivo.read()
    recoger_archivo = recoger_archivo.split("\n")
    return recoger_archivo

archivo_usuario = recoger_archivo("Login.txt")
archivo_clave = recoger_archivo("Clave.txt")

cont = 0

while cont != 2:
    
    usuario = input("Ingresar Usuario: ")
    clave = input("Ingresar Clave: ")
    
    for usuarioItem in archivo_usuario:
        if usuario == usuarioItem:
            for clave_Item in archivo_clave:
                if clave == clave_Item:
                    print ("El usuario y clave son correctos")
                    print ("Datos Persona\n1.Listar personas\nAgregar personas\nSalir\n")
                    cont = 2
                else:
                    print ("Los datos digitados son incorrectos\n")
                    cont += 1
            else:
                print ("El usuario digitado es incorrecto\n")
                cont += 1
            
            
