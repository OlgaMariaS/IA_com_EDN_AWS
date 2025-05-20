# Crie um programa que permita a um professor registrar as notas de uma turma. 
# O programa deve continuar solicitando notas até que o professor digite 'fim'. 
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
# No final, deve exibir a média da turma.

sum_grades = 0.0
count = 0

while True:
    entrada = input("Digite uma nota ou 'fim' para terminar: ").strip().lower()
    if entrada == 'fim':
        break
    try:
        nota = float(entrada)
    except ValueError:
        continue
    if 0 <= nota <= 10:
        sum_grades += nota
        count += 1

media = sum_grades / count if count != 0 else 0.0
print(f"A média da turma é {media:.2f}")