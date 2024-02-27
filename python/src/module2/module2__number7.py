def output(a):
	string = ''
	for i in range(len(a)-1):
		string += str(a[i]) + ', '
	string += str(a[-1])
	return string

def radix__sort(arr):
    print('Initial array:')
    print(output(arr))
    print("**********")
    len__digits = len(str(arr[0]))
    base = 10
    bins = [[] for _ in range(base)]
    for i in range(0,len__digits):
        print(f"Phase {i+1}")
        for x in arr:
            digit = (int(x) // base ** i) % base
            if len(str(x)) == len__digits:
                bins[digit].append(str(x))
            else:
                x = '0' * (len__digits - len(str(x))) + str(x)
                bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        for j in range(len(bins)):
            if len(bins[j]) == 0:
                print(f"Bucket {j}: empty")
            else:
                string = output(bins[j])
                print(f"Bucket {j}: {string}")
        bins = [[] for _ in range(base)]
        print("**********")
    print("Sorted array:")
    print(output(arr))
n = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))
radix__sort(arr)
        
        