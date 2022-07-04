import os
import datetime

def Foldereng():
    os.system("color a")
    x = datetime.datetime.now()
    print("Hello. First of all, thank you for using the 'MPP'\nFrom Today: ",x.strftime("%A"),x.strftime("%c"))
    print("""
    .___        _____       
    |   | _____/ ____\____  
    |   |/    \   __\/  _ \ 
    |   |   |  \  | (  <_> )
    |___|___|  /__|  \____/ 
            \/             
            
    The Folder will be Created where the program is installed.
    """)
    klasör = input("Enter The Name Of The Folder You Want To Create: ")
    if os.path.exists(klasör.format()):
      os.system("cls")
      os.system("color 4")
      print("""
  _  _  _  _______  _______  _______  _______  _______  _  _  _ 
  ( )( )( )(  ____ \(  ____ )(  ____ )(  ___  )(  ____ )( )( )( )
  | || || || (    \/| (    )|| (    )|| (   ) || (    )|| || || |
  | || || || (__    | (____)|| (____)|| |   | || (____)|| || || |
  | || || ||  __)   |     __)|     __)| |   | ||     __)| || || |
  (_)(_)(_)| (      | (\ (   | (\ (   | |   | || (\ (   (_)(_)(_)
  _  _  _ | (____/\| ) \ \__| ) \ \__| (___) || ) \ \__ _  _  _ 
  (_)(_)(_)(_______/|/   \__/|/   \__/(_______)|/   \__/(_)(_)(_)
                                                                
  """)
      remove = input("Such a folder already exists.\nDo you want to delete?Y/N :")
      if remove == "Y" or remove == "y":
        os.rmdir(klasör.format())
        return False
    else :
      os.mkdir(klasör.format())
      print("Folder Created Successfully!","Folder Name:",klasör)
      print("Write Exit To Close The 'MPP'or Type menu to return to the menu.")
    cikis= input("Write Here :")
    if cikis == "exit"or cikis == "Exit":
      print("Program Closing...") 
      return False
    elif cikis == "Menu" or cikis == "":
       engmenu()
def Foldertr():
  os.system("color a")
  x = datetime.datetime.now()
  print("Merhaba.Öncelikle 'MPP'yi Kullandığın için teşekkür ederim.\nBugün Günlerden: ",x.strftime("%A"),x.strftime("%c"))
  print("""
__________.__.__          .__ 
\______   \__|  |    ____ |__|
 |    |  _/  |  |   / ___\|  |
 |    |   \  |  |__/ /_/  >  |
 |______  /__|____/\___  /|__|
        \/        /_____/     
    Dosya Programın Kurulu Olduğu Yere Oluşturulacaktır.
    """)
  klasör = input("Oluşturmak İstediğiniz Klasörün İsmini Girin: ")
  if os.path.exists(klasör.format()):
      os.system("cls")
      os.system("color 4")
      print("""
_  _  _           _______ _________ _______  _  _  _ 
( )( )( )|\     /|(  ___  )\__   __/(  ___  )( )( )( )
| || || || )   ( || (   ) |   ) (   | (   ) || || || |
| || || || (___) || (___) |   | |   | (___) || || || |
| || || ||  ___  ||  ___  |   | |   |  ___  || || || |
(_)(_)(_)| (   ) || (   ) |   | |   | (   ) |(_)(_)(_)
 _  _  _ | )   ( || )   ( |   | |   | )   ( | _  _  _ 
(_)(_)(_)|/     \||/     \|   )_(   |/     \|(_)(_)(_)                                                  
                                                                
  """)
      remove = input("Böyle Bir Klasör Zaten Mevcut.\nSilmek İstermisiniz?E/H :")
      if remove == "E" or remove == "e":
        os.rmdir(klasör.format())
        return False
      else:
        None
  else :
    os.mkdir(klasör.format())
    print("Klasör Başarıyla Oluşturuldu!","Klasör ismi:",klasör)
    print("'MPP'Yi Kapatmak İçin Exit Yazın veya Menüye Dönmek İçin Menü Yazın.")
    cikis= input("Buraya Yazın :")
    if cikis == "exit"or cikis == "Exit":
      print("Program Kapatılıyor...") 
      exit
    elif cikis == "Menü" or cikis == "menü":
       trmenu()       
def noteeng():
    x = datetime.datetime.now()
    print("Hello. First of all, thank you for using the program.\nFrom Today: ",x.strftime("%A"),x.strftime("%c"))
    print("""
    .___        _____       
    |   | _____/ ____\____  
    |   |/    \   __\/  _ \ 
    |   |   |  \  | (  <_> )
    |___|___|  /__|  \____/ 
            \/             
            
    The File will be Created where the program is installed.
    """)
    input("Press Enter To Continue")
    os.system("cls")
    os.system("color a")
    print("""
  $$\   $$\            $$\               $$$$$$$\                 $$\ 
  $$$\  $$ |           $$ |              $$  __$$\                $$ |
  $$$$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\  $$ |  $$ |$$$$$$\   $$$$$$$ |
  $$ $$\$$ |$$  __$$\\_$$  _|  $$  __$$\ $$$$$$$  |\____$$\ $$  __$$ |
  $$ \$$$$ |$$ /  $$ | $$ |    $$$$$$$$ |$$  ____/ $$$$$$$ |$$ /  $$ |
  $$ |\$$$ |$$ |  $$ | $$ |$$\ $$   ____|$$ |     $$  __$$ |$$ |  $$ |
  $$ | \$$ |\$$$$$$  | \$$$$  |\$$$$$$$\ $$ |     \$$$$$$$ |\$$$$$$$ |
  \__|  \__| \______/   \____/  \_______|\__|      \_______| \_______ 
  """)
    print("Hello. First of all, thank you for using The 'MPP'.\nFrom Today: ",x.strftime("%A"),x.strftime("%c")) 
    yazi = input("Write Your Note:")
    if os.path.exists("My Note.txt"):
      os.system("cls")
      os.system("color 4")
      print("""
  _  _  _  _______  _______  _______  _______  _______  _  _  _ 
  ( )( )( )(  ____ \(  ____ )(  ____ )(  ___  )(  ____ )( )( )( )
  | || || || (    \/| (    )|| (    )|| (   ) || (    )|| || || |
  | || || || (__    | (____)|| (____)|| |   | || (____)|| || || |
  | || || ||  __)   |     __)|     __)| |   | ||     __)| || || |
  (_)(_)(_)| (      | (\ (   | (\ (   | |   | || (\ (   (_)(_)(_)
  _  _  _ | (____/\| ) \ \__| ) \ \__| (___) || ) \ \__ _  _  _ 
  (_)(_)(_)(_______/|/   \__/|/   \__/(_______)|/   \__/(_)(_)(_)
                                                                
  """)
      input("Such a File Already Exists.\nPlease Restart the Program After Deleting the Existing File.")
      return False
    else:
      f  = open("My Note.txt", "w")
      f.write(yazi.format())
    print("Note Written Inside the File :",yazi.format())

    print("Write Exit To Close The 'MPP'or Type menu to return to the menu.")
    cikis= input("Write Here :")
    if cikis == "exit"or cikis == "Exit":
      print("Program Closing...") 
      return False
    elif cikis == "Menu" or cikis == "":
       engmenu()   
def notetr():
    x = datetime.datetime.now()
    print("Merhaba.Öncelikle Programı Kullandığın için Teşekkür ederim.\nBugün Günlerden: ",x.strftime("%A"),x.strftime("%c"))
    print("""
    
__________.__.__          .__ 
\______   \__|  |    ____ |__|
 |    |  _/  |  |   / ___\|  |
 |    |   \  |  |__/ /_/  >  |
 |______  /__|____/\___  /|__|
        \/        /_____/                  
            
    Dosya Programın Kurulu Olduğu Yere Oluşturulacaktır.
    """)
    input("Devam Etmek İçin Entera Basın")
    os.system("cls")
    os.system("color a")
    print("""

$$\   $$\            $$\           $$$$$$$\             $$$$$$\    $$\                         $$\ 
$$$\  $$ |           $$ |          $$  __$$\           $$  __$$\   $$ |                        \__|
$$$$\ $$ | $$$$$$\ $$$$$$\         $$ |  $$ | $$$$$$\  $$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\  $$\ 
$$ $$\$$ |$$  __$$\\_$$  _|        $$ |  $$ |$$  __$$\ $$$$\     \_$$  _|  $$  __$$\ $$  __$$\ $$ |
$$ \$$$$ |$$ /  $$ | $$ |          $$ |  $$ |$$$$$$$$ |$$  _|      $$ |    $$$$$$$$ |$$ |  \__|$$ |
$$ |\$$$ |$$ |  $$ | $$ |$$\       $$ |  $$ |$$   ____|$$ |        $$ |$$\ $$   ____|$$ |      $$ |
$$ | \$$ |\$$$$$$  | \$$$$  |      $$$$$$$  |\$$$$$$$\ $$ |        \$$$$  |\$$$$$$$\ $$ |      $$ |
\__|  \__| \______/   \____/       \_______/  \_______|\__|         \____/  \_______|\__|      \__| 
                                                                                                                                                                                                      
  """)
    print("Merhaba. Her şeyden önce, 'MPP'yi kullandığınız için teşekkür ederim.\nBugün Günlerden ",x.strftime("%A"),x.strftime("%c")) 
    yazi = input("Notunuzu Yazın.:")
    if os.path.exists("Notum.txt"):
      os.system("cls")
      os.system("color 4")
      print("""
 _  _  _           _______ _________ _______  _  _  _ 
( )( )( )|\     /|(  ___  )\__   __/(  ___  )( )( )( )
| || || || )   ( || (   ) |   ) (   | (   ) || || || |
| || || || (___) || (___) |   | |   | (___) || || || |
| || || ||  ___  ||  ___  |   | |   |  ___  || || || |
(_)(_)(_)| (   ) || (   ) |   | |   | (   ) |(_)(_)(_)
 _  _  _ | )   ( || )   ( |   | |   | )   ( | _  _  _ 
(_)(_)(_)|/     \||/     \|   )_(   |/     \|(_)(_)(_)                                                  
                                                                
  """)
      input("Böyle Bir Dosya Zaten Var.\nLütfen Dosyayı sildikten Sonra Programı Yeniden Başlatın.")
      return False
    else:
      f  = open("Notum.txt", "w")
      f.write(yazi.format())
    print("Kullanıcı Tarafından Yazılan Not :",yazi.format())

    print("'MPP'Yi Kapatmak İçin Exit Yazın veya Menüye Dönmek İçin Menü Yazın.")
    cikis= input("Buraya Yazın :")
    if cikis == "exit"or cikis == "Exit":
      print("Program Kapatılıyor...") 
      exit
    elif cikis == "Menü" or cikis == "menü":
       trmenu()  
def engmenu():
  os.system("color 1")
  os.system("cls")
  print("""
888b     d888 8888888b.  8888888b.  
8888b   d8888 888   Y88b 888   Y88b 
88888b.d88888 888    888 888    888 
888Y88888P888 888   d88P 888   d88P 
888 Y888P 888 8888888P"  8888888P"  
888  Y8P  888 888        888        
888   "   888 888        888        
888       888 888        888        
""")
  print("The purpose of this program is for people whose computers work slowly.\nYou can learn the details from the User's Guide.")
  print("1. Folder Creation Program.\n2.Note Creator Program (Notepad)")
  prog = input("Which one would you like to use 1/2?\nChoose Your Option: ")
  prog = int(prog)
  if prog == 1:
    os.system("cls")
    Foldereng()
  elif prog == 2:
    os.system("cls")
    noteeng() 
  else:  
    os.system("color 4")
    os.system("cls")
    print("""
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
                             
""") 
    input("OOPS! Wrong Option. If you have new ideas, you can send an e-mail.\nEmail Address : mpppython@gmiail.com")
    return False
def trmenu():
  os.system("color 4")
  os.system("cls")
  print("""
888b     d888 8888888b.  8888888b.  
8888b   d8888 888   Y88b 888   Y88b 
88888b.d88888 888    888 888    888 
888Y88888P888 888   d88P 888   d88P 
888 Y888P 888 8888888P"  8888888P"  
888  Y8P  888 888        888        
888   "   888 888        888        
888       888 888        888        
""")
  print("Bu program, bilgisayarı yavaş çalışan kişiler içindir.\nAyrıntıları Kullanım Kılavuzundan öğrenebilirsiniz.")
  print("1. Klasör Oluşturma Programı.\n2.Not Oluşturma Programı (Not Defteri)")
  prog = input("Hangisini kullanmak istersiniz?1/2\nBirini Seçin: ")
  prog = int(prog)
  if prog == 1:
    os.system("cls")
    Foldertr()
  elif prog == 2:
    os.system("cls")
    notetr() 
  else:  
    os.system("color 4")
    os.system("cls")
    print("""
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
                             
""") 
    input("UPS! Yanlış Seçenek. Yeni fikirleriniz varsa e-posta gönderebilirsiniz.\nE-posta Adresi : mpppython@gmiail.com")
    return False

lang = input("Choose Your Language EN/TR:")
guide = input("Do you want to install the User's Guide?Y/N: ")
if guide == "Y":
  os.system('"User Guide.py"')
else:
  None
os.system("cls") 

if lang == "EN" or lang == "En" or lang == "en" or lang=="eN":
  os.system("cls")
  engmenu() 
elif lang == "NE" or lang == "nE" or lang == "Ne" or lang == "ne":
  os.system("color 4")
  print("""  
  
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
  
""")
  print("OOPS! You Spelled It Wrong.\nDid You Mean? : EN")
  input("Press Enter To Exit.")
  exit
elif lang == "TR" or lang == "Tr" or lang == "tR" or lang == "tr": 
  os.system("cls")
  trmenu()
elif lang == "RT" or lang == "Rt" or lang == "rT" or lang == "rt":
  os.system("color 4")
  print("""  
   ____  ____  ____  _____ __
  / __ \/ __ \/ __ \/ ___// /
 / / / / / / / /_/ /\__ \/ / 
/ /_/ / /_/ / ____/___/ /_/  
\____/\____/_/    /____(_)   
  
""")
  print("UPS! Yanlış Yazdın.\nBunumu Demek İstedin? : EN")
  input("Çıkmak İçin Entera Basın.")
  exit