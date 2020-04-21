def cmyk_to_hsv(c, m, y, k):
    r = 255 * ((1 - c) * (1 - k))
    g = 255 * ((1 - m) * (1 - k))
    b = 255 * ((1 - y) * (1 - k))
     
    print(r, g, b) 

    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r,g,b)
    
    cmin = min(r,g,b)
    
    dt = cmax - cmin
    
    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b)/dt) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r)/dt) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g)/dt) + 240) % 260
    if cmax == 0:
        s = 0
    else:
        s = (dt/cmax)*100
    v = cmax * 100          
    return h, s, v

c = float(input("INFORME O VALOR ENTRE 0 e 1 (C): \n"))
while((c < 0) or (c > 1)):
    c = float(input("INFORME O VALOR ENTRE 0 e 1 : \n"))

m = float(input("INFORME O VALOR ENTRE 0 e 1 (M): \n"))
while((m < 0) or (m > 1)):     
    m = float(input("INFORME O VALOR ENTRE 0 e 1 : \n")) 

y = float(input("INFORME O VALOR ENTRE 0 e 1 : (Y)\n"))
while((y < 0) or (y > 1)):
    y = float(input("INFORME O VALOR ENTRE 0 e 1 : \n"))

k = float(input("INFORME O VALOR ENTRE 0 e 1 : (K)\n"))
while((k < 0) or (k > 1)):
    k = float(input("INFORME O VALOR ENTRE 0 e 1 : \n"))

print(cmyk_to_hsv(c, m, y, k))