from recommendations import drama, asa, horror, comedy, tms, romance,aatv, scifi, dramatv, comedytv, hiphop, indiealt, randb, pop, fiction, science, philosophy, nonfiction, historicalfiction ,contemporary,pc,ps4
from random import choice
import string



print("""
                                                                        ____           ____     ____    __    __   ____
                                                         \          /  |      |       /       /      \  | \  / |  |  
                                                          \        /   |____  |      |       |        | |  \/  |  |____
                                                           \  /\  /    |      |      |       |        | |      |  |
                                                            \/  \/     |____  |____   \ ____  \ ____ /  |      |  |____

                                                                              ________    ____  
                                                                                 |      /      \ 
                                                                                 |     |        |
                                                                                 |     |        |
                                                                                 |      \ ____ /

                                                           _____                     ____     ____         _____         
                                                         |       \  |         |    /      \  |      |\   |   |     \  /   |
                                                         | _____ /  |  _____  |   |        | |____  | \  |   |      \/    |
                                                         |          |  _____  |   |        | |      |  \ |   |      /\    |
                                                         |          |         |    \ ____ /  |____  |   \| __|__   /  \   .

""")

intro = "Ahoy! Welcome to Phoenix!"
intro2 = intro.center(177)
print(intro2)

welcome = "I will be your personal Entertainment guide today! How may I help you? ^‿^"
welcome2 = welcome.center(177)
print(welcome2)

enter = "We've got recommendations for all your entertainment needs! Ranging from books to video games, anything you need, you will find it here!"
enter2 = enter.center(177)
print(enter2)

print("\n")

global name
name = input(
        "                                                                   Before we begin, what should I call you? ")
print("                                                                            Nice to meet you", name, "!")

print("\n")

recc = "Would you like to listen to a new album or watch a film or maybe something else? Choose an option! "
recc2 = recc.center(177)
print(recc2)

print("\n")

option1 = "1. Need a film recommendation?"
option2 = option1.center(177)
print(option2)

option3 = "2. Having trouble finding a new show to binge?"
option4 = option3.center(177)
print(option4)

option5 = "3. Can't decide on what album to listen to?"
option6 = option5.center(177)
print(option6)

option7 = "4. Need help deciding what to read next?"
option8 = option7.center(177)
print(option8)

option9 = "5. Looking for a new game suggestion?"
option10 = option9.center(177)
print(option10)

print("\n")
global what
what = input("                                                                  Where do you want to go? Enter a number: ")

print("\n")

what_list = ["1", "2", "3", "4", "5"]
while what not in what_list:
    what = input("                                                          Invalid entry. Where do you want to go? Enter a number: ")

    print("\n")

def main_func():
    print("""
                                                                            ____           ____     ____    __    __   ____
                                                             \          /  |      |       /       /      \  | \  / |  |  
                                                              \        /   |____  |      |       |        | |  \/  |  |____
                                                               \  /\  /    |      |      |       |        | |      |  |
                                                                \/  \/     |____  |____   \ ____  \ ____ /  |      |  |____

                                                                                  ________    ____  
                                                                                     |      /      \ 
                                                                                     |     |        |
                                                                                     |     |        |
                                                                                     |      \ ____ /

                                                               _____                     ____     ____         _____         
                                                             |       \  |         |    /      \  |      |\   |   |     \  /   |
                                                             | _____ /  |  _____  |   |        | |____  | \  |   |      \/    |
                                                             |          |  _____  |   |        | |      |  \ |   |      /\    |
                                                             |          |         |    \ ____ /  |____  |   \| __|__   /  \   .

    """)

    enter = "We've got recommendations for all your entertainment needs! Ranging from books to video games, anything you need, you will find it here!"
    enter2 = enter.center(177)
    print(enter2)

    print("\n")


    recc = "Would you like to listen to a new album or watch a film or maybe something else? Choose an option! "
    recc2 = recc.center(177)
    print(recc2)

    print("\n")

    option1 = "1. Need a film recommendation?"
    option2 = option1.center(177)
    print(option2)

    option3 = "2. Having trouble finding a new show to binge?"
    option4 = option3.center(177)
    print(option4)

    option5 = "3. Can't decide on what album to listen to?"
    option6 = option5.center(177)
    print(option6)

    option7 = "4. Need help deciding what to read next?"
    option8 = option7.center(177)
    print(option8)

    option9 = "5. Looking for a new game suggestion?"
    option10 = option9.center(177)
    print(option10)

    print("\n")
    global what
    what = input(
        "                                                                  Where do you want to go? Enter a number: ")

    print("\n")

    what_list = ["1", "2", "3", "4", "5"]
    while what not in what_list:
        what = input(
            "                                                          Invalid entry. Where do you want to go? Enter a number: ")

        print("\n")

    if what == "1":
        print("                                                       Hello", name,
              "! I am Marilyn ❐ ‿ ❑ I will be your film guide today!")
        genre = "What genre of film would you like to watch?"
        genre2 = genre.center(177)
        print(genre2)
        print("\n")
        genre3 = "1. Drama"
        genre4 = genre3.center(177)
        print(genre4)
        genre5 = "2. Action/Adventure/Sci-Fi"
        genre6 = genre5.center(177)
        print(genre6)
        genre7 = "3. Horror"
        genre8 = genre7.center(177)
        print(genre8)
        genre9 = "4. Comedy"
        genre10 = genre9.center(177)
        print(genre10)
        genre11 = "5. Thriller/Mystery"
        genre12 = genre11.center(177)
        print(genre12)
        genre13 = "6. Romance"
        genre14 = genre13.center(177)
        print(genre14)
        print("\n")
        global genre_choice
        genre_choice_list = ["1", "2", "3", "4", "5", "6"]
        genre_choice = input(
            "                                                                               Choose an option: ")
        print("\n")

        while genre_choice not in genre_choice_list:
            genre_choice = input(
                "                                                                       Invalid entry. Try again please : ")
            print("\n")

        def drama_func():
            global drama_rec
            drama_rec = choice(drama)
            drama_out = "We recommend you to watch : "
            drama_out2 = drama_out.center(177)
            print(drama_out2)
            print(drama_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def asa_func():
            if genre_choice == "2":
                global asa_rec
                asa_rec = choice(asa)
                asa_out = "We recommend you to watch : "
                asa_out2 = asa_out.center(177)
                print(asa_out2)
                print(asa_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def horror_func():
            if genre_choice == "3":
                global horror_rec
                horror_rec = choice(horror)
                horror_out = "We recommend you to watch : "
                horror_out2 = horror_out.center(177)
                print(horror_out2)
                print(horror_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def comedy_func():
            if genre_choice == "4":
                global comedy_rec
                comedy_rec = choice(comedy)
                comedy_out = "We recommend you to watch : "
                comedy_out2 = comedy_out.center(177)
                print(comedy_out2)
                print(comedy_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def tms_func():
            if genre_choice == "5":
                global tms_rec
                tms_rec = choice(tms)
                tms_out = "We recommend you to watch : "
                tms_out2 = tms_out.center(177)
                print(tms_out2)
                print(tms_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def romance_func():
            if genre_choice == "6":
                global romance_rec
                romance_rec = choice(romance)
                romance_out = "We recommend you to watch : "
                romance_out2 = romance_out.center(177)
                print(romance_out2)
                print(romance_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        if genre_choice == "1":
            drama_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                drama_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()
        elif genre_choice == "2":
            asa_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                asa_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()
        elif genre_choice == "3":
            horror_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                horror_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif genre_choice == "4":
            comedy_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                comedy_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif genre_choice == "5":
            tms_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                tms_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif genre_choice == "6":
            romance_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                romance_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

    elif what == "2":
        print("                                                       Hello", name,
              "! I am Milo (•◡•) I will be your TV guide today!")
        tv_genre = "What type of TV Show would you like to watch?"
        tv_genre2 = tv_genre.center(177)
        print(tv_genre2)
        print("\n")
        tv_genre3 = "1. Adventure/Action"
        tv_genre4 = tv_genre3.center(177)
        print(tv_genre4)
        tv_genre5 = "2. Sci-Fi"
        tv_genre6 = tv_genre5.center(177)
        print(tv_genre6)
        tv_genre7 = "3. Drama"
        tv_genre8 = tv_genre7.center(177)
        print(tv_genre8)
        tv_genre9 = "4. Comedy"
        tv_genre10 = tv_genre9.center(177)
        print(tv_genre10)
        print("\n")
        global tv_genre_choice
        tv_genre_choice_list = ["1", "2", "3", "4"]
        tv_genre_choice = input(
            "                                                                               Choose an option: ")
        print("\n")
        while tv_genre_choice not in tv_genre_choice_list:
            tv_genre_choice = input(
                "                                                                       Invalid entry. Try again please : ")
            print("\n")

        def aatv_func():
            if tv_genre_choice == "1":
                global aatv_rec
                aatv_rec = choice(aatv)
                aatv_out = "We recommend you to watch : "
                aatv_out2 = aatv_out.center(177)
                print(aatv_out2)
                print(aatv_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def scifi_func():
            if tv_genre_choice == "2":
                global scifi_rec
                scifi_rec = choice(scifi)
                scifi_out = "We recommend you to watch : "
                scifi_out2 = scifi_out.center(177)
                print(scifi_out2)
                print(scifi_rec.center(177))
                print("\n")
                global happy
                happy = input(
                    "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")
                happy_list = ["yes", "no"]
                while happy not in happy_list:
                    happy = input(
                        "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                    print("\n")

        def dramatv_func():
            global dramatv_rec
            dramatv_rec = choice(dramatv)
            dramatv_out = "We recommend you to watch : "
            dramatv_out2 = dramatv_out.center(177)
            print(dramatv_out2)
            print(dramatv_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def comedytv_func():
            global comedytv_rec
            comedytv_rec = choice(comedytv)
            comedytv_out = "We recommend you to watch : "
            comedytv_out2 = comedytv_out.center(177)
            print(comedytv_out2)
            print(comedytv_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        if tv_genre_choice == "1":
            aatv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                aatv_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()


        elif tv_genre_choice == "2":
            scifi_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                scifi_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif tv_genre_choice == "3":
            dramatv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                dramatv_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif tv_genre_choice == "4":
            comedytv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                comedytv_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()


    elif what == "3":
        print("                                                       Hello", name,
              "! I am Robyn (✦ ‿ ✦) I will help find you an album today!")
        album_genre = "What kind of music would you like to listen to?"
        album_genre2 = album_genre.center(177)
        print(album_genre2)
        print("\n")
        album_genre3 = "1. Hip-Hop"
        album_genre4 = album_genre3.center(177)
        print(album_genre4)
        album_genre5 = "2. Indie Alt"
        album_genre6 = album_genre5.center(177)
        print(album_genre6)
        album_genre7 = "3. R&B"
        album_genre8 = album_genre7.center(177)
        print(album_genre8)
        album_genre9 = "4. Pop"
        album_genre10 = album_genre9.center(177)
        print(album_genre10)
        print("\n")
        global album_genre_choice
        album_genre_choice_list = ["1", "2", "3", "4"]
        album_genre_choice = input(
            "                                                                               Choose an option: ")
        print("\n")
        while album_genre_choice not in album_genre_choice_list:
            album_genre_choice = input(
                "                                                                       Invalid entry. Try again please : ")
            print("\n")

        def hiphop_func():
            global hiphop_rec
            hiphop_rec = choice(hiphop)
            hiphop_out = "We recommend you to listen to : "
            hiphop_out2 = hiphop_out.center(177)
            print(hiphop_out2)
            print(hiphop_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def indiealt_func():
            global indiealt_rec
            indiealt_rec = choice(indiealt)
            indiealt_out = "We recommend you to listen to : "
            indiealt_out2 = indiealt_out.center(177)
            print(indiealt_out2)
            print(indiealt_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def randb_func():
            global randb_rec
            randb_rec = choice(randb)
            randb_out = "We recommend you to listen to : "
            randb_out2 = randb_out.center(177)
            print(randb_out2)
            print(randb_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def pop_func():
            global pop_rec
            pop_rec = choice(pop)
            pop_out = "We recommend you to listen to : "
            pop_out2 = pop_out.center(177)
            print(pop_out2)
            print(pop_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        if album_genre_choice == "1":
            hiphop_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                hiphop_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()


        elif album_genre_choice == "2":
            indiealt_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                indiealt_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif album_genre_choice == "3":
            randb_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                randb_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif album_genre_choice == "4":
            pop_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                pop_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

    elif what == "4":
        print("                                                  Hello", name,
              "! I am Marko (─‿─) I will help you find a new book to read today!")
        book_genre = "What type of book would you like to read?"
        book_genre2 = book_genre.center(177)
        print(book_genre2)
        print("\n")
        book_genre3 = "1. Literary Fiction"
        book_genre4 = book_genre3.center(177)
        print(book_genre4)
        book_genre5 = "2. Science"
        book_genre6 = book_genre5.center(177)
        print(book_genre6)
        book_genre7 = "3. Philosophy"
        book_genre8 = book_genre7.center(177)
        print(book_genre8)
        book_genre9 = "4. Non-Fiction"
        book_genre10 = book_genre9.center(177)
        print(book_genre10)
        book_genre11 = "5. Historical Fiction"
        book_genre12 = book_genre11.center(177)
        print(book_genre12)
        book_genre13 = "6. Contemporary"
        book_genre14 = book_genre13.center(177)
        print(book_genre14)
        print("\n")
        global book_genre_choice
        book_genre_choice_list = ["1", "2", "3", "4", "5", "6"]
        book_genre_choice = input(
            "                                                                               Choose an option: ")
        print("\n")
        while book_genre_choice not in book_genre_choice_list:
            book_genre_choice = input(
                "                                                                       Invalid entry. Try again please : ")
            print("\n")

        def fiction_func():
            global fiction_rec
            fiction_rec = choice(fiction)
            fiction_out = "We recommend you to read : "
            fiction_out2 = fiction_out.center(177)
            print(fiction_out2)
            print(fiction_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def science_func():
            global science_rec
            science_rec = choice(science)
            science_out = "We recommend you to read : "
            science_out2 = science_out.center(177)
            print(science_out2)
            print(science_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def philosophy_func():
            global philosophy_rec
            philosophy_rec = choice(philosophy)
            philosophy_out = "We recommend you to read : "
            philosophy_out2 = philosophy_out.center(177)
            print(philosophy_out2)
            print(philosophy_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def nonfiction_func():
            global nonfiction_rec
            nonfiction_rec = choice(nonfiction)
            nonfiction_out = "We recommend you to read : "
            nonfiction_out2 = nonfiction_out.center(177)
            print(nonfiction_out2)
            print(nonfiction_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def historicalfiction_func():
            global historicalfiction_rec
            historicalfiction_rec = choice(historicalfiction)
            historicalfiction_out = "We recommend you to read : "
            historicalfiction_out2 = historicalfiction_out.center(177)
            print(historicalfiction_out2)
            print(historicalfiction_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def contemporary_func():
            global contemporary_rec
            contemporary_rec = choice(contemporary)
            contemporary_out = "We recommend you to read : "
            contemporary_out2 = contemporary_out.center(177)
            print(contemporary_out2)
            print(contemporary_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        if book_genre_choice == "1":
            fiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                fiction_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif book_genre_choice == "2":
            science_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                science_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif book_genre_choice == "3":
            philosophy_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                philosophy_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif book_genre_choice == "4":
            nonfiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                nonfiction_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()


        elif book_genre_choice == "5":
            historicalfiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                historicalfiction_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif book_genre_choice == "6":
            contemporary_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                contemporary_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

    elif what == "5":
        print("                                              Hello", name,
              "! I am Mutiny ( ⌬̀⌄⌬́ ) Let's try and find what game you're going to play next!")
        game_plat = "What platform will you be gaming on?"
        game_plat2 = game_plat.center(177)
        print(game_plat2)
        print("\n")
        game_plat3 = "1. PC"
        game_plat4 = game_plat3.center(177)
        print(game_plat4)
        game_plat5 = "2. PS4"
        game_plat6 = game_plat5.center(177)
        print(game_plat6)
        print("\n")
        global game_plat_choice
        game_plat_choice = input(
            "                                                                               Choose an option: ")
        print("\n")
        game_plat_choice_list = ["1", "2"]
        while game_plat_choice not in game_plat_choice_list:
            game_plat_choice = input(
                "                                                                       Invalid entry. Try again please : ")
            print("\n")

        def pc_func():
            global pc_rec
            pc_rec = choice(pc)
            pc_out = "We recommend you to play : "
            pc_out2 = pc_out.center(177)
            print(pc_out2)
            print(pc_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        def ps4_func():
            global ps4_rec
            ps4_rec = choice(ps4)
            ps4_out = "We recommend you to play : "
            ps4_out2 = ps4_out.center(177)
            print(ps4_out2)
            print(ps4_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

        if game_plat_choice == "1":
            pc_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                pc_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()

        elif game_plat_choice == "2":
            ps4_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
            while happy == "no":
                ps4_func()
                if happy == "yes":
                    happy2 = "We're glad that you like our choice!"
                    happy3 = happy2.center(177)
                    print(happy3)
                    main_menu()


def main_menu():
    print("\n")
    goback = input("                                                        Would you like to go back the main menu? Type 'yes' or 'no' -  ")
    print("\n")
    if goback == "yes":
        main_func()
    elif goback == "no":
        farewell = "We're glad we could help. Thanks for using our application. Ciao!"
        farewell2 = farewell.center(177)
        print(farewell2)
    goback_list = ["yes","no"]
    while goback not in goback_list:
        goback = input("                                                Invalid entry. Would you like to go back the main menu? Type 'yes' or 'no' -  ")
        print("\n")
        if goback == "yes":
            main_func()
        elif goback == "no":
            farewell = "We're glad we could help. Thanks for using our application. Ciao! :)"
            farewell2 = farewell.center(177)
            print(farewell2)



if what == "1":
    print("                                                       Hello", name,
          "! I am Marilyn ❐ ‿ ❑ I will be your film guide today!")
    genre = "What genre of film would you like to watch?"
    genre2 = genre.center(177)
    print(genre2)
    print("\n")
    genre3 = "1. Drama"
    genre4 = genre3.center(177)
    print(genre4)
    genre5 = "2. Action/Adventure/Sci-Fi"
    genre6 = genre5.center(177)
    print(genre6)
    genre7 = "3. Horror"
    genre8 = genre7.center(177)
    print(genre8)
    genre9 = "4. Comedy"
    genre10 = genre9.center(177)
    print(genre10)
    genre11 = "5. Thriller/Mystery"
    genre12 = genre11.center(177)
    print(genre12)
    genre13 = "6. Romance"
    genre14 = genre13.center(177)
    print(genre14)
    print("\n")
    global genre_choice
    genre_choice_list = ["1","2","3","4","5","6"]
    genre_choice = input(
        "                                                                               Choose an option: ")
    print("\n")

    while genre_choice not in genre_choice_list:
        genre_choice = input(
            "                                                                       Invalid entry. Try again please : ")
        print("\n")

    def drama_func():
        global drama_rec
        drama_rec = choice(drama)
        drama_out = "We recommend you to watch : "
        drama_out2 = drama_out.center(177)
        print(drama_out2)
        print(drama_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")


    def asa_func():
        if genre_choice == "2":
            global asa_rec
            asa_rec = choice(asa)
            asa_out = "We recommend you to watch : "
            asa_out2 = asa_out.center(177)
            print(asa_out2)
            print(asa_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def horror_func():
        if genre_choice == "3":
            global horror_rec
            horror_rec = choice(horror)
            horror_out = "We recommend you to watch : "
            horror_out2 = horror_out.center(177)
            print(horror_out2)
            print(horror_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def comedy_func():
        if genre_choice == "4":
            global comedy_rec
            comedy_rec = choice(comedy)
            comedy_out = "We recommend you to watch : "
            comedy_out2 = comedy_out.center(177)
            print(comedy_out2)
            print(comedy_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def tms_func():
        if genre_choice == "5":
            global tms_rec
            tms_rec = choice(tms)
            tms_out = "We recommend you to watch : "
            tms_out2 = tms_out.center(177)
            print(tms_out2)
            print(tms_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def romance_func():
        if genre_choice == "6":
            global romance_rec
            romance_rec = choice(romance)
            romance_out = "We recommend you to watch : "
            romance_out2 = romance_out.center(177)
            print(romance_out2)
            print(romance_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    if genre_choice == "1":
        drama_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            drama_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
    elif genre_choice == "2":
        asa_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            asa_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()
    elif genre_choice == "3":
        horror_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            horror_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif genre_choice == "4":
        comedy_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            comedy_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif genre_choice == "5":
        tms_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            tms_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif genre_choice == "6":
        romance_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            romance_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

elif what == "2":
    print("                                                       Hello",name,
          "! I am Milo (•◡•) I will be your TV guide today!")
    tv_genre = "What type of TV Show would you like to watch?"
    tv_genre2 = tv_genre.center(177)
    print(tv_genre2)
    print("\n")
    tv_genre3 = "1. Adventure/Action"
    tv_genre4 = tv_genre3.center(177)
    print(tv_genre4)
    tv_genre5 = "2. Sci-Fi"
    tv_genre6 = tv_genre5.center(177)
    print(tv_genre6)
    tv_genre7 = "3. Drama"
    tv_genre8 = tv_genre7.center(177)
    print(tv_genre8)
    tv_genre9 = "4. Comedy"
    tv_genre10 = tv_genre9.center(177)
    print(tv_genre10)
    print("\n")
    global tv_genre_choice
    tv_genre_choice_list = ["1","2","3","4"]
    tv_genre_choice = input(
        "                                                                               Choose an option: ")
    print("\n")
    while tv_genre_choice not in tv_genre_choice_list:
        tv_genre_choice = input(
            "                                                                       Invalid entry. Try again please : ")
        print("\n")

    def aatv_func():
        if tv_genre_choice == "1":
            global aatv_rec
            aatv_rec = choice(aatv)
            aatv_out = "We recommend you to watch : "
            aatv_out2 = aatv_out.center(177)
            print(aatv_out2)
            print(aatv_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def scifi_func():
        if tv_genre_choice == "2":
            global scifi_rec
            scifi_rec = choice(scifi)
            scifi_out = "We recommend you to watch : "
            scifi_out2 = scifi_out.center(177)
            print(scifi_out2)
            print(scifi_rec.center(177))
            print("\n")
            global happy
            happy = input(
                "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")
            happy_list = ["yes", "no"]
            while happy not in happy_list:
                happy = input(
                    "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
                print("\n")

    def dramatv_func():
        global dramatv_rec
        dramatv_rec = choice(dramatv)
        dramatv_out = "We recommend you to watch : "
        dramatv_out2 = dramatv_out.center(177)
        print(dramatv_out2)
        print(dramatv_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def comedytv_func():
        global comedytv_rec
        comedytv_rec = choice(comedytv)
        comedytv_out = "We recommend you to watch : "
        comedytv_out2 = comedytv_out.center(177)
        print(comedytv_out2)
        print(comedytv_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    if tv_genre_choice == "1":
        aatv_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            aatv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()


    elif tv_genre_choice == "2":
        scifi_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            scifi_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif tv_genre_choice == "3":
        dramatv_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            dramatv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif tv_genre_choice == "4":
        comedytv_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            comedytv_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()


elif what == "3":
    print("                                                       Hello",name,
          "! I am Robyn (✦ ‿ ✦) I will help find you an album today!")
    album_genre = "What kind of music would you like to listen to?"
    album_genre2 = album_genre.center(177)
    print(album_genre2)
    print("\n")
    album_genre3 = "1. Hip-Hop"
    album_genre4 = album_genre3.center(177)
    print(album_genre4)
    album_genre5 = "2. Indie Alt"
    album_genre6 = album_genre5.center(177)
    print(album_genre6)
    album_genre7 = "3. R&B"
    album_genre8 = album_genre7.center(177)
    print(album_genre8)
    album_genre9 = "4. Pop"
    album_genre10 = album_genre9.center(177)
    print(album_genre10)
    print("\n")
    global album_genre_choice
    album_genre_choice_list = ["1","2","3","4"]
    album_genre_choice = input(
        "                                                                               Choose an option: ")
    print("\n")
    while album_genre_choice not in album_genre_choice_list:
        album_genre_choice = input(
            "                                                                       Invalid entry. Try again please : ")
        print("\n")

    def hiphop_func():
        global hiphop_rec
        hiphop_rec = choice(hiphop)
        hiphop_out = "We recommend you to listen to : "
        hiphop_out2 = hiphop_out.center(177)
        print(hiphop_out2)
        print(hiphop_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def indiealt_func():
        global indiealt_rec
        indiealt_rec = choice(indiealt)
        indiealt_out = "We recommend you to listen to : "
        indiealt_out2 = indiealt_out.center(177)
        print(indiealt_out2)
        print(indiealt_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")


    def randb_func():
        global randb_rec
        randb_rec = choice(randb)
        randb_out = "We recommend you to listen to : "
        randb_out2 = randb_out.center(177)
        print(randb_out2)
        print(randb_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def pop_func():
        global pop_rec
        pop_rec = choice(pop)
        pop_out = "We recommend you to listen to : "
        pop_out2 = pop_out.center(177)
        print(pop_out2)
        print(pop_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")


    if album_genre_choice == "1":
        hiphop_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            hiphop_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()


    elif album_genre_choice == "2":
        indiealt_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            indiealt_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif album_genre_choice == "3":
        randb_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            randb_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif album_genre_choice == "4":
        pop_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            pop_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

elif what == "4":
    print("                                                  Hello",name,
          "! I am Marko (─‿─) I will help you find a new book to read today!")
    book_genre = "What type of book would you like to read?"
    book_genre2 = book_genre.center(177)
    print(book_genre2)
    print("\n")
    book_genre3 = "1. Literary Fiction"
    book_genre4 = book_genre3.center(177)
    print(book_genre4)
    book_genre5 = "2. Science"
    book_genre6 = book_genre5.center(177)
    print(book_genre6)
    book_genre7 = "3. Philosophy"
    book_genre8 = book_genre7.center(177)
    print(book_genre8)
    book_genre9 = "4. Non-Fiction"
    book_genre10 = book_genre9.center(177)
    print(book_genre10)
    book_genre11 = "5. Historical Fiction"
    book_genre12 = book_genre11.center(177)
    print(book_genre12)
    book_genre13 = "6. Contemporary"
    book_genre14 = book_genre13.center(177)
    print(book_genre14)
    print("\n")
    global book_genre_choice
    book_genre_choice_list = ["1","2","3","4","5","6"]
    book_genre_choice = input(
        "                                                                               Choose an option: ")
    print("\n")
    while book_genre_choice not in book_genre_choice_list:
        book_genre_choice = input(
            "                                                                       Invalid entry. Try again please : ")
        print("\n")

    def fiction_func():
        global fiction_rec
        fiction_rec = choice(fiction)
        fiction_out = "We recommend you to read : "
        fiction_out2 = fiction_out.center(177)
        print(fiction_out2)
        print(fiction_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def science_func():
        global science_rec
        science_rec = choice(science)
        science_out = "We recommend you to read : "
        science_out2 = science_out.center(177)
        print(science_out2)
        print(science_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def philosophy_func():
        global philosophy_rec
        philosophy_rec = choice(philosophy)
        philosophy_out = "We recommend you to read : "
        philosophy_out2 = philosophy_out.center(177)
        print(philosophy_out2)
        print(philosophy_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def nonfiction_func():
        global nonfiction_rec
        nonfiction_rec = choice(nonfiction)
        nonfiction_out = "We recommend you to read : "
        nonfiction_out2 = nonfiction_out.center(177)
        print(nonfiction_out2)
        print(nonfiction_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def historicalfiction_func():
        global historicalfiction_rec
        historicalfiction_rec = choice(historicalfiction)
        historicalfiction_out = "We recommend you to read : "
        historicalfiction_out2 = historicalfiction_out.center(177)
        print(historicalfiction_out2)
        print(historicalfiction_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def contemporary_func():
        global contemporary_rec
        contemporary_rec = choice(contemporary)
        contemporary_out = "We recommend you to read : "
        contemporary_out2 = contemporary_out.center(177)
        print(contemporary_out2)
        print(contemporary_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")


    if book_genre_choice == "1":
        fiction_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            fiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif book_genre_choice == "2":
        science_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            science_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif book_genre_choice == "3":
        philosophy_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            philosophy_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif book_genre_choice == "4":
        nonfiction_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            nonfiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()


    elif book_genre_choice == "5":
        historicalfiction_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            historicalfiction_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif book_genre_choice == "6":
        contemporary_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            contemporary_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

elif what == "5":
    print("                                              Hello",name,
          "! I am Mutiny ( ⌬̀⌄⌬́ ) Let's try and find what game you're going to play next!")
    game_plat = "What platform will you be gaming on?"
    game_plat2 = game_plat.center(177)
    print(game_plat2)
    print("\n")
    game_plat3 = "1. PC"
    game_plat4 = game_plat3.center(177)
    print(game_plat4)
    game_plat5 = "2. PS4"
    game_plat6 = game_plat5.center(177)
    print(game_plat6)
    print("\n")
    global game_plat_choice
    game_plat_choice = input(
        "                                                                               Choose an option: ")
    print("\n")
    game_plat_choice_list = ["1", "2"]
    while game_plat_choice not in game_plat_choice_list:
        game_plat_choice = input(
            "                                                                       Invalid entry. Try again please : ")
        print("\n")

    def pc_func():
        global pc_rec
        pc_rec = choice(pc)
        pc_out = "We recommend you to play : "
        pc_out2 = pc_out.center(177)
        print(pc_out2)
        print(pc_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    def ps4_func():
        global ps4_rec
        ps4_rec = choice(ps4)
        ps4_out = "We recommend you to play : "
        ps4_out2 = ps4_out.center(177)
        print(ps4_out2)
        print(ps4_rec.center(177))
        print("\n")
        global happy
        happy = input(
            "                                                            Are you happy with our selection? Type 'yes' or 'no' - ").lower()
        print("\n")
        happy_list = ["yes", "no"]
        while happy not in happy_list:
            happy = input(
                "                                           Invalid entry. Please try again. Are you happy with our selection? Type 'yes' or 'no' - ").lower()
            print("\n")

    if game_plat_choice == "1":
        pc_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            pc_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()

    elif game_plat_choice == "2":
        ps4_func()
        if happy == "yes":
            happy2 = "We're glad that you like our choice!"
            happy3 = happy2.center(177)
            print(happy3)
            main_menu()
        while happy == "no":
            ps4_func()
            if happy == "yes":
                happy2 = "We're glad that you like our choice!"
                happy3 = happy2.center(177)
                print(happy3)
                main_menu()


