# list = ['behi', 'anor', 'anjir', 'shaftoli', 'uzum', 'olma', 'olcha']
# print(list[0:2])

# list[1] = 'banan'
# print(list)


# list.append('meva')
# print(list)

# list.insert(3, 'mevalar')
# print(list)

# mevalar = ['apelsin', 'limon', 'mandarin']
# list.extend(mevalar)
# print(list)

# ma'lumotlarni o'chirish
# list.remove('behi')
# print(list)

# index bilan o'chirish
# list.pop(5)
# print(list)

# butunlay o'chirish
# del mevalar
# print(mevalar)


# hammasini tozalash
# list.clear()
# print(list)


# names = ['iftikhor', 'farrukh', 'elbek', 'jasur','nodir']

# count = 1

# for ism in names:
#     print(f"{count}-{ism}")
#     count = count + 1 

# [print(ism) for ism in names]

# orqaga qaytarish
# names.sort(reverse=True)
# print(names)

raqamlar = [10,20,40,88,66,100,853,445,862,4]
raqamlar.sort()
raqamlar[5] = 10
print(raqamlar)

raqamlar2 = raqamlar 
raqamlar[1] = 100
print(raqamlar2)


raqamlar3 = raqamlar.copy()
raqamlar[1] = 258
print(raqamlar)

raqamlar5 = list(raqamlar)
print(raqamlar5)

raqamlar10 = [123,321,10,10]

final = raqamlar+raqamlar10
print(final)