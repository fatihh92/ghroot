#_*_coding:utf-8_*_
from urllib.parse import urlparse
import urllib.request
import os
import img2pdf

banner = """
 _____            ______     ____   ____  _______
|     |    |   |  |     |   |    | |    |    |
|   ______ |___|  |_____|   |    | |    |    |
|        | |   |  |     )   |    | |    |    |
|________| |   |  |      )  |____| |____|    |
"""
print(banner)
u_rl = input("Url: ")
url= urlparse(u_rl)
u_path = url.path
print("Yol:  " + u_path)
print("\n\n")
path_array = u_path.split("-")
print("Yol dizisi: ", path_array)
print("\n\n")
no = input("Sayfa sayı dizisi: ")
print("\n\n")
page_no = path_array[int(no)]
print("İndirilecek sayfa sayısı: ", page_no)
print("\n\n")
while True:
    folder = input("Klasör ismi: ")
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.chdir(folder)
        break
    else:
        print(folder, " klasörü önceden oluşturulmu.Burdan devam etmek ister misin?")
        print("\n")
        ans = input("Cevap: ")
        if ans == 'e' or ans == 'E':
            os.chdir(folder)
            break
        else:
           continue
nu = input("Değiştirmek istediğin karakter hangisi?: ")
print("\n\n")
try:
    for i in range(1, int(page_no) + 1):
        path_array[i] = u_path.replace(nu, "-" + str(i))
        new_url = url.scheme +"://" + url.netloc + path_array[i]
        urllib.request.urlretrieve(new_url,"deneme"+str(i)+".jpg")
        print("*"*i+"  "+str(i)+".sayfa indirildi")
except ModuleNotFoundError as e:
    print(e)

print("\nPDF oluşturuluyor...")
print("\n\n")
pdf_name = input("PDF ismi: ")
print("\n\n")
with open(pdf_name+".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))

print("\nPDF oluşturuldu.")