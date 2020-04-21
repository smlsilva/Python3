import math
def hsv_to_rgb(h, s, v):
    
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
      
    r, g, b = (((r + m)/100) * 255, ((g + m)/100) * 255, ((b + m)/100) * 255)
    
    while (r >= 256):
        r -= 1
    while (g >= 256):
        g -= 1
    while (b >= 256):
        b -= 1

    return "R :""%3.0f"%(r), "G :""%3.0f"%(g), "B :""%3.0f"%(b)

print("----- INFORME O VALOR DE 0 A 100 -----\n")
h = int(input("Informe o valor de H :\n"))
s = int(input("Informe o valor de S :\n"))
v = int(input("Informe o valor de V :\n"))

print(hsv_to_rgb(h,s,v))    