mening_info = "Bu Iftixorning do'sti"

print(mening_info)

# Bo'laklash

print(mening_info[0:2]) # Bu
print(mening_info[3:14]) # Iftixorning
print(mening_info[15:21]) # do'sti
print('------------------------------')

print(mening_info[:20])
print(mening_info[10:])
print(mening_info[-5:3])
print('------------------------------')

print(len(mening_info))
print('------------------------------')

matn = "mening ismim Iftikhor"
print(matn.lower())
print('------------------------------')


matn2 = "men Javascriptni o'rganayabman"
matn2_new = matn2.replace("Javascriptni", "Pythonni")
print(matn2_new)

print('--------------Split----------------')
matn3 = "Men mohirfestda umumiy dasturlashni o'rganayabman"
print(matn3.split(" "))

print('--------------concatenation----------------')
a = 'salom '
b = 'Iftikhor'
c = a+b
print(c)

# print('--------------Matnni formatlash----------------')
name5 = 'Iftikhor'
age = 21
job = 'Python'

print("I'm {}, I {}, I learn {}".format(name5,age,job))
text = f"Menning ismim {name5}, Menning yoshim {age}, Men {job} o'rganayabman"
print(text)

