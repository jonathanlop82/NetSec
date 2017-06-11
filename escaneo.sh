#!/bin/bash
#Escaneo de redes con fping - Por: Jonathan Lopez @jonathanlop82
echo Inserte el tercer octeto de la subred
read direccion
echo $direccion
fping -g 192.168."$direccion".0/24 2>/dev/null | grep alive
