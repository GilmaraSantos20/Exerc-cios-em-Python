
'''Digite nomes de alunos para serem impressos na tela com uma vírgula separando.'''

Alunos = []
for a in range (5):
  mensagem = input('Mensagem para alunos (Alunos separados por vírgula): ')
  Alunos.append(mensagem)
print(Alunos)