def hsv_to_Cmyk(h, s, v):
    
    c = v * s
    if(c < 0):
        c = 0
    
    h = ((h / 6.0) / 2)
    x = (c * h)
    if(x < 0):
        x = 0
    
    m = (v - c)
    if(m < 0):
        m = 0
    
    if (0 <= h < 60):
        r, g, b = (c, x, 0)
    elif (60 <= h < 120):
        r, g, b = (x, c, 0)
    elif (120 <= h < 180):
        r, g, b = (0, c, x)
    elif (180 <= h < 240):
        r, g, b = (0, x, c)
    elif (240 <= h < 300):
        r, g, b = (x, 0, c)
    elif (300 <= h < 361):
        r, g, b = (c, 0, x)
      
    r = ((r + m)/100) * 256 
    g = ((g + m)/100) * 256 
    b = ((b + m)/100) * 256
    
    while (r >= 256):
        r -= 1
    while (g >= 256):
        g -= 1
    while (b >= 256):
        b -= 1
    
    print("-------------------------------------------------\n")
    print("-------------------------------------------------\n")
    print("R : ""%2.2f"%(r),"G : ""%2.2f"%(g),"B : ""%2.2f"%(b))
    print("-------------------------------------------------\n")
    print("-------------------------------------------------\n")
    print("-------------------------------------------------\n")
     
    r = r / 256
    g = g / 256
    b = b / 256     
    

     #PARA A DEFINIÇÃO DAS CORES EM CMYK
    k = 1 - max(r, g, b)
    print("%1.2f"%(k))
    c = (1 - r - k)
    print("%1.2f"%(c)) 
    if(c > 0):
        c = c / (1 - k)
        print("%1.2f"%(c))
    else:
        c = 0

    m = (1 - g - k)
    print("%1.2f"%(m))
    if(m > 0):
       m = m / (1 - k)
       print("%1.2f"%(m))   
    else:
        m = 0

    y = (1 - b - k)
    print("%1.2f"%(y)) 
    if(y > 0):
       y = y / (1 - k)
       print("%1.2f"%(y))
    else:
        y = 0
         
     #LISTA COM OS VALORES DEFINIDOS
    
    return "C :""%1.1f"%(c), "M :""%1.1f"%(m), "Y :""%1.1f"%(y), "K :""%1.1f"%(k)

print("----- INFORME O VALOR DE 0 A 100 -----\n")
h = int(input("Informe o valor de H :\n"))
print("----- INFORME O VALOR DE 0 A 1 -----\n")
s = int(input("Informe o valor de S :\n"))
print("----- INFORME O VALOR DE 0 A 1 -----\n")
v = int(input("Informe o valor de V :\n"))

print(hsv_to_Cmyk(h,s,v))   