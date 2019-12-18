import numpy as np

np.set_printoptions(precision=2, suppress=True)

# # Варинат 1
# text = 9192
# N = 10573
# e = 8483

# # Варинат 2
# text = 3688
# N = 10807
# e = 1359

# # Варинат 36
# text = 6529
# N = 12319
# e = 5021

# # Варинат 53
# text = 10766
# N = 11009
# e = 6353

# # Варинат 67
# text = 4022
# N = 11413
# e = 5141

# # Варинат 89
# text = 10957
# N = 13589
# e = 361

# Варинат Ввод данных
print ("\nВВЕДИТЕ ДАННЫЕ ВАРИАНТА")
text = int(input("\tШифр-текст: "))
N = int(input("\tПерехваченное число (N): "))
e = int(input("\tОткрытый ключ (e): "))


print ("\nДАНО", "\n\tШифр-текст:", text, "\n\tN =", N, "\n\tОткрытый ключ (e):", e)

p = 2
q = 0

flag = True
while flag:
	if N % p == 0:
		q = N / p
		flag = False
	else:
		p += 1
	pass

print ("\nРазложили N на множители (простые большие числа)")
print ("\tN =", int(p), "*", int(q) )





phi = (p - 1) * (q - 1)

print ("\nРасчитаем функцию 'phi' = (p - 1)(q - 1) ")
print ("\tphi =", phi)






print ( "\nНайдем закрытый ключ (d) для этого решим d * e = 1 mod(phi) \nНайдем e^-1 (Ход Конем):" )

matrix = np.array( [[1, 0, phi],
					[0, 1, e]] )

flag = True
d = 0 # d = _e

print ("\n\t", matrix[0] )
print ("\t", matrix[1] )

while flag:
	index = np.shape(matrix)
	k = int( matrix[index[0]-2, -1] / matrix[index[0]-1, -1] )
	temp =  matrix[index[0]-2] - matrix[-1] * k
	print ("\t", temp )
	matrix = np.vstack((matrix, temp))
	if (temp[-1] == 1):
		d = temp[1]
		flag = False
	if (temp[-1] == 0):
		flag = False
	pass

print ("\nЗакрытый ключ (d):", d)

step = np.array( [int(item) for item in bin(int(d))[2:] ] )

print ("Закрытый ключ (в двоичной форме):", step)






d = 1
t = text

print ("\nДешифруем сообщение (алгоритм возведения в степень «справа налево»)")

size = np.size(step)
for i in range(size):
	if step[size-i-1] == 1:
		print ("Шаг", i)
		print( "\td = (", d, "*", t, ") mod(", N, ") =", (d * t) % N )
		print ( "\tt =", t, "^2 mod(", N, ") =", pow(t, 2) % N )
		d = (d * t) % N
		t = pow(t, 2) % N
	else:
		print ("Шаг", i)
		print ( "\tt =", t, "^2 mod(", N, ") =", pow(t, 2) % N )
		t = pow(t, 2) % N
		
	pass

print ("\nДешифрованное сообщение:", d)
print ("Дешифрованное сообщение (в двоичной форме):", np.array( [int(item) for item in bin(int(d))[2:] ]) )






# attak = np.array( [int(item) for item in bin(int(d))[2:] ] )

print ("\nОТВЕТ:")
print ("\tDay:", int( bin( int(d) )[-5:], 2 ), "\tMonth:", int( bin( int(d) )[2:-5], 2 ) )

