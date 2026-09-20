import os

print(os.getcwd()) #use esse comando para descobrir em qual diretório você está 

os.chdir(r"seu caminho aqui") #use esse comando para mudar para o caminho do diretório onde você quer utilizar o organizador

lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)] 
#faz uma compreensão de lista (list comprehension) onde lista todos os arquivos e pastas existentes no diretório, 
#através do if utilizado o comando só trará os arquivos e vai ignorar as pastas
#como os arquivos aceitam que as extensões possam ser escritas em maiúsculas como TXT e o Python é case sensitive usamos o .lower() para colocar todas letras dos nomes dos arquivos em minúsculas
#por fim, passamos o resultado para uma variável chamada lista_arquivos


lista_tipos = {tipo.split('.')[-1] for tipo in lista_arquivos}
#transforma em conjunto, pois pode haver várias extensões .txt ou de outros tipo então para não fazer várias pastas com o mesmo nome usa-se um conjunto por que não se pode repetir elementos nele (faz um set comprehension, utilize as chaves {})
#faz a separação das palavras, obtidas na variável lista_arquivos, através de um delimitador. Neste caso, utilizamos o "." e o [-1] para pegar apenas o último índice que é a extensão
#por fim, o resultado é passado para a variável lista_tipos

for tipo in lista_tipos:
    if os.path.exists(tipo): #averigua se o caminho (pasta) já existe, caso sim ele apenas passa. Facilita para não dar erro
        pass
    else:
        os.mkdir(tipo) #caso o contrário, ele cria uma pasta para cada nome de extensão existente na lista_tipos

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1] #ele pega somente a extensão do arquivo e joga para a pasta_destino
    de = os.path.join(os.getcwd(), arquivo)#junta os caminhos do diretório atual e o do arquivo. Caso esteja no downloads, ficará algo como esse exemplo: c:\\Users\\Helena\\Downloads\\nome-do-arquivo
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)#junta o caminho do diretório atual com a pasta_destino (que são os nomes das extensões) e o nome do arquivo                                 
    if os.path.exists(de): #caso o caminho exista, mude o arquivo de lugar, então se um arquivo .txt está no downloads ele será colocado na pasta de destino (a pasta que está nomeada como txt)
        os.replace(de, para)