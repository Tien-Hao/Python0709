print('\'')

pen = 15
amount = 20
total = pen * amount
print(pen, amount, total, sep="&")
print(pen, amount, total, sep=",")
print('鉛筆每支' + str(pen) + '元' + str(amount) + '支總共是' + str(total) + '元')
print('鉛筆每支%d元%d支總共是%d元' % (pen, amount, total))
