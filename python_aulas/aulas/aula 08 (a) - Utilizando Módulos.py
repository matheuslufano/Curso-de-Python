# Curso Python #08 - Utilizando Módulos

#=======================================================================================================================
"""             (Utilizando Módulos)


 Nessa aula, vamos aprender como utilizar módulos
em Python utilizando os comandos import e
from/import no Python. Veja como carregar
bibliotecas de funções e utilizar vários recursos
adicionais nos seus programas utilizando módulos
built-in e módulos externos, oferecidos no Pypi.

há Bibliotecas que ja vem instalado no python e
tambem há como baixar outras milhares de bibliotecas.
nelas podemos importar fuções. (BIBLIOTECAS OU MÓDULOS),
arquivos ".py" que fornece varias funções que pode
ajusar e muito o funcionamento do nosso programa.
Para consutar, use o site

https://docs.python.org/3/library/index.html


----------------Ex. de biblioteca---------------------------------------------------------------------------------------
biblioteca/modulo: math (matematica)
funções:
- ceil: arredondamento pra cima.
- floor: arredondamento pra baixo.
- trunc: trocar número, eliminando apois a virgula.
- pow: potencia (**)
- sqrt: calcular raiz quadrada ou raiz, rute, square, quadrada
- factorial: calculo fatorial.

------MANEIRAS DE IMPORTAR BIBLIOTECAS--------------

"import": A função import, importa toda a biblioteca.
"from math import sqrt": (de matematica importe sqrt)
importa uma função ou mais."""
#digite import e tecle (CTRL + Epaço) para ver a
#quantidade de bibliotecas disponiveis pra usar.


#=======================================================================================================================

#exemplo de como utilizar uma biblioteca.
#-------------importar matematica---------------------------------------------------------------------------------------
import math
num = int(input("digite um número: "))
raiz = math.sqrt(num)
# "math.sqrt(num)" função calculo de raiz quadrada.

print("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))
# ceil--->  "math.ceil()" serve para arredondar p/ cima,
# floor-->  "math.floor()" p/ arredondar pra baixo ou ":.0f"

#obs.: use "." ponto para ver as funções disponives na biblioteca

#<-------------Números aleatorios---------------------------------------------------------------------------------------
import random
num1 = random.randint(1,50)
print("Número aleatorio: ",num1)



#<---------------emoji--------------------------------------------------------------------------------------------------
"""import emoji
print(emoji.emojize("olá, mundo :grinning_face:", use_aliases=True))
print(emoji.emojize('Olá, mundo :terra_Emojis:', language = 'pt' ))
print(emoji.emojize("Eu :grinning_face_with_big_eyes: python", variant="emoji_type"))

import emoji
print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))
"""
#----------from math import---------------------------------------------------------------------------------------------

import math
num2 = int(input('Digite um número: '))
raiz = math.sqrt(num2)
print("A raiz quadrada de {} é igual a {}".format(num,math.ceil(raiz)))

"""
Tipos integrados
Teste de valor de verdade
Operações Booleanas — and, or,not
Comparações
Tipos Numéricos — int, float,complex
Tipos de iterador
Tipos de sequência — list, tuple,range
Tipo de sequência de texto —str
Tipos de sequência binária — bytes, bytearray,memoryview
Definir tipos — set,frozenset
Tipos de mapeamento —dict
Tipos de gerenciador de contexto
Tipos de anotação de tipo — Alias ​​genérico , União
Outros tipos integrados
Atributos Especiais
Limitação de comprimento de conversão de string inteira
Exceções integradas
contexto de exceção
Herdando de exceções internas
classes base
Exceções concretas
Avisos
Grupos de exceção
Hierarquia de exceção
Serviços de processamento de texto
string— Operações de string comuns
re— Operações de expressão regular
difflib— Auxiliares para calcular deltas
textwrap— Quebra e preenchimento de texto
unicodedata— Banco de dados Unicode
stringprep— Preparação de sequência de Internet
readline— Interface de linha de leitura GNU
rlcompleter— Função de conclusão para GNU readline
Serviços de dados binários
struct— Interpretar bytes como dados binários compactados
codecs— Registro de codec e classes base
Tipos de dados
datetime— Tipos básicos de data e hora
zoneinfo— Suporte de fuso horário IANA
calendar— Funções gerais relacionadas ao calendário
collections— Tipos de dados de contêiner
collections.abc— Classes base abstratas para contêineres
heapq— Algoritmo de fila de heap
bisect— Algoritmo de bisseção de matriz
array— Arrays eficientes de valores numéricos
weakref- Referências fracas
types— Criação de tipos dinâmicos e nomes para tipos integrados
copy— Operações de cópia rasas e profundas
pprint— Impressora bonita de dados
reprlibrepr()— Implementação alternativa
enum— Suporte para enumerações
graphlib— Funcionalidade para operar com estruturas semelhantes a gráficos
Módulos Numéricos e Matemáticos
numbers— Classes de base abstratas numéricas
math— Funções matemáticas
cmath— Funções matemáticas para números complexos
decimal— Aritmética de ponto fixo decimal e ponto flutuante
fractions- Números racionais
random— Gerar números pseudo-aleatórios
statistics— Funções estatísticas matemáticas
Módulos de Programação Funcional
itertools— Funções que criam iteradores para um loop eficiente
functools— Funções e operações de ordem superior em objetos chamáveis
operator— Operadores padrão como funções
Acesso a arquivos e diretórios
pathlib— Caminhos do sistema de arquivos orientados a objetos
os.path— Manipulações comuns de nomes de caminho
fileinput— Iterar sobre linhas de vários fluxos de entrada
stat— Interpretação stat()de resultados
filecmp— Comparações de arquivos e diretórios
tempfile— Gerar arquivos e diretórios temporários
glob— Expansão do padrão de nome de caminho de estilo Unix
fnmatch— Correspondência de padrão de nome de arquivo Unix
linecache— Acesso aleatório a linhas de texto
shutil— Operações de arquivo de alto nível
Persistência de dados
pickle— Serialização de objeto Python
copyreg— Registrar picklefunções de suporte
shelve— Persistência do objeto Python
marshal— Serialização interna do objeto Python
dbm— Interfaces para “bancos de dados” Unix
sqlite3— Interface DB-API 2.0 para bancos de dados SQLite
Compactação e arquivamento de dados
zlib— Compressão compatível com gzip
gzip— Suporte para arquivos gzip
bz2— Suporte para compactação bzip2
lzma— Compressão usando o algoritmo LZMA
zipfile— Trabalhe com arquivos ZIP
tarfile— Ler e gravar arquivos compactados tar
Formatos de arquivo
csv— Leitura e gravação de arquivos CSV
configparser— Analisador de arquivo de configuração
tomllib— Analisar arquivos TOML
netrc— processamento de arquivo netrc
plistlib— Gerar e analisar .plistarquivos Apple
Serviços criptográficos
hashlib— Hashes seguros e resumos de mensagens
hmac— Hash com chave para autenticação de mensagem
secrets— Gera números aleatórios seguros para gerenciar segredos
Serviços de sistema operacional genérico
os— Diversas interfaces do sistema operacional
io— Ferramentas básicas para trabalhar com streams
time— Acesso e conversões de tempo
argparse— Analisador para opções de linha de comando, argumentos e subcomandos
getopt— Analisador estilo C para opções de linha de comando
logging— Recurso de registro para Python
logging.config— Configuração de registro
logging.handlers— Manipuladores de registro
getpass— Entrada de senha portátil
curses— Manipulação de terminal para exibições de células de caracteres
curses.textpad— Widget de entrada de texto para programas curses
curses.ascii— Utilitários para caracteres ASCII
curses.panel— Uma extensão de pilha de painéis para maldições
platform— Acesso aos dados de identificação da plataforma subjacente
errno— Símbolos padrão do sistema errno
ctypes— Uma biblioteca de funções estrangeiras para Python
Execução Simultânea
threading— Paralelismo baseado em thread
multiprocessing— Paralelismo baseado em processos
multiprocessing.shared_memory— Memória compartilhada para acesso direto entre processos
o concurrentpacote
concurrent.futures— Iniciar tarefas paralelas
subprocess— Gerenciamento de subprocessos
sched- Agendador de eventos
queue— Uma classe de fila sincronizada
contextvars— Variáveis ​​de contexto
_thread— API de encadeamento de baixo nível
Redes e comunicação entre processos
asyncio— E/S assíncronas
socket— Interface de rede de baixo nível
ssl— Wrapper TLS/SSL para objetos de soquete
select— Aguardando a conclusão da E/S
selectors— Multiplexação de E/S de alto nível
signal— Definir manipuladores para eventos assíncronos
mmap— Suporte a arquivos mapeados em memória
Manipulação de Dados da Internet
email— Um pacote de tratamento de e-mail e MIME
json— Codificador e decodificador JSON
mailbox— Manipular caixas de correio em vários formatos
mimetypes— Mapear nomes de arquivos para tipos MIME
base64— Codificações de dados Base16, Base32, Base64, Base85
binascii— Converter entre binário e ASCII
quopri— Codificar e decodificar dados imprimíveis citados MIME
Ferramentas de processamento de marcação estruturada
html— Suporte para Linguagem de Marcação de Hipertexto
html.parser— Analisador simples de HTML e XHTML
html.entities— Definições de entidades gerais HTML
Módulos de Processamento XML
xml.etree.ElementTree— A API XML do ElementTree
xml.dom— A API do modelo de objeto de documento
xml.dom.minidom— Implementação mínima do DOM
xml.dom.pulldom— Suporte para construção de árvores DOM parciais
xml.sax— Suporte para analisadores SAX2
xml.sax.handler— Classes base para manipuladores SAX
xml.sax.saxutils— Utilitários SAX
xml.sax.xmlreader— Interface para analisadores XML
xml.parsers.expat— Análise rápida de XML usando Expat
Protocolos de Internet e Suporte
webbrowser— Conveniente controlador de navegador da web
wsgiref— Utilitários WSGI e implementação de referência
urllib— Módulos de manipulação de URL
urllib.request— Biblioteca extensível para abrir URLs
urllib.response— Classes de resposta usadas por urllib
urllib.parse— Analisar URLs em componentes
urllib.error— Classes de exceção geradas por urllib.request
urllib.robotparser— Analisador para robots.txt
http— Módulos HTTP
http.client— cliente de protocolo HTTP
ftplib— Cliente de protocolo FTP
poplib— cliente de protocolo POP3
imaplib— Cliente de protocolo IMAP4
smtplib— cliente de protocolo SMTP
uuid— Objetos UUID de acordo com RFC 4122
socketserver— Uma estrutura para servidores de rede
http.server— Servidores HTTP
http.cookies— Gerenciamento de estado HTTP
http.cookiejar— Manipulação de cookies para clientes HTTP
xmlrpc— Servidor XMLRPC e módulos de cliente
xmlrpc.client— Acesso de cliente XML-RPC
xmlrpc.server— Servidores XML-RPC básicos
ipaddress— Biblioteca de manipulação de IPv4/IPv6
Serviços multimídia
wave— Ler e gravar arquivos WAV
colorsys— Conversões entre sistemas de cores
Internacionalização
gettext— Serviços de internacionalização multilingues
locale— Serviços de internacionalização
Estruturas do programa
turtle- Gráficos de tartaruga
cmd— Suporte para interpretadores de comandos orientados a linha
shlex— Análise lexical simples
Interfaces Gráficas de Usuário com Tk
tkinter— Interface Python para Tcl/Tk
tkinter.colorchooser— Diálogo de escolha de cores
tkinter.font— Invólucro de fonte Tkinter
Diálogos do Tkinter
tkinter.messagebox— Prompts de mensagem do Tkinter
tkinter.scrolledtext- Widget de texto rolado
tkinter.dnd- Suporte para arrastar e soltar
tkinter.ttk- Widgets temáticos Tk
tkinter.tix— Widgets de extensão para Tk
PARADO
Ferramentas de desenvolvimento
typing— Suporte para dicas de tipo
pydoc— Gerador de documentação e sistema de ajuda online
Modo de Desenvolvimento Python
Efeitos do modo de desenvolvimento do Python
Exemplo de Aviso de Recurso
Exemplo de erro de descritor de arquivo inválido
doctest— Teste exemplos interativos de Python
unittest— Estrutura de teste de unidade
unittest.mock— biblioteca de objetos fictícios
unittest.mock- começando
2to3 — Tradução automatizada de código Python 2 para 3
test— Pacote de testes de regressão para Python
test.support— Utilitários para o conjunto de testes Python
test.support.socket_helper— Utilitários para testes de soquete
test.support.script_helper— Utilitários para os testes de execução do Python
test.support.bytecode_helper— Ferramentas de suporte para testar a geração correta de bytecode
test.support.threading_helper— Utilitários para testes de rosqueamento
test.support.os_helper— Utilitários para testes de SO
test.support.import_helper— Utilitários para testes de importação
test.support.warnings_helper— Utilitários para testes de avisos
Depuração e Criação de Perfil
Tabela de eventos de auditoria
bdb— Estrutura do depurador
faulthandler— Despeje o rastreamento do Python
pdb— O Depurador Python
Os Perfis do Python
timeit— Medir o tempo de execução de pequenos trechos de código
trace— Rastreie ou rastreie a execução da instrução Python
tracemalloc— Rastrear alocações de memória
Empacotamento e Distribuição de Software
distutils— Construindo e instalando módulos Python
ensurepip— Inicializando o pipinstalador
venv— Criação de ambientes virtuais
zipapp— Gerenciar arquivos zip Python executáveis
Serviços de tempo de execução do Python
sys— Parâmetros e funções específicos do sistema
sysconfig— Fornecer acesso às informações de configuração do Python
builtins- Objetos embutidos
__main__— Ambiente de código de nível superior
warnings- Controle de alerta
dataclasses— Classes de dados
contextlib— Utilitários para withcontextos de declaração
abc— Classes base abstratas
atexit— Manipuladores de saída
traceback— Imprima ou recupere um rastreamento de pilha
__future__— Definições de declarações futuras
gc— Interface do coletor de lixo
inspect— Inspecionar objetos vivos
site— Gancho de configuração específico do site
Interpretadores Python personalizados
code— Classes base do intérprete
codeop— Compilar código Python
Importando Módulos
zipimport— Importar módulos de arquivos Zip
pkgutil— Utilitário de extensão de pacote
modulefinder— Encontrar módulos usados ​​por um script
runpy— Localizando e executando módulos Python
importlib- A implementação deimport
importlib.resources- Recursos
Funções obsoletas
importlib.resources.abc– Classes base abstratas para recursos
Usandoimportlib.metadata
A inicialização do sys.pathcaminho de pesquisa do módulo
Serviços de Linguagem Python
ast— Árvores de sintaxe abstrata
symtable— Acesso às tabelas de símbolos do compilador
token— Constantes usadas com árvores de análise Python
keyword— Teste de palavras-chave Python
tokenize— Tokenizer para fonte Python
tabnanny— Detecção de indentação ambígua
pyclbr— Suporte ao navegador do módulo Python
py_compile— Compilar arquivos fonte do Python
compileall— Bibliotecas Python de compilação de bytes
dis— Desmontador para bytecode Python
pickletools— Ferramentas para desenvolvedores de picles
Serviços Específicos do MS Windows
msvcrt— Rotinas úteis do tempo de execução do MS VC++
winreg— Acesso ao registro do Windows
winsound— Interface de reprodução de som para Windows
Serviços específicos do Unix
posix— As chamadas de sistema POSIX mais comuns
pwd— O banco de dados de senhas
grp— O banco de dados do grupo
termios— Controle tty estilo POSIX
tty— Funções de controle do terminal
pty— Utilitários de pseudo-terminal
fcntl— As chamadas de sistema fcntleioctl
resource— Informações de uso de recursos
syslog— Rotinas da biblioteca de syslog do Unix
Módulos Substituídos
aifc— Ler e gravar arquivos AIFF e AIFC
asynchat— Manipulador de comando/resposta de soquete assíncrono
asyncore— Manipulador de soquete assíncrono
audioop— Manipular dados de áudio brutos
cgi— Suporte de interface de gateway comum
cgitb— Gerenciador de rastreamento para scripts CGI
chunk— Ler dados fragmentados IFF
crypt— Função para verificar senhas Unix
imghdr— Determinar o tipo de imagem
imp— Acesse os internos de importação
mailcap— Manipulação de arquivo Mailcap
msilib— Ler e gravar arquivos do Microsoft Installer
nis— Interface para NIS da Sun (Páginas Amarelas)
nntplib— Cliente de protocolo NNTP
optparse— Analisador para opções de linha de comando
ossaudiodev— Acesso a dispositivos de áudio compatíveis com OSS
pipes— Interface para shell pipelines
smtpd— Servidor SMTP
sndhdr— Determinar o tipo de arquivo de som
spwd— O banco de dados de senhas sombra
sunau— Ler e gravar arquivos Sun AU
telnetlib— Cliente Telnet
uu— Codificar e decodificar arquivos uuencode
xdrlib— Codificar e decodificar dados XDR
Considerações de segurança
"""