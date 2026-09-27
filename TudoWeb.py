#Decidi incluir a Playstation na atividade para estimular os meus processos criativos.
#Além de incluir o cálculo para EXCELENTE e RUIM, também decidi incluir para BOM.
#Também incluí o cálculo para o total somar o total de entrevistados.

print("Afim de melhorar nossos serviços, a Playstation, em parceria com a TudoWeb, está "
      "realizando uma pesquisa de satisfação com os nossos clientes. Insira a nota e os dados abaixo.")
print("Obs: nos avalie com uma das seguintes classificações: "
      "'Excelente ★★★', 'Bom ★★☆', ou 'Ruim ★☆☆:'.")


excelente = 0
bom = 0
ruim = 0

for i in range(1+49):

#Input.

 nota = input("Digite a classificação: ")
 nome = input("Nome: ")
 idade = input("Idade: ")

#Processing.

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


#Output.

print("\n Total de usuários entrevistados:", total_entrevistados)
print("\n Total de avaliações 'Excelente' ★★★:", total_excelente)
print("\n Total de avaliações 'Bom' ★★☆:", total_bom)
print("\n Total de avaliações 'Ruim' ★☆☆:", total_ruim)
print("\n A Playstation agradece a sua preferência.")