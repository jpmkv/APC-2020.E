answer = [input("Telefonou para a vítima? Sim (1) ou Não(0): "),
          input("Esteve no local do crime? Sim (1) ou Não(0): "),
          input("Mora perto da vítima? Sim (1) ou Não(0): "),
          input("Devia para a vítima? Sim (1) ou Não(0): "),
          input("Já trabalhou com a vítima? Sim (1) ou Não(0): ")]

answer_sum = 0

for c in answer:
    answer_sum = answer_sum + int(c)

print()

if answer_sum < 2:
    print("Inocente")

elif answer_sum == 2:
    print("Suspeita")

elif 3 <= answer_sum <= 4:
    print("Cúmplice")

elif answer_sum == 5:
    print("Assassino")

