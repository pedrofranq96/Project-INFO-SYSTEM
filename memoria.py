import psutil

def mostrar_uso_memoria():
    memory = []
    mem = psutil.virtual_memory()
    total = "Total de memória: {} GB".format(round(mem.total / pow(2, 30),1))
    disponivel= "Memória disponível: {} GB".format(round(mem.available / pow(2, 30),1)) 
    percentualMemoria= "Percentual de mem. utilizado: {} %".format( mem.percent)
    usada ="Memória utilizada: {} GB".format(round(mem.used / pow(2, 30),1))
    livre = "Memória livre: {} GB".format(round(mem.free / pow(2, 30),1))
    memory.append(total)
    memory.append(disponivel)
    memory.append(percentualMemoria)
    memory.append(usada)
    memory.append(livre)
    return memory