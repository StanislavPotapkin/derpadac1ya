chek = int(input('Сумма товара в чеке 1: '))
chek2 = int(input('Сумма товара в чеке 2: '))
chek3 = int(input('Сумма товара в чеке 3: '))
summ = chek + chek2 + chek3
sell = summ * 5 / 100
if summ > 10000:
  a = summ - sell
  print("Скидка составила:", sell)
  print('К оплате:', a, 'рублей.')