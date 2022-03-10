import psutil

def mostrar_uso_disco():
    uso_disco = []
    disc = psutil.disk_usage(".")
    total_disc = "Total do disco: {}".format(round(disc.total / pow(2, 30), 2))
    disc_percent = "Porcentagem em uso: " + str(disc.percent) + "%"
    livre = "Livre: {}".format(round(disc.free / pow(2, 30), 0), "GB")
    uso = "Em uso: {}".format(round(disc.used / pow(2, 30), 0), "GB")
    uso_disco.append(total_disc)
    uso_disco.append(disc_percent)
    uso_disco.append(livre)
    uso_disco.append(uso)
    return uso_disco