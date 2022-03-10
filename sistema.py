import platform


def system():
    sys = []
    nomeMaquina = "Nome da máquina: {}".format(platform.node())
    versaoSO = "Versão do SO': {}".format(platform.platform())
    sO = "Sistema Operacional: {}\n".format(platform.system())
    sys.append(nomeMaquina)
    sys.append(versaoSO)
    sys.append(sO)
    return sys