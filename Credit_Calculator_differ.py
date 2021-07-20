# Кредитный калькулятор дифференцированный

summa_zaima = float(input("Введите сумму займа: "))
srok_kreditovaniya = int(input("Введите срок кредитования в месяцах: "))
procentnaya_stavka = float(input("Введите процентную ставку: "))
perv_vznos = float(input("Введите сумму первоначального взноса, иначе введите \"0\": "))

chast_osnovn_dolga = summa_zaima / srok_kreditovaniya
summa_perv_zaima = summa_zaima

if perv_vznos == 0:
    summa_oplati_credita = []
    for mes in range(1, srok_kreditovaniya + 1):
        summa_procentov = summa_zaima * (procentnaya_stavka / 100) * 30 / 365
        summa_platega_v_mesyac = chast_osnovn_dolga + summa_procentov
        summa_oplati_credita.append(summa_platega_v_mesyac)
        print(f"Сумма выплаты в {mes} месяц = {round(summa_platega_v_mesyac, 2)}")
        summa_zaima = summa_zaima - chast_osnovn_dolga
else:
    summa_oplati_credita = []
    summa_zaima_minus_vznos = summa_zaima - perv_vznos
    chast_osnovn_dolga_minus_vznos = summa_zaima_minus_vznos / srok_kreditovaniya
    for mes in range(1, srok_kreditovaniya + 1):
        summa_procentov = summa_zaima_minus_vznos * (procentnaya_stavka / 100) * 30 / 365
        summa_platega_v_mesyac = chast_osnovn_dolga_minus_vznos + summa_procentov
        summa_oplati_credita.append(summa_platega_v_mesyac)
        print(f"Сумма выплаты в {mes} месяц = {round(summa_platega_v_mesyac, 2)}")
        summa_zaima_minus_vznos = summa_zaima_minus_vznos - chast_osnovn_dolga_minus_vznos

summa_oplati = sum(summa_oplati_credita)
print(f"Сумма, которую вы выплатите за весь срок кредита = {round(summa_oplati, 2)}")
print(f"Сумма переплаты составит = {round(summa_oplati - summa_perv_zaima - perv_vznos, 2)}")
