import platform, psutil,cpuinfo

def mostrar_uso_cpu():
    cpu=[]
    info = cpuinfo.get_cpu_info()
    arq ="Arquitetura: {}".format(info["arch"])
    processor ="Processador: {}".format(info["brand_raw"])
    registradores = "Registradores:{} bits". format(info["bits"])
    marca = "Marca do processador: {}".format(platform.processor())
    freq = "Frequencia: {} GHz".format(round(psutil.cpu_freq().current/1000,1))
    nucleos = "Número de núcleos:{}".format( psutil.cpu_count())
    coresF = "Núcleos Físicos: {}".format(psutil.cpu_count(logical=False))
    percentage = psutil.cpu_times_percent(interval=1)
    consumo = "Em uso: {} %".format(percentage.user + percentage.system)
    livre = "Livre: {} %".format(percentage.idle)           
    cpu.append(marca)
    cpu.append(arq)
    cpu.append(processor)
    cpu.append(registradores)
    cpu.append(freq)
    cpu.append(nucleos)
    cpu.append(coresF)
    cpu.append(consumo)
    cpu.append(livre)
    
 
    return cpu

# result = mostrar_uso_cpu()
# for i in result:
#     print(i)
