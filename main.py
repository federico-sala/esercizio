n = int(input("Inserisci un numero => "))
m = int(input("Inserisci un numero => "))
print("Ora calcolero' il maggiore tra i due e se esso e' divisibile per l'altro")
print(" ")

if n == m:
	print("I due numeri sono uguali")
elif n > m:
	if n%m == 0:
		print("Il numero maggiore tra i due e'", n)
		print(n, " e' divisibile per ", m)
	else:
		print("Il numero maggiore tra i due e'", n)
		print(n, " non e' divisibile per ", m)
elif n < m:
	if m%n == 0:
		print("Il numero maggiore tra due e'", m)
		print(m, " e' divisibile per ", n)
	else:
		print("il numero maggiore tra i due e'", m)
		print(m , " non e' divisibile per ", n)
