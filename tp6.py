import os, subprocess, platform, nmap
dataTp6 = []
def retorna_ping(host):
    plataforma = platform.system()
    if (plataforma == "Windows"):
        args = ["ping", "-n", "1", "-l", "1", "-w", "1000", host]
    else:
        args = ["ping", "-c", "1", "-W", "1", host]
    retorno = subprocess.call(args, stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))
    return retorno
def procurando_hosts(base_ip):
    #dataTp6.append("Procurando...")
    host_validos = []
    for i in range(1, 20):
        if ((i % 5) == 0):
            print(".", end="")
        ip = base_ip + str(i)
        retorno = retorna_ping(ip)
        if (retorno == 0):
            host_validos.append(ip)
    return host_validos

def obter_hostnames(host_validos):
    nm = nmap.PortScanner()
    try:
        nm.scan(host)
        dataTp6.append("IP " + str(host) + "possui o nome " + str(nm[host].hostname()))
    except:
        pass
        #dataTp6.append("Erro:" + str(host))
        
def scan_host(host):
    nm = nmap.PortScanner()
    nm.scan(host)
    dataTp6.append(str(nm[host].hostname()))
    for proto in nm[host].all_protocols():
        print("-----------------------------")
        dataTp6.append("Protocolo: " + str(proto))
        lport = nm[host][proto].keys()
        for port in lport:
            dataTp6.append("Porta " + str(port) + " Estado " + str(nm[host][proto][port]["state"]))

ip_string = "192.168.0.172"
ip_lista = ip_string.split(".") 
base_ip = ".".join(ip_lista[0:3]) + "." 
dataTp6.append("\nTestar os IPs da subrede:" + str(base_ip) + "0") 
host_validos = procurando_hosts(base_ip)
dataTp6.append("Hosts válidos:" + str(host_validos))
for host in host_validos:
    obter_hostnames(host)
    scan_host(host)   


def backDatatp6():
    return dataTp6
