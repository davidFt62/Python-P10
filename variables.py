# l' opérateur d'affectation = permet d'injecter une valeur


# integer, nombre entier

my_number1 = 123
my_number2 = -42
print (type(my_number1))

print (my_number1)
print (my_number2)

# float, nombre à virgule flottante

my_number3 =3.14
my_number4 = -2.71
my_number5 = 0.0
print (type(my_number3))

print (my_number3)
print (my_number4)
print (my_number5)

# bool, booolée
my_boolean1 = True
my_boolean2 = False

print (my_boolean1)
print (my_boolean2)
print (type(my_boolean1))

# None, valeur nulle ou null ou nil
my_none = None
print(type(my_none))


#string, chaîne de caractères
# double quote ou simple quote, c'est pareil
my_text1 = "Ceci est une chaîne de caractères"
my_text2 = "Ceci est aussi une chaîne de caractères"

print (my_text1)
print (my_text2)
print (type(my_text2))


#\ caractère d'échappement
#\ n saut de ligne
my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "John \"Foo \"Doe"
my_text6= """abc
def
ghi"""
my_text7 = '''abc
def
ghi'''
print (my_text3)
print (my_text4)
print (my_text5)
print (my_text6)
print (my_text7)

# ctrlf: Win ( \r\n)/ ef:linux (\n) / cr: macos (\r))

a=123
b=42
# permutation de la valeur

a,b=b,a
print (a, b)

a=42
b=123
c=123

#variante uniquement valable avec des nombres
c = a+b
a = c-a
b = c-b

print(a, b)

# + addition
foo = 123 + 42
foo = foo + 42
# écriture simplifier foo += 42 au lieu de foo = foo + 42

print (foo)

# / division
foo = 123 / 42
foo /= 42
print (foo)
print (type(foo))

# //division
foo = 123 // 42
foo //= 42
print (foo)
print (type(foo))

# % modulo


# * multiplication
# ** puissance

foo = 2 ** 6
print (foo)
my_text1 = "Ceci est une chaine de caractères"
my_text2 = 'Ceci est une chaine de caractères'

print (my_text1)
print (my_text2)


# = affectation
# + addition
# - soustraction
# / division
# // division entière
# % modulo
# * multiplication
# ** puissance
# ^ puissance mais pas en python
# @TODO

foo = "123"
# str vers int
foo = int (foo)
print (foo)
print(type((foo)))

foo = "123"
# str float
foo = float (foo)
print(type(foo))

foo = 3.14
# float vers str
foo = str(foo)
print(type(foo))

foo = 2.712333
# récuperer la partie entière (c-à-d_2)
a= int(foo)
# récupérer la partie aprés les virgules (c-à-d 0.71)
b= foo-a
print (a)
print (b)

foo= 0.2+0.1
print (foo)


