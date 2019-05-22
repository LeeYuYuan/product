
import os
products = []

#讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品, 價錢' in line:
                continue
            PN, PP = line.strip().split(',')
            products.append([PN, PP])   
    return products
#輸入商品及商品價格
def input_information(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        pp =[name, price]
        products.append(pp)
    print(products)
    return products
#印出商品資料	
def print_product(products):
    for pp in products:
        print(pp[0], '的價錢是', pp[1], '元')
#寫入新檔
def write_new_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價錢\n')
        for pp in products:
            f.write(pp[0] + ',' + str(pp[1]) + '\n')
  

def main_function():
    filename = input('您想找的檔案名稱:')
    if os.path.isfile(filename):
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('找無檔案')
    products = input_information(products)
    print_product(products)
    write_new_file(filename, products)

main_function()