def output(a):
	string = ''
	for i in range(len(a)-1):
		string += str(a[i]) + ' '
	string += str(a[-1])
	return string
n = int(input())
mass = list(map(int, input().split()))
if mass != sorted(mass):
	for i in range(n-1):
		for j in range(n-i-1):
			if mass[j] > mass[j+1]:
				mass[j], mass[j+1] = mass[j+1], mass[j]
				print(output(mass))
else:
	print(0)