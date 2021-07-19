# Кредитный калькулятор аннуитетный

summa_zaima = float(input("Введите сумму займа: "))
srok_kreditovaniya = int(input("Введите срок кредитования в месяцах: "))
procentnaya_stavka = float(input("Введите процентную ставку: "))

mes_procent_stavka = (procentnaya_stavka / 12) / 100
chisl_annuitet = mes_procent_stavka * ((1 + mes_procent_stavka) ** srok_kreditovaniya)
znamen_annuitet = ((1 + mes_procent_stavka) ** srok_kreditovaniya) - 1
koefficient_annuiteta = chisl_annuitet / znamen_annuitet
month_payment = summa_zaima * koefficient_annuiteta
print(f"Сумма ежемесячного платежа = {round(month_payment, 2)}")
