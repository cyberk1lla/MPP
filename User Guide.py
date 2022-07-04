import os
import datetime
os.system("cls")
os.system("color F0")
x = datetime.datetime.now()
print("Hello. First of all, thank you for using the program.\nFrom Today: ",x.strftime("%A"),x.strftime("%c"))
lang = input("Choose Your Language EN/TR: ")
def eng():
  if os.path.exists("User Guide.txt"):
    os.remove("User Guide.txt")
    input("Such a File Already Exists.\nThe existing file will be deleted and replaced with a new one.")
  f = open("User Guide.txt", "a")
  f.write("Hello Dear User,\nFirst of all, thank you for using the program.\n'MPP'aims to make it easier to create folders and write in notebook on low-end computers.\nDoes Not Contain Any Malware.\nYou can e-mail your thoughts and suggestions about the program.\nEmail Address : mpppython@gmail.com")
  input("User Guide Created Successfully!\nPress Enter To Continue.")
  return False
def tr():
  if os.path.exists("Kullanım Kılavuzu.txt"):
    os.remove("Kullanım Kılavuzu.txt")
    input("Böyle Bir Dosya Zaten Var.\nMevcut dosya silinecek ve yenisiyle değiştirilecek..")
  f = open("Kullanım Kılavuzu.txt", "a")
  f.write("Merhaba Değerli Kullanıcı,\nÖncelikle, programı kullandığınız için teşekkür ederim.\n'MPP',düşük seviyedeki bilgisayarlarda klasör oluşturmayı ve not defterlerine yazı yazmayı kolaylaştırmayı amaçlamaktadır.\nHiçbir Kötü Amaçlı Yazılım İçermez.\nProgramla ilgili düşünce ve önerilerinizi mail atabilirsiniz.\nE-posta Adresi : mpppython@gmail.com")
  input("Kullanım Kılavuzu Başarıyla Oluşturuldu!\nDevam Etmek İçin Entera Basın.")
  return False
if lang == "EN" or lang == "En" or lang == "eN" or lang == "en":   
  eng()
elif lang == "NE" or lang == "nE" or lang == "Ne" or lang == "ne":
  os.system("color 4")
  print("""  
  
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
  
""")
  input("OOPS! You Spelled It Wrong.\nDid You Mean? : EN")
  exit
elif lang == "TR" or lang == "Tr" or lang == "tR" or lang == "tr": 
  tr()
elif lang == "RT" or lang == "Rt" or lang == "rT" or lang == "rt":
  os.system("color 4")
  print("""  
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
  
""")
  input("UPS! Yanlış Yazdın.\nBunumu Demek İstedin? : TR")
  exit
