#Meira Rihanna
#1/10
#To-do list

#Main
MovieList = ["Star Wars", "Barbie", "A Ballad of Songbirds and Snakes", "Night School"]
print("Welcome to your Movie List")
print("Please choose option: (Type in a number between 1-5)")
print("""1. View List \n2. Add to list \n3. Check as Complete \n4. Remove movie \n5. Quit 
    \n6. Remove all tasks \n7. Sort list in alphabetical order \n8. Print # of items on the list""")
option = int(input("Option:"))

if (option == 1):
    print(MovieList)

elif (option == 2):
    MovieList.append(input("What would you like to add to your list?"))
    print(MovieList)

elif (option == 3):
    ans = input("Please enter a movie name from the list to mark as Complete: ")
    i = MovieList.index(ans)
    MovieList[i] = ans + ": X"
    print(MovieList)
    
elif (option == 4):
    MovieList.pop(int(input("What movie # on the list do you want to remove?")))
    print(MovieList)

elif (option == 5):
    quit()

elif (option == 6):
    MovieList.clear()
    print(MovieList)

elif (option == 7):
    MovieList.sort()
    print(MovieList)

elif (option == 8):
    print(len(MovieList))

