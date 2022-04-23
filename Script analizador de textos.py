texto = input('Ingresa un texto: ')
print('Ahora vas a decirme 3 letras, a tu gusto.')
letra1 = input('Letra 1: ')
letra2 = input('Letra 2: ')
letra3 = input('Letra 3: ')

print("""
------------
""")

print('Cuantas veces aparece cada una de las letras.')
conteo1 = texto.lower().count(letra1)
conteo2 = texto.lower().count(letra2)
conteo3 = texto.lower().count(letra3)

print(f'La letra {letra1} aparece {conteo1} veces.')
print(f'La letra {letra2} aparece {conteo2} veces.')
print(f'La letra {letra3} aparece {conteo3} veces.')

print("""
------------
""")

print('Cuantas palabras hay a lo largo de todo el texto.')

listexto = texto.split(' ')
wordnum = (len(listexto))
print(f'En el texto hay {wordnum} palabras.')

print("""
------------
""")

print('Cuál es la primera letra del texto y cuál es la última.')
primera = texto[0]
ultima = texto[-1]
print(f'La primera letra del texto es: {primera}.')
print(f'La última letra del texto es: {ultima}.')

print("""
------------
""")

print('Texto del revés.')
print(texto[::-1])

print("""
------------
""")

print('¿Se encuentra la palabra "Python" dentro del texto?')
piton = 'Python'
print(piton.lower() in texto)


print("""
------------
""")

print('¿El número de palabras es par o impar?')

if wordnum % 2 == 0:
    print('El número de palabras del texto es par')
else:
    print('El número de palabras del texto es impar')





