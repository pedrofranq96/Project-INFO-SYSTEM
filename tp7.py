from psutil import net_if_addrs
import socket, netifaces, psutil, json
from psutil import net_connections
import tabulate

informacao = net_if_addrs()
IP = socket.gethostbyname(socket.gethostname())
porta = netifaces.gateways()

dataTp7 = []
interTp7 = []
#1
def infos():
    dataTp7.append("IP:" + str(IP))
    dataTp7.append("Mascara de subrede:" + str(informacao["Ethernet"][1][2]))
    dataTp7.append("Gateway: " + str(porta["default"][2][0]))
infos()    

#2
def rede():
    informacaoRede = psutil.net_io_counters()
    dataTp7.append("Bytes enviados: " + str(informacaoRede[0]))
    dataTp7.append("Bytes recebidos: " + str(informacaoRede[1]))
    dataTp7.append("Pacotes enviados: " + str(informacaoRede[2]))
    dataTp7.append("Pacotes recebidos: " + str(informacaoRede[3]))
    dataTp7.append("Erros ao receber: " + str(informacaoRede[4]))
    dataTp7.append("Erros ao enviar: " + str(informacaoRede[5]))
    dataTp7.append("Pacotes recebidos descartados: " + str(informacaoRede[6]))
    dataTp7.append("Pacotes enviados descartados: " + str(informacaoRede[7]))
rede()    

#3

def InternetProtocol(ips):
    if(ips == socket.AF_INET):
        return ("IPV4")
    elif(ips == socket.AF_INET6):
        return ("IPV6")
    elif (ips == socket.AF_UNIX):
        return ("UNIX")
    else: 
        return ("-")


def infonet_pid():
    informacao = []
    for process in net_connections(kind='inet'):
        informacao.append("Tipo de Endereco: " + str(InternetProtocol(process[1])))
        informacao.append("IP Local: " + str(process[3][0]))
        informacao.append("Porta: " + str(process[3][1]))
        
    return informacao


#print(infonet_pid()) 
    
def backDataTp7():
  return dataTp7 







