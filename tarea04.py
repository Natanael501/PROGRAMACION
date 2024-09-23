###Tarea: Promedios
calif_1 = 10
calif_2 = 7
calif_3 = 4
#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total

print((calif_1*15)/10)
print((calif_2*35)/10)
print((calif_3*50)/10)

###MATRIZ, una matriz es una lista de listas
## matriz = [ [1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13] ]
matriz = [ [1, 1, 1, 3], [2, 2, 2, 6], [3, 3, 3, 9], [4, 4, 4, 12] ]

if matriz[0][3] == matriz[0][0] + matriz[0][1] + matriz[0][2]:
    print('Correcto')

if matriz[1][3] == matriz[1][0] + matriz[1][1] + matriz[1][2]:
    print('Correcto')

if matriz[2][3] == matriz[2][0] + matriz[2][1] + matriz[2][2]:
    print('Correcto')

if matriz[3][3] == matriz[3][0] + matriz[3][1] + matriz[3][2]:
    print('Correcto')
