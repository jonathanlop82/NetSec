# coding=utf-8
import nmap
import sys

print ("Scanmmd: , Desarrollado por Jonathan López, 2017")
direccion    = raw_input("Introduzca el numero de sucursal: ")
num = int(direccion)
dirip = ''

sucursales = [['192.168.0.0/24','Home'],['192.168.1.0/24','Via Argentina'],['192.168.2.0/24','Rio Abajo'],['192.168.3.0/24','Calidonia'],['192.168.4.0/24','Peatonal'],['192.168.5.0/24','San Miguelito'],['192.168.6.0/24','Via Porras'],['192.168.7.0/24','Vista Hermosa'],['192.168.8.0/24','Pedregal'],['192.168.9.0/24','Plaza Carolina'],['192.168.24.0/23','Transistmica']]

dirip = str(sucursales[(num-1)][0])
nombre = str(sucursales[(num-1)][1])
print ('Sucursal: '+nombre)
print ('Subred: '+dirip)

nm = nmap.PortScanner()
#resultado = nm.scan(dirip,'22,25,80,443')
#print(nombre)
#print(nm.csv())
#else:
#    print ('No se encontro la sucursal')
contador = 0
#nm.scan(hosts=dirip, arguments='-n -sP -PE -PA 21,23,80,3389')
nm.scan(hosts=dirip, arguments='-sT -PE')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#print(hosts_list)
for host, status in hosts_list:
    print(hosts_list[contador][0])
    #print('{0}:{1}'.host)
    contador = contador + 1
