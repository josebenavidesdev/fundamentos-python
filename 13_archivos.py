# with: Nos permite abrir un archivo y luego cerrarlo automaticamente
# r -> leer  w -> escribir  a -> añadir  w+ -> leer y escribir

# LEER
with open("frases.txt", "r") as archivo:
    for linea in archivo:
        print(linea, end="")


# ESCRIBIR
notas = {
    "Gino": 20,
    "Loretto": 17,
    "Talina": 12
}

with open("notas.txt", "w") as archivo:
    archivo.write("***** Notas *****\n")

    for nombre, nota in notas.items():
        archivo.write(f"{nombre}: {nota}\n")


# AGREGAR
nuevas_notas = {
    "Emily": 19,
    "Daniel": 15,
    "Julienne": 13
}

with open("notas.txt", "a") as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(f"{nombre}: {nota}\n")
