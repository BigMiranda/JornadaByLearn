def continuar_cadastrando(tipo):
  resp = input(f"Deseja continuar a cadastrar {tipo}? (S/N) ")
  print(" ")

  if resp.upper() != "N":
    return True
  else:
    return False


def entrada_nota():
  nome = input("**Insira o nome do aluno: ")

  notas = []
  contador = 0
  continuar = True

  while continuar:

    notas.append(float(input(f"Insira a {contador + 1}° nota: ")))
    contador += 1

    continuar = continuar_cadastrando("notas")

  return [ nome , notas ]


def inserir_alunos():
  alunos = []
  continuar = True

  while continuar:
    aluno_novo = entrada_nota()

    alunos.append(aluno_novo)

    continuar = continuar_cadastrando("alunos") 
    print(" ") 

  return alunos


#_____________________________________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________________________


def o_que_sera_feito(alunos):
  print("O que será feito com esses dados? \nDigite o número correspondente")
  print(" 1 - Exibir notas \n 2 - Exibir médias \n 3 - Exibir a situação acadêmica e as médias \n 4 - Exibir a média geral \n 5 - Terminar")
  resp = input("Escolha a opção desejada: " )

  print("\n\n")

  if resp == "1":
    exibe_notas(alunos)
  elif resp == "2":
    exibe_medias(alunos)
  elif resp == "3":
    exibe_aprovados(alunos)
  elif resp == "4":
    exibe_media_geral(alunos)
  elif resp == "5":
    print("\n\n Até mais então!")
    return False
  else:
    print("\n Opção inválida")
  
  return True


def exibe_notas(alunos):
  for aluno in alunos:
    print("Notas do aluno ", aluno[0], ": ")
    
    for nota in aluno[1]:
      print(" - ", nota)

    print(" ")


def exibe_medias(alunos):
  for aluno in alunos:

    media = sum(aluno[1]) / len(aluno[1])

    print("Média do aluno ", aluno[0], ": ", media)

    print(" ")


def exibe_aprovados(alunos):

  nota_de_corte = float(input("Insira a nota de corte: "))
  print(" ")

  for aluno in alunos:
    media = sum(aluno[1]) / len(aluno[1])

    situacao = "APROVADO"
    if media < nota_de_corte:
      situacao = "REPROVADO"

    print(f"Aluno {aluno[0]} : {situacao} ---- Média: {media}")

    print("\n")


def exibe_media_geral(alunos):
  todas_as_medias = []

  for aluno in alunos:
    media = sum(aluno[1]) / len(aluno[1])
    todas_as_medias.append(media)

  media_total = sum(todas_as_medias) / len(todas_as_medias)
  print("A média geral dos alunos cadastrados é ", media_total)

alunos = inserir_alunos()

continuar = True
while continuar:
  print("\n_______________________________________________\n")
  continuar = o_que_sera_feito(alunos)
