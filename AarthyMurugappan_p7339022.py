from movies import Movie
#{}.FORMAT retrieves the data set in side the parentisis
def PrintMovieDetails(Movie):
    print("Name: {}".format(Movie.getName()))
    print("Category: {}".format(Movie.getCategory()))
    print("Description: {}".format(Movie.getDescription()))
    print("Price: {}".format(Movie.getPrice()))
    print("Price with GST: {}".format(Movie.GetPricewithGST()))


def PrintAllMovieDetails(listofmovies):
    print()
    print("Printing All Movies")
    print()
    print(70 * "-")
    for movie in listofmovies:
        PrintMovieDetails(movie)
        print(70 * "-")
    print()
    print()

def SearchBasedOnNameOrCategory(searchString, listOfMovies):
    for movie in listOfMovies:
        if movie.getName() == searchString.lower():
            return movie
    return None


def readMovies():
    listofmovies = []
    file = open("C:\\Users\\gayat\\Desktop\\web dev\\pyassnS_2_01\\movlist.txt")
    lines = file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        content = line.split("|")
        # print(content)
        movie_obj = Movie(content[0], content[1], content[2], content[3])
        listofmovies.append(movie_obj)
    return listofmovies


listofmovies = readMovies()
# PrintAllMovieDetails(listofmovies)


def mainmenu():
    print(30 * "-", "MAIN MENU", 30 * "-")
    print("1. Display all Moivies")
    print("2. Display movie full names for selection")
    print("3. Search based on Name or Category substring")
    print("Q. Enter Q to quit")
    print(67*"-")
    menuSelection = input("Please input your selection\n")
    print(67*"-")
    print("You have selected "+menuSelection+".. ",end="")

    if menuSelection == "Q":
        return
    elif menuSelection == "1":
        menu1()
    elif menuSelection == "2":
        menu2()
    elif menuSelection == "3":
        menu3()




def menu1():
    try:
        print("\n Display all Movies")
        index = 0
        userinput = ""
        while userinput != "M":
            if userinput == "N":
                if index < len(listofmovies)-1:
                    index += 1
                else:
                    index = 0
                print("Index {}".format(index))
            elif userinput == "P":
                if index >= 0:
                    index -= 1
                else:
                    index = len(listofmovies) - 1

            print("\nMovie "+str(index+1)+" of "+str(len(listofmovies)))
            print("=============================================")
            PrintMovieDetails(listofmovies[index])
            print("=============================================")
            print("Enter N for Next movie")
            print("Enter P for Previous movie")
            userinput = input("Enter M to return to Main Menu\n")
            if userinput == "M":
                mainmenu()

    except IndexError:
        print("Index Error occurred")




def menu2():
    try:
        print("\n\n Display movie full names for selection")
        index = 0
        userinput = ""
        while userinput != "M":
            if userinput == "N":
                if index < len(listofmovies)-1:
                    index += 1
                else:
                    index = 0
                print("Index {}".format(index))
            elif userinput == "P":
                if index >= 0:
                    index -= 1
                else:
                    index = len(listofmovies) - 1

            print("\nMovie "+str(index+1)+" of "+str(len(listofmovies)))
            print("=============================================")
            print("Movie full name: {} " .format(listofmovies[index].getName()))
            print("=============================================")
            print("Enter N for Next movie")
            print("Enter P for Previous movie")
            print("Enter E for details")
            userinput = input("Enter M to return to Main Menu\n")
            
            if userinput == "E":
                PrintMovieDetails(listofmovies[index])
            if userinput == "M":
                mainmenu()


    except IndexError:
        print("IndexError occurred")


def menu3():
    print("\n\nSearch based on Name or Category substring")
    userinput = ""
    while True:
        userinput = input("please enter your search input\n")
        movie = SearchBasedOnNameOrCategory(userinput, listofmovies)
        if movie is not None:
            print("MOVIE FOUND: {}".format(userinput))
            print()
            print("=============================================")
            PrintMovieDetails(movie)
            print("=============================================")
            print()
        else:
            print("No movie found with the {} search string".format(userinput))
        
        while userinput != "1" and userinput != "2":
                print("1. Search again")
                userinput = input("2. Return to Main Menu\n")

        if userinput == "2":
            mainmenu()


mainmenu()
