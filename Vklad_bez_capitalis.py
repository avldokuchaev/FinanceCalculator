# Калькулятор вклада без капитализации

try:
    summa_vklada = float(input("Введите сумму вклада: "))
    srok_vklada = int(input("Введите срок вклада в днях: "))
    procentnaya_stavka = float(input("Введите процентную ставку: "))
except:
    print("Вы ввели не цифры!")
else:
    zarabot_summa_v_god = (summa_vklada * procentnaya_stavka * srok_vklada / 365) / 100
    print(f"За {srok_vklada} дней вы получите {round(zarabot_summa_v_god, 2)}")
    print(f"Итоговая сумма через {srok_vklada} дней составит {round(zarabot_summa_v_god + summa_vklada, 2)}")
