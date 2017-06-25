#!/bin/bash
#Escaneo de redes con fping
echo Inserte el tercer octeto de la subred 
read direccion
echo $direccion
fping -g 192.168."$direccion".0/24 2>/dev/null | grep alive


