
from io import UnsupportedOperation
import sqlite3

connection = sqlite3.connect("todo.db")

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE tasks(task text, status text)""")
    except:
        pass    



def wyswietl_liste(connection):
    task_index = 0
    print("--------------------------------------------------------")
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task, status FROM tasks""")
    result = cur.fetchall()
    # print(result)
    # print("@@@@@@@")
    for row in result:
        print(str(row[0]) + " - " + row[1] + " - " + row[2])
    # print("//////")
    # for row in result:
    #     print(row)


def dodaj_zadanie(connection):
    new_task = input("NOWE ZADANIE: ")
    cur = connection.cursor()
    cur.execute("""INSERT INTO tasks(task, status) VALUES(?,?)""", (new_task,"open"))
    connection.commit()


def usun_zadanie(connection):
    ktore = int(input("Podaj numer zadania które chcesz usunąc: "))
    
    cur = connection.cursor()
    try:
        usuniete = cur.execute("""DELETE FROM tasks WHERE rowid=?""", (ktore,)).rowcount
        print("które: ", ktore)
        print("usuniete: ", usuniete)
        if usuniete == 1:
            print("brawo, zadanie usuniet")
        else:
            print("Takie zadanie nie istniej")
    except:
        print("blad przy usuwaniu")
    connection.commit()

def przeniesc_zadnie_do_DONE(ktore):
    ktore = int(input("Podaj numer zadania które wykonałeś [DONE]: "))
    cur = connection.cursor()
    updated = cur.execute("""UPDATE tasks SET status=? WHERE rowId=?""", ("DONE",ktore)).rowcount
    if updated == 1:
        print("zaktualizowano wiersz:",ktore )
    else:
        print("bład")
    connection.commit()


create_table(connection)

while True:

    print ("\n"+"|||||||||||||||||||||||||||||||||||||||     MENU   ||||||||||||||||||||||||||||||||||||||||||||||||||")
    print ("1 - wyświetla wszystkie zadania")
    print ("2 - dodaj NOWE zadanie")
    print ("3 - usuń zadanie")
    print ("4 - zadanie wykonane")
    print ("5 - KONIEC"+"\n")

    try:
        action = int(input("Co chciałbyś zrobić? "+"\n"))

        if action >=1 and action <=5:
            if action == 1:
                wyswietl_liste(connection)
            elif action ==2:
                dodaj_zadanie(connection)
            elif action ==3:
                usun_zadanie(connection)
            elif action ==4:
                przeniesc_zadnie_do_DONE(connection)
            elif action ==5:
                break
        else:
            print ("wybierz poprawną cyfrę z menu !!!")
    except:
        print("Możesz wybrać tylko cyfrę od 1 do 5")



connection.close()