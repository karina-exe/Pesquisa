excelente = 0
bom = 0
ruim = 0

for i in range(1+5):
 nota = input("Digite a nota: ")
 if nota == "excelente":
   excelente += 1
 elif nota == "bom":
    bom += 1
 elif nota == "ruim":
   ruim += 1

soma = 0
total_excelente = soma + excelente
total_bom = soma + bom
total_ruim = soma + ruim
total_entrevistados = total_excelente + total_bom + total_ruim

print("\n Total de usuários entrevistados:", total_entrevistados)
print("\n Total de avaliações 'Excelente' ★★★:", total_excelente)
print("\n Total de avaliações 'Bom' ★★☆:", total_bom)
print("\n Total de avaliações 'Ruim' ★☆☆:", total_ruim)