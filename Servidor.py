#Servidor TCP 
import socket, random , psutil, pickle
from memoria import mostrar_uso_memoria
from cpu import mostrar_uso_cpu
from disco import mostrar_uso_disco
from sistema import system
from tp5 import dataDirLayout, dataPidLayout
from tp6 import backDatatp6
from tp7 import backDataTp7, infonet_pid

def mostrar_info_rede():
    uso_rede = []
    net = psutil.net_if_addrs()
    ipv6 = "IPV6: {}".format(net["Ethernet"][2].address)
    address_fisico ="Endereço Físico: {}".format(net["Ethernet"][0].address)
    ipv4 = "IPV4: {}".format(net["Ethernet"][1].address)   
    uso_rede.append(ipv6)
    uso_rede.append(address_fisico)
    uso_rede.append(ipv4)
    return uso_rede

#Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() #Nome do servidor
porta = 9999 # Porta do servidor
#Realiza o bind (ligação) do IP e porta com o servidor 
socket_servidor.bind((host, porta))
#Escutando ......
socket_servidor.listen()
print("Servidor", host.upper(), "esperando conexão na porta", porta)
#Aceita a conexão do Cliente
(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a ", str(addr))
while True:
    msg = socket_cliente.recv(102400) #Recebe a mensagem do cliente 
    
    if (msg.decode("UTF-8") == "$"):
        print("Termino da conexão")
        socket_cliente.close()
        break
    elif(msg.decode("UTF-8") == "1"):
        dados = mostrar_uso_memoria()
        print("funcionando")
    elif(msg.decode("UTF-8") == "2"):
        dados = mostrar_uso_disco()
    elif(msg.decode("UTF-8") == "3"):
        dados = mostrar_info_rede()
    elif(msg.decode("UTF-8") == "4"):
        dados = mostrar_uso_cpu()
    elif(msg.decode("UTF-8") == "5"):
        dados = system()
    elif(msg.decode("UTF-8") == "6"):
        dados = backDatatp6()
    elif (msg.decode("UTF-8") == "7"):
        dados = dataDirLayout()  
    elif(msg.decode("UTF-8") == "8"):
        dados = dataPidLayout()
    elif(msg.decode("UTF-8") == "9"):
        dados = backDataTp7()  
    elif(msg.decode("UTF-8") == "10"):
       dados = infonet_pid()
    elif(msg.decode("UTF-8") == "?"):
        resp = random.randint(0, 1) #Gera numero aleatório de 0 ou 1 
        msg = "Sim\n"
        if(resp == 0):
            msg = "Não\n"
    else:
        msg = "Ok ..." + msg.decode("UTF-8") #Resposta padrão  
    # Converte de lista para bytes
    bytes = pickle.dumps(dados)
    #print(bytes)
    # Envia os bytes
    socket_cliente.send(bytes)
    # Fecha a conexão com o cliente
socket_cliente.close()