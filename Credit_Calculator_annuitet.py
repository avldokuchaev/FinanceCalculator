# Кредитный калькулятор аннуитетный

summa_zaima = float(input("Введите сумму займа: "))
srok_kreditovaniya = int(input("Введите срок кредитования в месяцах: "))
procentnaya_stavka = float(input("Введите процентную ставку: "))
perv_vznos = float(input("Введите сумму первоначального взноса, иначе введите \"0\": "))

mes_procent_stavka = (procentnaya_stavka / 12) / 100
chisl_annuitet = mes_procent_stavka * ((1 + mes_procent_stavka) ** srok_kreditovaniya)
znamen_annuitet = ((1 + mes_procent_stavka) ** srok_kreditovaniya) - 1
koefficient_annuiteta = chisl_annuitet / znamen_annuitet

if perv_vznos == 0:
    month_payment = summa_zaima * koefficient_annuiteta
    print(f"Сумма ежемесячного платежа = {round(month_payment, 2)}")
    print(f"Сумма, которую вы выплатите за весь срок кредита = {round(month_payment * srok_kreditovaniya, 2)}")
    print(f"Сумма переплаты составит = {round(month_payment * srok_kreditovaniya - summa_zaima, 2)}")
else:
    month_payment = (summa_zaima - perv_vznos) * koefficient_annuiteta
    print(f"Сумма ежемесячного платежа = {round(month_payment, 2)}")
    print(f"Сумма, которую вы выплатите за весь срок кредита = {round(month_payment * srok_kreditovaniya, 2)}")
    print(f"Сумма переплаты составит = {round(month_payment * srok_kreditovaniya - summa_zaima, 2)}")
