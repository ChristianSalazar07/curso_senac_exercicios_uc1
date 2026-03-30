N = int(input("Informe o valor de N:"))
A = N
for i in range(N-1):
    A = A + ((N-(i+1))/(i+2))
print(f"A = N + (N - 1) / 2 + (N - 2) / 3 + ... + 1/N \nLogo, A={A:.2f}")