val = input("Digite Algo: ")

#USANDO O MÉTODOS
print("O tipo Primitivo desse valor é: ", type(val))
print("Só tem espaço? ", val.isspace())
print("É um Número ", val.isnumeric())
print("É Alfabético ", val.isalpha())
print("É alfanumérico ", val.isalnum())
print("Está em maiuscula ", val.isupper())
print("Está em minuscula ", val.islower())
print("Está capitalizado ", val.istitle())
