#dados comuns ou basicos
nome = input("nome: ").strip().lower()
snome = input("sobrenome: ").strip().lower()
nick = input("apelido: ").strip().lower()
birth = input("data de nascimento: ").strip().lower()

#opcoes simples
comuns = input("usar senhas mais comuns(S/N)?: ").strip().lower()
anos = input("combinar com anos?(S/N): ").strip().lower()
maiusculas = input("usar combinacao com maiusculas(EXEMPLO)(S/N): ").strip().lower()

#opcoes compostas
palavras_chaves = input("adicionar palavras-chave?(S/N): ").strip().lower()
if palavras_chaves == "s":
    key = input("adicione as palavras-chave separadas por virgula\n---> ").split(",")
ordem_de_escolha = input("escolher ordem de escrita?(S/N): ").strip().lower()
if ordem_de_escolha == "s":
    ordem = input("escolha a ordem:\n\
[1]---Basicas | [2]---Chaves | [3]---Comuns | [4]---Maiusculas | [5]---Anos\n\
separadas por virgula: ").split(",")
    
#string que sera usada para armazenar a escrita antes de ser gravada
# finalmente na wordlist
STRING = ""

# funcao basica que ira nas compostas
def combo(x,y,repetir="s"):
    global STRING
    if x!="" and y!="" and x!=y and repetir == "s":
        STRING += f"{x}{y}\n{y}{x}\n"
    elif x!="" and y!="" and x!=y:
        STRING += f"{x}{y}\n"

def Basica():
    global STRING
    combo(nome,snome);combo(nome,nick);combo(snome,nick)
    if birth!="" and len(birth) == 8:
        STRING += f"{birth}\n"
        combo(nome,birth[:4]);combo(snome,birth[:4]);combo(nick,birth[:4])
        combo(nome,birth[4:]);combo(snome,birth[4:]);combo(nick,birth[4:])

def Chaves():
    if palavras_chaves == "s":
        for x in key:
            combo(x,nome);combo(x,snome);combo(x,nick)
            if len(birth) == 8:
                combo(x,birth[:4])
                combo(x,birth[4:])
        for x in key:
            for y in key[::-1]:
                combo(x,y,"n")

def Anos():
    if anos == "s":
        for year in range(2000,2025):
            combo(nome,year);combo(snome,year);combo(nick,year)
    if palavras_chaves == "s":
        for x in key:
            for year in range(2000,2025):
                combo(x,year,"n");combo(year,x,"n")

def Comuns():
    global STRING
    STRING += "admin\n12345\n123456\n12345678\n123456789\n12345678910\npassword\
\n1234567890\nsenha123\nmudar123\nadmin123\nuser\nUNKNOWN\nPassword\n"

def Maiusculas():
    if maiusculas == "s":
        combo(nome.upper(),snome);combo(nome,snome.upper());combo(nome.upper(),snome.upper())
        combo(nome.upper(),nick);combo(nome,nick.upper());combo(nome.upper(),nick.upper())
        combo(snome.upper(),nick);combo(snome,nick.upper());combo(snome.upper(),nick.upper())
        if palavras_chaves == "s":
            for x in key:
                combo(x,nome.upper());combo(x,snome.upper());combo(x,nick.upper())
                combo(x.upper(),nome);combo(x.upper(),snome);combo(x.upper(),nick)
                combo(x.upper(),birth[:4]);combo(x.upper(),birth[4:])
            for x in key:
                for y in key[::-1]:
                    combo(x.upper(),y,"n")
                    combo(x,y.upper(),"n")
                    combo(x.upper(),y.upper(),"n")
        if anos == "s":
            for year in range(2000,2025):
                combo(nome.upper(),year);combo(snome.upper(),year);combo(nick.upper(),year)
        if anos == "s" and palavras_chaves == "s":
            for x in key:
                for y in range(2000,2025):
                    combo(x.upper(),y)
                    
wl_nome = input("qual o nome da wordlist?: ")+".txt".lower().strip()
if wl_nome != ".txt":
    dicionario = open(wl_nome,"w")
else:
    print("\n"*99+"cancelado por nome vazio")
    exit()

#ORDEM EXECUCAO
dicio = {"1":"Basica()","2":"Chaves()","3":"Comuns()","4":"Maiusculas()","5":"Anos()"}
if ordem_de_escolha == "s":
    for x in ordem:
        exec(dicio[x])
    if len(ordem)<5:
        for x in ordem:
            del dicio[x]
        for x in dicio.values():
            exec(x)
else:
    for x in dicio.values():
        exec(x)


#escrita
dicionario.write(STRING)
dicionario.close()
print("\n"*99)
print(f"{wl_nome} foi criado com sucesso!!!")
