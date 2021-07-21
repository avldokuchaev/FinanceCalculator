# Калькулятор вклада без капитализации

try:
    summa_vklada = float(input("Введите сумму вклада: "))
    srok_vklada = int(input("Введите срок вклада в месяцах: "))
    procentnaya_stavka = float(input("Введите процентную ставку: "))
except:
    print("Вы ввели не цифры!")
else:
    zarabot_summa_v_god = (summa_vklada * procentnaya_stavka * srok_vklada / 365) / 100
    print(f"За {srok_vklada} месяца(ев) вы получете {round(zarabot_summa_v_god, 2)}")
    print(f"Итоговая сумма через {srok_vklada} месяца(ев) составит {round(zarabot_summa_v_god + summa_vklada, 2)}")
