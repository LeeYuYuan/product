


import os
products = []
if os.path.isfile('product.csv'):
	print('找到檔案了')
	#讀取檔案
	with open('product.csv', 'r', encoding='utf-8') as f:
	    for line in f:
		    if '商品, 價錢' in line:
			    continue
		    PN, PP = line.strip().split(',')
		    products.append([PN, PP])
else:
	print('找無檔案')

#輸入商品及商品價格
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	pp =[name, price]
	products.append(pp)
print(products)

#印出商品資料	
for pp in products:
	print(pp[0], '的價錢是', pp[1], '元')

#寫入新檔
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價錢\n')
	for pp in products:
		f.write(pp[0] + ',' + str(pp[1]) + '\n')
  