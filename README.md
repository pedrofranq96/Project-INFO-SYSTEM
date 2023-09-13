# Documentação do Sistema "INFO-SYSTEM"

O "INFO-SYSTEM" é uma aplicação desenvolvida em Python que permite aos usuários coletar informações importantes sobre o sistema operacional Windows em que estão usando. Esta ferramenta é útil para obter informações detalhadas sobre a configuração do sistema, como memória (RAM), CPU, rede, protocolos, threads, status da rede Wi-Fi, uso de disco e informações sobre a cache.

## Requisitos Prévios

Antes de começar a usar o "INFO-SYSTEM", certifique-se de que você possui os seguintes requisitos prévios em sua máquina:

- Python instalado (versão 3.6 ou superior).
- Acesso de administrador ou permissões elevadas para executar algumas consultas no sistema.

## Instalação

Siga os passos abaixo para instalar e usar o "INFO-SYSTEM" em sua máquina Windows:

### Passo 1: Clonar o Repositório

Clone o repositório do "INFO-SYSTEM" para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/info-system.git
```

Substitua `seu-usuario` pelo seu nome de usuário no GitHub, se necessário.

### Passo 2: Instalar Dependências

Navegue até o diretório do projeto "INFO-SYSTEM" e instale as dependências usando o comando:

```bash
pip install -r requirements.txt
```

### Passo 3: Executar o Sistema

Após a instalação das dependências, execute o "INFO-SYSTEM" com o seguinte comando:

```bash
python info_system.py
```

## Utilizando o "INFO-SYSTEM"

O "INFO-SYSTEM" fornece uma interface de linha de comando simples para coletar informações do sistema. Você pode interagir com o sistema de duas maneiras:

1. **Opções de Comando**:

   O "INFO-SYSTEM" oferece várias opções de comando para coletar informações específicas. Por exemplo, para coletar informações sobre a CPU, você pode usar o comando:

   ```bash
   python info_system.py --cpu
   ```

   Consulte o menu de ajuda ou o README do projeto para obter uma lista completa de opções de comando disponíveis.

2. **Menu Interativo**:

   Você também pode usar o "INFO-SYSTEM" no modo interativo, onde você pode navegar pelas opções e coletar informações específicas do sistema.

   ```bash
   python info_system.py --interactive
   ```

   O menu interativo permite escolher as informações que deseja coletar a partir de um menu.

## Informações Disponíveis

O "INFO-SYSTEM" pode coletar uma variedade de informações sobre o sistema operacional Windows, incluindo:

- Memória (RAM): Informações sobre a memória RAM disponível e em uso.
- CPU: Detalhes sobre a CPU, incluindo modelo, velocidade e número de núcleos.
- Rede: Informações sobre a configuração de rede, incluindo endereço IP e gateway padrão.
- Protocolos: Lista de protocolos de rede habilitados.
- Threads: Informações sobre threads em execução no sistema.
- Wi-Fi: Status e informações sobre redes Wi-Fi disponíveis.
- Disco: Uso de disco, incluindo espaço disponível e total em unidades de disco.
- Cache: Informações sobre a cache do sistema.

## Notas Finais

O "INFO-SYSTEM" é uma ferramenta útil para coletar informações detalhadas sobre o sistema operacional Windows. Este projeto é uma demonstração de como Python pode ser usado para acessar informações do sistema.

Lembre-se de que o "INFO-SYSTEM" pode exigir permissões elevadas para acessar algumas informações do sistema. Certifique-se de executar a ferramenta com privilégios de administrador ou permissões adequadas.

Para obter informações detalhadas sobre o uso da ferramenta e as opções de comando, consulte o README do projeto ou use a opção de ajuda fornecida pela ferramenta.

Para qualquer dúvida ou problema específico relacionado ao "INFO-SYSTEM," consulte o código-fonte ou entre em contato com o desenvolvedor do projeto. Divirta-se explorando as informações do seu sistema operacional!

