permutation = []
def perm(a, k=0):
    if k == len(a):
        newElement = "".join([str(ab) for ab in a])
        if(newElement not in permutation):
            permutation.append(newElement)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

def next_number(num):
    numList = [int(a) for a in str(num)]
    perm(numList)
    NumberIndex = sorted(permutation).index(str(num))
    return int(sorted(permutation)[NumberIndex] if NumberIndex == len(permutation) - 1 else sorted(permutation)[NumberIndex + 1])

print(next_number(19))

