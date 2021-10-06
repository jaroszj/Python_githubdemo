import random
import sys
import string

password = []
password_length = int(input("Podaj długość hasła: "))
signs_left = password_length


def update_remaining_characters (ile_znakow):
    global signs_left           #zmienna globalna, aby fukcja widziała zmienną zadeklaroną na zewnątrz funckji
    if signs_left < 0 or ile_znakow > signs_left:
        print("wykorzystałeś wszystkie znaki lub chcesz. Zostało ich", signs_left)
        sys.exit(0)
    else:
        signs_left -= ile_znakow
        print("Pozstało do wykorzystania: ", signs_left)



Upper_letters = int(input("Ile dużych liter: "))
update_remaining_characters(Upper_letters)
        
Lower_letters = int(input("Ile małych liter: "))
update_remaining_characters(Lower_letters)

Special_chars = int(input("Ile znaków specjalnych: "))
update_remaining_characters(Special_chars)

Digits = int(input("Ile cyfr: "))
update_remaining_characters(Digits)


if signs_left > 0:
    print("Pozostało ", signs_left , "znaków do wykorzystania. Jakimi znakami chciałbyś je uzupełnić ?")
    print("[1] - Duże litery")
    print("[2] - małe litery")
    print("[3] - znaki specjalne")
    print("[4] - cyfry")
    uzupelnienie = int(input())  

    if uzupelnienie ==1:
        Upper_letters +=signs_left
    elif uzupelnienie == 2:
        Lower_letters +=signs_left
    elif uzupelnienie==3:
        Special_chars +=signs_left
    elif uzupelnienie==4:
        Digits+=signs_left





print("Dlugosc hasła: ", password_length , "składajace się z: ")
print("Duże liter: ", Upper_letters)
print("Małe litery : ", Lower_letters)
print("Znaki specjalne :", Special_chars)
print("Cyfry :", Digits)


for _ in range (password_length):
    if Upper_letters >0:
        password.append(random.choice(string.ascii_uppercase))
        Upper_letters -=1
    if Lower_letters >0:
        password.append(random.choice(string.ascii_lowercase))
        Lower_letters -=1
    if Special_chars>0:
        password.append(random.choice(string.punctuation))
        Special_chars -=1
    if Digits >0:
        password.append(random.choice(string.digits))
        Digits -=1

random.shuffle(password)
print("wygenerowane hasło to: ", "".join(password))




