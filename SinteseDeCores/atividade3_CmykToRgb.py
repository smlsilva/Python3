def cmyk_to_rgb(c, m, y, k):
    r = 255 * ((1 - c) * (1 - k))
    g = 255 * ((1 - m) * (1 - k))
    b = 255 * ((1 - y) * (1 - k))

    rgb = [r, g, b]
    return rgb

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

print(cmyk_to_rgb(c, m, y, k))    