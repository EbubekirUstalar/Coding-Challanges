def bonacci(N, k):
	
    Numbers = []
    for i in range(k):
        if(i < N -1):
            Numbers.append(0)
        elif(i == N - 1):
            Numbers.append(1)
        else:
            Numbers.append(sum(Numbers[-N:]))
    print(Numbers)
    return Numbers[-1]

print(bonacci(1, 10))
print(bonacci(2, 10))
print(bonacci(3, 10))
print(bonacci(4, 10))
print(bonacci(5, 10))