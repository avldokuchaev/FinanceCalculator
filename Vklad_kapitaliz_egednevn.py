# Калькулятор вклада с ежедневной капитализацией

try:
    summa_vklada = float(input("Введите сумму вклада: "))
    srok_vklada = int(input("Введите срок вклада в днях: "))
    procentnaya_stavka = float(input("Введите процентную ставку: "))
except:
    print("Вы ввели не цифры!")
else:
    procentnaya_stavka_modific = procentnaya_stavka / 100
    koefficient_dnei = procentnaya_stavka_modific / 365
    zarabotan_summa_full = summa_vklada * (1 + koefficient_dnei) ** srok_vklada
    zarabotan_summa_no_full = zarabotan_summa_full - summa_vklada
    print(f"За {srok_vklada} дней вы получите {round(zarabotan_summa_no_full, 2)}")
    print(f"Итоговая сумма через {srok_vklada} дней составит {round(zarabotan_summa_full, 2)}")
