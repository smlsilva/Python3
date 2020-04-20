import random as rd
def rgb_to_hsv(r, g, b):
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
'''
x = rd.randrange(0,256)
y = rd.randrange(0,256)
z = rd.randrange(0,256)
'''

x = 0
y = 0
z = 0

x = int(input("Informe o valor do R: "))
print("--------------------------------")
print("--------------------------------")
y = int(input("Informe o valor de G: "))
print("--------------------------------")
print("--------------------------------")
Z = int(input("Informe o valor de B: "))
print("--------------------------------")
print("--------------------------------")

print(rgb_to_hsv(x, y, z))
