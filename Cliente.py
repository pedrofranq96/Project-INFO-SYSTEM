7# Cliente TCP
import socket, sys,pickle, time

host = socket.gethostname() # Endereço do servidor
porta = 9999 # Porta do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket no cliente
try:
    s.connect((host, porta)) # Tenta conexão com o servidor
except Exception as erro:
    print(str(erro))
    sys.exit(1) # Termina o programa

while True: 
    print()
    print("Escolha a opção desejada: ")
    print("1-------------------Memória")
    print("2-------------------Disco")
    print("3-------------------Rede")
    print("4-------------------CPU")
    print("5-------------------Sistema")
    print("6-------------------Subrede e portas disponíveis")
    print("7-------------------Diretórios")
    print("8-------------------Processos")
    print("9-------------------Info Redes")
    print("10-------------------Interfaces de Rede disponíveis")
    print("Para encerrar digite $")
    msg = input("Entre com a opção: ")
    print()
    inicio_func = time.time()
    opcao = msg
    s.send(msg.encode("UTF-8"))    
    msg = s.recv(102400)
    fim_func = time.time()
    tempo = round((fim_func - inicio_func),3)
    #print("mensagem: {}".format(msg))
    # Converte de bytes para lista
    dados = pickle.loads(msg, encoding='utf8')
    if opcao == "7" or opcao == "8":
        print(dados)
        print()
        print("Tempo de execução: {} s.".format(tempo))       
    else:    
        for item in dados:
            print(item)
        print()    
        print("Tempo de execução: {} s.".format(tempo))     
s.close()    

