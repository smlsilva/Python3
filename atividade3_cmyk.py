import random 

print("-------------------------------------------")
print("INFOME QUAL OPERAÇÃO VOCÊ DESEJA REALIZAR!")
print("-------------------------------------------")
print("MODO INTERATIVO - Digite 1 \n")
print("MODO AUMÁTICO - Digite 2 \n")
print("-------------------------------------------")    

opcao = int(input("Informe o Modo desejado : "))
while((opcao >= 3) or (opcao == 0)):
    opcao = int(input("Informe o Modo desejado : "))    
    
if(opcao == 1):
    
    r = -1
    g = -1
    b = -1

    while((r < 0) or (r > 255) or (g < 0) or (g > 255) or (b < 0) or (b > 255)):
        print("INFORME O VALOR ENTRE 0 e 255 \n")
        print("---------------------")
        print("---------------------")
        r = float(input("Digite o valor de R :"))
        print("---------------------")
        g = float(input("Digite o valor de G :"))
        print("---------------------")
        b = float(input("Digite o valor de B :"))
        print("---------------------")
        print("----------------------")
        
        if(((r >= 0) or (r <= 255) or (g >= 0) or (g <= 255) or (b >= 0) or (b <= 255))):
            #IRA FAZER A DIVISAO POR 255, PARA GERAR UM NUMERO ENTRE 0 E 1 
            r = r / 255
            print(r)
            g = g / 255
            print(g)
            b = b / 255
            print(b)        
            #CONDICAO PARA ARREDONDAMENTO
            if(r > 0.5):
                round(r + 0.5)
                round(r,0)
                print(r)
            elif(r < 0.5):
                round(r - 0.5)
                round(r,0)
                print(r)
            elif(g > 0.5):
                round(g + 0.5)
                round(g,0)
                print(g)
            elif(g < 0.5):
                round(g - 0.5)
                round(g,0)
                print(g)
            elif(b > 0.5):
                round(b + 0.5)
                round(b,0)
                print(b)
            elif(b < 0.5):
                round(b - 0.5)
                round(b,0)
                print(b)        
            #DEFINIÇÃO DE CASAS DECIMAIS (RGB)   
            r = round(r,0)
            g = round(g,0)
            b = round(b,0)
            

            #PARA A DEFINIÇÃO DAS CORES EM CMYK
            k = 1 - max(r,g,b)
            c = ((1 - r - k) / (1 - k))
            m = ((1 - g - k) / (1 - k))
            y = ((1 - b - k) / (1 - k))
                
            #DEFINIÇÃO DE CASAS DECIMAIS (CMYK)
            k = round(k,0)
            c = round(c,0)
            m = round(m,0)
            y = round(y,0)
    
            #LISTA COM OS VALORES DEFINIDOS
            print("---------------------\n")
            print("----------------------\n")
            cmyk = [k,c,m,y]
            print("CMYK {} :".format(cmyk))

elif(opcao == 2):
    
    #GERA UM NUMERO ALEATORIO ATE 255
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    
    cor = [r,g,b] #IRA FAZER UMA LISTA COM OS NUMEROS GERADOS
    print(cor)
     
    #IRA FAZER A DIVISAO POR 255, PARA GERAR UM NUMERO ENTRE 0 E 1 
    r = r / 255
    g = g / 255
    b = b / 255
    
    #CONDICAO PARA ARREDONDAMENTO
    if(r > 0.5):
        round(r + 0.5)
    elif(r < 0.5):
        round(r - 0.5)
    elif(g > 0.5):
        round(g + 0.5)
    elif(g < 0.5):
        round(g - 0.5)
    elif(b > 0.5):
        round(b + 0.5)
    elif(b < 0.5):
        round(b - 0.5)        

    #DEFINIÇÃO DE CASAS DECIMAIS (RGB)   
    r = round(r,0)
    g = round(g,0)
    b = round(b,0)
    
    #PARA A DEFINIÇÃO DAS CORES EM CMYK
    k = 1 - max(r,g,b)
    c = ((1 - r - k) / (1 - k))
    m = ((1 - g - k) / (1 - k))
    y = ((1 - b - k) / (1 - k))
    
    #DEFINIÇÃO DE CASAS DECIMAIS (CMYK)
    k = round(k,0)
    c = round(c,0)
    m = round(m,0)
    y = round(y,0)
    
    #LISTA COM OS VALORES DEFINIDOS
    cmyk = [k,c,m,y]
    print("CMYK {} :".format(cmyk))
