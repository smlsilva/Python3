import requests
from bs4 import BeautifulSoup

def sites(escolha):

    urls = ["","https://github.com", "https://sci-hub.tw","https://www.fbi.gov"] #Sites pré-definidos

    page = requests.get(urls[escolha])#REQUESTS PEGA A URL DE DETERMINADA POSISÇÃO NA LISTA
    print(page.status_code)#CODIGO DE STATUS_DA_PAGINA
    soup = BeautifulSoup(page.content, 'lxml')    
    
    escrita = open("Site.txt", 'w')#pega o site e passa o html para um TXT  
    escrita.write(page.text)#Método para incluir o HTML da página
    escrita.close()#Funcion for close the file txt
    
    buscar = input("Você gostaria de fazer alguma pesquisa ? Sim / Não \n")
    if(buscar == "Sim"):
        soup = BeautifulSoup(page.content, 'lxml')
        bs = input("Informe a tag HTML para buscar o conteúdo : \n")
        print(soup.find_all(bs))

    elif(buscar == "Não"):
        print(soup)
    

    sucess = "Sucesso"
    return sucess
    
def Informe(seusite):

    url = ["https://" + seusite]
    
    
    page = requests.get(url[0])
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'lxml')
    
    escrita = open("Site.txt", 'w')  
    escrita.write(page.text)
    escrita.close()
    
    buscar = input("Você gostaria de fazer alguma pesquisa ? Sim / Não \n")
    if(buscar == "Sim"):
        soup = BeautifulSoup(page.content, 'lxml')
        bs = input("Informe a tag HTML para buscar o conteúdo : \n")
        print(soup.find_all(bs))

    elif(buscar == "Não"):
        print(soup)
    
    sucess = "Sucesso"
    return sucess     

print("---------APS-2020----------")
print("--------VERSÃO 2.0---------")
print("-------WEB - CRAWLER-------\n")

escolha = input("Digite (Sim) para entrar no programa ou informe (Sair) para sair :\n ")
if(escolha == "Sim"):    
    if(escolha == "Sim"):
        print("-----------------------------")
        print("1 - Site do Github \n")
        print("2 - Site do SCI-HUB (ARTIGOS CIENTÍFICOS) \n")
        print("3 - Site do FBI\n")
        print("4 - Para digitar o seu site pressione (4)")
        print("-----------------------------")
        escolha = input("Coloque o Número de sua escolha ou\n Caso queira sair digite (Sair):\n")
        if(escolha == "1"):
            opcao = 1         
            print(sites(opcao))
        elif(escolha == "2"):
            opcao = 2
            print(sites(opcao))
        elif(escolha == "3"):
            opcao = 3
            print(sites(opcao))    
        elif(escolha == "4"):
            print("---INFORME O NOME DO SITE--- ")
            seusite = input("Informe o nome do seu site para fazer a busca : ")
            print(Informe(seusite))
        elif(escolha == "Sair"):
            print("Tchau")
        else:
            print("\nDigitos Incorretos!")
            print("Programa encerrado!\n")    
    
elif(escolha == "Sair"):
    print("Tchau")

elif(escolha == "1","2","3","4","5","6","7","8","9","0"):
    print("Digito(s) incorreto(s)!") 

            