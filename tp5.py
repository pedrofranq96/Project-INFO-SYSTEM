import psutil, os, time, sched
from tabulate import tabulate
from hurry.filesize import size, alternative




layout_diretorios = []
layout_processos = []

def dirFinder():
    lista = os.listdir()
    dic = {}
    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(size(os.stat(i).st_size,system=alternative))
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)
        else:
            dirName = "(DIR) " + i
            dic[dirName] = []
            dic[dirName].append(size(os.stat(i).st_size,system=alternative))
            dic[dirName].append(os.stat(i).st_atime)
            dic[dirName].append(os.stat(i).st_mtime)

    tabela = [["Nome", "Tamanho", "Data criação", "Data modificação"]]
    for arq in dic:
        linha = [arq]
        linha.append(dic[arq][0])
        linha.append(time.ctime(dic[arq][1]))
        linha.append(time.ctime(dic[arq][2]))
        tabela.append(linha)
        linhaRes = tabulate(tabela, headers='firstrow', tablefmt="tsv")
    layout_diretorios.append(f'{linhaRes}')
    #callsSched.append("     (CHAMADA) " + str(time.ctime()) + str(nome))

def mostra_info(pid):
    try:
        p = psutil.Process(pid)
        texto = []
        texto.append(pid)
        texto.append(p.num_threads())
        texto.append(time.ctime(p.create_time()))
        texto.append(round(p.cpu_times().user, 2))
        texto.append(round(p.cpu_times().system, 2))
        texto.append(round(p.memory_percent(), 2))
        rss = round((p.memory_info().rss / (2 ** 20)), 2)
        texto.append(rss)
        vms = round((p.memory_info().vms / (2 ** 20)), 2)
        texto.append(vms)
        exe = p.exe()
        exe = exe.split("\\")
        exe = exe[-1]
        texto.append(exe)
        #print(texto)
        return texto
    except:
        pass

def pidFinder():
    tabela = []
    lista_pids = psutil.pids()
    cont = 0
    for pid in lista_pids:
        texto = mostra_info(pid)
        if (texto != None):
            tabela.append(texto)
            if (cont == 20):
                break
        cont += 1
    linhaRes = tabulate(tabela, headers='firstrow', tablefmt="tsv")    
    layout_processos.append(f'{linhaRes}')
    #callsSched.append("     (CHAMADA) " + str(time.ctime()) + str(nome))
    



def dataDirLayout(): # diretorio
    dirFinder()
    for i in layout_diretorios:
        return i 

def dataPidLayout(): # processo
    pidFinder() 
    for i in layout_processos:
        return i