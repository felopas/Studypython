import random
alunos = ['cleiton','ze','jose','felipe']
alunosm = random.sample(alunos,4)

for aluno,numero in zip(alunosm,range(1,5)):
    print(f'o aluno escolhido foi {numero}: {aluno}')