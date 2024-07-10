'OPERADORES LÓGICOS'

'''
- AND (&, and)
- OR (|, or)
- NOT (not)
'''

'''Operador AND
True & True = True
False and True = False'''

#Ejemplos
expresion = True and False & True 
print("El valor es {}".format(expresion))

expresion = (True & False) and (True & True)
print("El valor es {}".format(expresion))

'''Operador OR
False | False = False
True or False = True'''

expresion = True | False or False
print("El valor es {}".format(expresion))

expresion = ((True and True) | (False & False)) and (True or False)
print("El valor es {}".format(expresion))

'''Operador NOT
not True = False
not False = True'''

expresion = not True
print("El valor es {}".format(expresion))

expresion = ((True & (not False)) | ((not True) | (not False)))
print("El valor es {}".format(expresion))

#Expresion combinada
expresion = (((True | True) and (not(True & False | True)) | (not(True & False)) | True))
print("El valor es {}".format(expresion))