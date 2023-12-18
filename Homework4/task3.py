# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

summ = 10000
in_money = 'Пополнить'
out_money = 'Снять'
exit_bank = 'Выйти'
SUMM_SN = 50
MOD_SUMM = 0.015
MIN_MONEY = 30
MAX_MONEY = 600
IN_MOD = 1.03
GOLD_HUMAN = 0.9
MUILTIPLICITY = 3
count = 10
SUMM_GOLD_HUMAN = 5_000_000


def in_bank_money(s: int):
    if s % SUMM_SN == 0:
        global count
        count += 1
        global summ
        summ += in_bank


def out_bank_money(s: int):
    global summ
    global count
    if s % SUMM_SN == 0:
        commiss = s * MOD_SUMM
        if commiss < MIN_MONEY:
            commiss = MIN_MONEY
        elif commiss > MAX_MONEY:
            commiss = MAX_MONEY
        if commiss + s < summ:
            summ -= (commiss + s)
            count += 1


while True:
    action = input('Выберите операцию: Пополнить, Снять, Выйти: ')
    if summ >= SUMM_GOLD_HUMAN:
        summ *= GOLD_HUMAN
    if count % MUILTIPLICITY == 0 and count != 0:
        summ += summ*IN_MOD
        count = 0
    if action == in_money:
        in_bank = int(input('Введите сумму ввода средств: '))
        in_bank_money(in_bank)
    elif action == out_money:
        out_bank = int(input('Введите сумму для вывода средств: '))
        out_bank_money(out_bank)
    else:
        break
    print(summ)