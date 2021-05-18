#January 6, 2020
#This game has a 14 by 14 matrix where 6 ships with the dimesnsions listed below can be put on the matrix. Then each player plays against the computer to hit all the ships that are on their opponent's matrix. The one who hits all ships first, wins the game.
import random #random imported for further use in the code
n_tracker={} #This dictionary keeps track of each player and the results of each game played by that player
#functions
#The ship_maker function makes a list of the x and ys of the 6 ships and it is used for making the list of user and computer ships                
def ship_maker():
    a=[] #list of the ships
    b=1 #current ship number
    while b<=6: 
        a.append([ ["x" , "x1"] , ["y" , "y1"] ]) 
        b+=1 
    return a 
#This function helps the computer in choosing which direction it wants to take when choosing where on the matrix to put its ships 
def computer_direction_check(a,b):
    if b!=1: 
        c=random.randint(1,2) 
        if c==1: 
            if a+(b-1)<=13: 
                d=a+(b-1) 
            if a-(b-1)>=0 and a+(b-1)>13: 
                d=a-(b-1) 
        if c==2:
            if a-(b-1)>=0: 
                d=a-(b-1) 
            if a+(b-1)<=13 and a-(b-1)<0: 
                d=a+(b-1) 
        if a+(b-1)>13 and a-(b-1)<0:  
            raise Exception
    if b==1: 
        d=a 
    return d 
#this function helps the computer have anawareness of which points it has chosen and which points are left on the matrix and can be chosen for ships to be placed in
def computer_list_maker(i,i2,j,j2,a): 
    c=max(j,j2) #maximum y coordinate number
    d=min(j,j2) #minimum y coordinate number
    e=max(i,i2) #maximum x coordinate number
    f=min(i,i2) #minimum x coordinate number
    while d<=c: 
        while f<=e:  
            a[d].remove(f) 
            f+=1
        f=min(i,i2) 
        d+=1   
    return a 
#This function checks to see if the place of the ship that is chosen by the computer is already taken or not and if it is taken, gives an error in order to have the computer choose another spot 
def empty_list_checker(i,i2,j,j2,a): 
    c=max(i,i2) #maximum x coordinate number
    d=min(i,i2) #minimum x coordinate number
    e=max(j,j2) #maximum y coordinate number
    f=min(j,j2) #minimun y coordinate number
    while f<=e: 
        while d<=c:
            if d in a[f]: 
                d+=1
            else: 
                raise Exception
        f+=1 
        d=min(i,i2) 
#This function determines the second x or y using the first x or y and the direction the player has chosen   
def distance_calculation(a,b,c): 
    e=a-1 
    if c=="left" or c=="up": 
        if b-e>=1: 
            d=b-e 
    if c=="right" or c=="down": 
        if e+b<=14: 
            d=b+e 
    return d 
#This function checks every ship's coordinates in order to make sure each ship is seperated from the other, and that two or more ships don't have any coordinates in common
def final_list_maker(i,i2,j,j2,a): 
    n=[] #n is the empty list that is used for checking if any of the spaces are already taken or not
    c=max(j,j2) #maximum number of y coordinate
    d=min(j,j2) #minimum number of y coordinate
    e=max(i,i2) #maximum number of x coordinate
    f=min(i,i2) #minimum number of x coordinate
    while d<=c: 
        if "X" not in a[d-1][f-1:e]: 
            n.append("O") 
            d+=1 
        #if any x is found in the spot that the next ship is going, an error is given in order to have the player choose another spot
        else:
           raise Exception
    if "X" not in n: 
        d=min(j,j2) 
        while d<=c: 
            a[d-1][f-1:e]=["X"]*(e-(f-1)) 
            d+=1            
    return a 

#for simplicity of the game for tha player, this function prints out the matrix in a manner that is easier to understand and follow        
def final_list_printer(a):
    c=0 
    while c<=13: 
        print(" ".join(a[c])) 
        c+=1 
#this function simply makes the matrix where the changes are applied and stored
#each matrix is a list with 14 lists inside each containing 14 elements (the original matrix only has "o"s in it and later on the ships are added as "x"s (os are replaced with xs)
def matrix_maker():
    a=[] 
    Os=0 
    while Os<=13: 
        a.append(["O"]*14) 
        Os+=1 
    return a 
#This function allows for the matrix that is number based meaning, it has 14 lists inside a list, each with numbers 0 to 13. (numbers instead of os so that it is easier for the computer to understand) 
def number_based_matrix():
    cn=0 
    rn=0 
    numbermatrix=[[]] 
    while rn<=13: 
        while cn<14: 
            numbermatrix[rn].append(cn) 
            cn+=1
        if cn==14: 
            cn=0 
            rn+=1 
            if rn!=14: 
                numbermatrix.append([]) 
    return numbermatrix 
#This function determines the coordinates that it is going to hit on the player's matrix using the first coordinate and numbers 1 or 2 to see if 1 is added or substracted from the chosen coordinate. 
def hit_direction_check(a,c):
    if c==1 or c==4: 
        d=a+1 
    if c==2 or c==3: 
        d=a-1 
    return d 
n=str(input("What is your name?")) 
n_tracker[n]=[] #a list is made so that the points of each game the user plays is added to this list
game="nq" #game is in not quited state
while game!="q": #while the game is not in the quited state
    #variables(most of them)
    asktimes=0 #the number of times that the user is asked to put an input is equal to zero
    hitpoint=0 #hitpoint is used as a key to locate certain values in the hit list
    hits=0 #Further on in the game, this list will give the number of hits the player has made 
    chits=0#Further on in the game, this list will give the number of hits the computer has made
    print("Welcome to the game " + n +". The grid is 14 by 14. You have six ships." + "\nShip 1 : 4 by 1" + "\nShip 2 : 3 by 1" + "\nShip 3 : 5 by 1" + "\nShip 4 : 4 by 1" + "\nShip 5 : 5 by 2" + "\nShip 6 : 6 by 1") #Introduce the game and the grid to the player
    i=1 #i indicates the number of times that a ship is chosen and lets the player only choose 6 ships 
    ci=1 #ci indicates the number of ships chosen by the computer
    chitcheck="no hit" #chitcheck checks to see if a hit has been made or not and indicates the difference between when no ship is hit or a ship is hit once or more
    hit=[] #This list is where the data of each hit(missed orhit after the first hit) is stored and used to make dicissions about the next hit
    firsthitpoints=[] #This list has in it the first points that have been hit 
    #the number of ships that are available to the user are stored in this list and with every number that the player picks, that ship number is removed from this list.     
    ship_tracker=[1,2,3,4,5,6]
    #Ships is a list of the players ships.(six lists and inside them, two lists, one for a min and max x and the other for a min and max y of one ship)
    Ships=ship_maker()
    #ComputerShips is a list of computers ships. (six lists and inside them, two lists, one for a min and max x and the other for a min and max y of one ship) 
    ComputerShips=ship_maker()
    #the distance list shows the space each ship will take on the matrix(they are ordered from ship 1 to 6).
    distance=[ [4 , 1] , [3 , 1] , [5 , 1] , [4 , 1] , [5 , 2] , [6 , 1] ]
    #computermatrix is a number based matrix that the computer uses for putting the ships on the right spots of the matrix(so that no two ships have any common spots).
    computermatrix=number_based_matrix()
    #usermatrix is a number based matrix that the computer understands and uses for determining where on the matrix is still left with no hits.
    usermatrix=number_based_matrix()
    #a visual computer matrix is made(for further use to help the player see where hits have been made)
    cemptylist=matrix_maker()
    #a visual matrix for the player to see where the ships are and further on where the computer has hit on the matrix
    emptylist=matrix_maker()
    #distancenumber is a list that shows the ships available to the computer(the ships that have not yet been placed on the computer matrix).
    distancenumber=[0,1,2,3,4,5]
    #while at least one ship is still left to be placed on the matrix
    while ci<=6:
        try:
            #computer randomly chooses a ship
            #random distance number(name of the list storing the 6 ships)
            rdn=random.choice(distancenumber)
            #the space the chosen ship takes is matched to the randomly picked ship using the distance list explained above
            randomship=distance[rdn]
            #the computer randomly chooses to either put ships verticaly or horizentaly on the matrix
            randomreverse=random.randint(1,2)
            #number 2 on randomreverse makes the elements of the distance list for a chosen ship reverse so that the x is y and the y is x (ships are always horzental when represented in the distance list)
            if randomreverse==2:
                randomship=randomship[::-1]
            #the y for the computer chosen ship is randomly picked(a number between 0 and 13)
            cy=random.randint(0,13)
            #the y coordinate replaces the original element in the ComputerShip's list for the chosen ship
            ComputerShips[rdn][1][0]=cy
            #the computer will need to restart if it chooses a horizetal line(list in the number based matrix) that is already empty(maybe due to it being already the place for other ships).
            #this senario is not likely to happen often since the probability of the computer choosing the ships's coordinates in such manner is extremely low
            if not computermatrix[cy]:
                raise Exception
            #by using the first y coordination chosen by the computer, the second y coordination is generated using one of the functions listed above
            cy2=computer_direction_check(cy,randomship[1])
            #the second y coordinate replaces the original element in the ComputerShip's list for the chosen ship
            #one of the ys are max while the other is the min and they fill the list from min to max
            ComputerShips[rdn][1][1]=cy2
            #the x coordinate is chosen from the numbers inside a list of computermatrix list(the number of this list is the same as the first chosen y coordinate)
            cx=random.choice(computermatrix[cy])
            #the x coordinate replaces the original element in the ComputerShip's list for the chosen ship
            ComputerShips[rdn][0][0]=cx
            #by using the first x coordination chosen by the computer, the second x coordination is generated using one of the functions listed above
            cx2=computer_direction_check(cx,randomship[0])
            #the second x coordinate replaces the original element in the ComputerShip's list for the chosen ship
            #one of the xs are max while the other is the min and they fill the list from min to max
            ComputerShips[rdn][0][1]=cx2
            #checks to make sure the place where this ship is going to be is not already taken by another one
            empty_list_checker(cx,cx2,cy,cy2,computermatrix)
        except:
            continue
        else:
            #the number of the chosen ship is removed from the list where the numbers are picked from so that the same ship is not chosen twice
            distancenumber.remove(rdn)
            #the numbers used on the matrix as a place for ships are removed from the number based matrix to avoid having them picked by the computer again
            #this makes the code run faster since there are less mistakes made by not choosing the same spot for another ship twice
            computer_list_maker(ComputerShips[rdn][0][0],ComputerShips[rdn][0][1],ComputerShips[rdn][1][0],ComputerShips[rdn][1][1],computermatrix)
            #1 is added to ci so that the loop ends after all ships have been picked
            ci+=1
    #while at least one ship is still left to be placed on the matrix
    while i<=6:
        #on each turn, the number of the ships left are displayed for the player so that the player does not choose the same ship twice(the number as if saying ship 1 and ship 6 are left not for saying how many ships are left).
        choice1="Choose the ship number:"
        for choice in ship_tracker:
            choice1+=str(choice) + ","
        try:
            a=int(input(choice1))
            if a not in ship_tracker:
                raise Exception
            #since the player chooses a number between 1 and 6 and not 0 and 5, the element in the distance can be matched with the number-1 not the number chosen itself
            a1=distance[a-1]
            print("The x and y coordination of your ship is respectively " + str(a1) + ".")
            #asks the user to press n if they want their ship to be vertical instead of horizental
            RO=str(input("press the n key if you wish to reverse it or press any other key to continue with the default coorninates"))
            #the elements in the distance list's list are reversed if the player wants the ships to be vertical
            if RO=="n":
                a1=a1[::-1]
                print(str(a1))
            #if the horizental space the ship takes is not equal to 1(if it is one then min and max x are equal since they are the same number)
            if a1[0]!=1:
                #asks the player to choose an x between 1 and 14
                x=int(input("Where is the ship x coordination beginning?(1-14)"))
                #error occurs if the player chooses one that is bigger than 14 or less than 1  
                if x>14 or x<0:
                    raise Exception
                else:
                    #the first x coordinate replaces the original element in the Ship's list for the chosen ship
                    Ships[a-1][0][0]=x
                    #asks the user if they want to go left or right
                    x_direction=str(input("Do you want to go left or right?(left/right)"))
                    #error if the answer is not left or right
                    if x_direction!="left" and x_direction!="right":
                        raise Exception
                    #the second x is calculated using the first x and functions
                    x1=distance_calculation(a1[0],x,x_direction)
                    #the second x coordinate replaces the original element in the Ship's list for the chosen ship
                    Ships[a-1][0][1]=x1
            #if the horizental space the ship takes is only 1, x2 and x1 are the same and the Ship's corresponding elements will be replaced both with x2
            if a1[0]==1:
                x2=int(input("Where do you want the x coodninate to be?(1-14)"))
                Ships[a-1][0][0]=x2
                Ships[a-1][0][1]=x2
            #if the vertical space the ship takes is not equal to 1(if it is one then min and max y are equal since they are the same number)
            if a1[1]!=1:    
                y=int(input("Where is the ship y coordination beginning? (1-14)"))
                #error occurs if the player chooses one that is bigger than 14 or less than 1
                if y>14 or y<0:
                    raise Exception
                else:
                    #the first y coordinate replaces the original element in the Ship's list for the chosen ship
                    Ships[a-1][1][0]=y
                    #asks the user if they want to go up or down
                    y_direction=str(input("Do you want to go up or down?(up/down)"))
                    #error if the answer is not up or down
                    if y_direction!="down" and y_direction!="up":
                        raise Exception
                    #the second y is calculated using the first y and functions
                    y1=distance_calculation(a1[1],y,y_direction)
                    #the second y coordinate replaces the original element in the Ship's list for the chosen ship
                    Ships[a-1][1][1]=y1
            #if the vertical space the ship takes is only 1, y2 and y1 are the same and the Ship's corresponding elements will be replaced both with y2
            if a1[1]==1:
                y2=int(input("Where do you want the y coodninate to be?(1-14)"))
                Ships[a-1][1][1]=y2
                Ships[a-1][1][0]=y2
            #the final_list_maker function replaces the right elements of the players matrix with xs and then the final_list_printer function, prints the list without commas and brackets
            matrixpoint=final_list_maker(Ships[a-1][0][0],Ships[a-1][0][1],Ships[a-1][1][0],Ships[a-1][1][1],emptylist)
            final_list_printer(matrixpoint)
        #in case of an error, the computer asks the player to reenter an input
        except:
            print("Wrong input please try again")
        else:
            #the number of the ship chosen is removed from the list of numbers and 1 is added to i indicating that a ship is already chosen
            ship_tracker.remove(a)
            i+=1
    #space for easier visualities
    print("")
    #the player only sees a matrix of os as the matrix of the computer
    final_list_printer(cemptylist)
    #space for easier visualities
    print("")
    #the player sees the final matrix(players final matrix with 6 ships on it)
    final_list_printer(matrixpoint)
    print("The O letters in the first printed matrix will change to H if a hit occurs. Otherwise, if a hit is missed, the O letter will change to M")
    #the position of hits(up,down,left,right) is already chosen for the computer(since it has little impact on the game's outcome)
    posneg=[1,2,3,4]
    #while no one has won(each player has to make 32 hits in order to win) 
    while hits<32 and chits<32:
        #the biggest try loop prevents the game being continued by either the player or the computer in case of an error in any one of them
        #throughout the whole game, "M" is an indication of a miss and "H" is an indication of a hit 
        try:
            try:
                if asktimes<1: #if the asktimes is zero(less than 1)
                    #asks the player wher they want to hit on their opponents matrix(first x and then y)
                    #the coordinates chosen cannot be less than zero or bigger than 14
                    hx=int(input("which x ccordination do you want to hit?(1-14)"))
                    if hx>14 or hx<0:
                        raise Exception
                    hy=int(input("which y ccordination do you want to hit?(1-14)"))
                    if hy>14 or hy<0:
                        raise Exception
                    #the chosen coordinates cannot be the ones that have already been chosen
                    if cemptylist[hy-1][hx-1]=="M" or cemptylist[hy-1][hx-1]=="H":
                        raise Exception
                    #once the user gives an input to the computer, 1 is added to the asktimes
                    asktimes+=1
            except:
                print("wrong input please try again")
                raise Exception
            try:
                #if there be no element left in the posneg list, the chitcheck will be changed to no hit and the lists get refilled        
                if len(posneg)==0:
                    posneg=[1,2,3,4]
                    chitcheck="no hit"
                #go indicates if the while loop will run or not 
                go="y"
                #chitcheck indicates if a hit has been made or not and proceeds to continue if a hit has been made
                if chitcheck=="hit":
                    try:
                       #while go has its value equal to "y", the loop will continue
                        while go=="y":
                            #if the first element in the posneg list is 1 or 3, x remains the same while y changes(vertical movement)
                            if posneg[0]==1 or posneg[0]==3:
                                #checks to see if the point it is about to hit, is not a previousley missed or hit point and checks to see if by adding 1 to or substracting 1 from the y, the y becomes less than 0, or more than 13, or not
                                if hitforwardx1 in usermatrix[hit_direction_check(hitforwardy1,posneg[0])] and hit_direction_check(hitforwardy1,posneg[0])>=0 and hit_direction_check(hitforwardy1,posneg[0])<=13:
                                    #x remains the same as when a hit was made
                                    hitforwardx1=firsthitpoints[0][0]
                                    #if the statements above are true, the hit_direction_check function adds 1 to or substracts 1 from the y point chosen by the computer(the y in the hits)
                                    hitforwardy1=hit_direction_check(hitforwardy1,posneg[0])
                                    go="n"
                                else:
                                    #the points are moved back to the first hit points and the first element of the posneg list is deleted
                                    del posneg[0]
                                    #the value of hitforwardx1 and hitforwardy1 are returned to the first hit values
                                    hitforwardx1=firsthitpoints[0][0]
                                    hitforwardy1=firsthitpoints[0][1]
                            #if the first element in the posneg list is 2 or 4, y remains the same while x changes(horizental movement)            
                            if posneg[0]==2 or posneg[0]==4:
                                #checks to see if the point it is about to hit, is not a previousley missed or hit point and checks to see if by adding 1 to or substracting 1 from the x, the x becomes less than 0, or more than 13, or not
                                if hit_direction_check(hitforwardx1,posneg[0]) in usermatrix[hitforwardy1]:
                                    #y remains the same as when a hit was made
                                    hitforwardy1=firsthitpoints[0][1]
                                    #if the statements above are true, the hit_direction_check function adds 1 to or substracts 1 from the x point chosen by the computer(the x in the hits)
                                    hitforwardx1=hit_direction_check(hitforwardx1,posneg[0])
                                    go="n"      
                                else:
                                    #the points are moved back to the first hit points and the first element of the posneg list is deleted
                                    del posneg[0]
                                    #the value of hitforwardx1 and hitforwardy1 are returned to the first hit values
                                    hitforwardx1=firsthitpoints[0][0]
                                    hitforwardy1=firsthitpoints[0][1]
                        #the hitforwardx1 number is removed from a list inside the user matrix with the same index as hitforwardy1    
                        usermatrix[hitforwardy1].remove(hitforwardx1)
                    #in case of an error, the first elements prosneg list will be deleted(if it has an element inside them). Otherwise, the code will just continue as no hit                             
                    except:
                        if len(posneg)==0:
                            posneg=[1,2,3,4]
                            chitcheck="no hit"
                            go="n"
                        else:
                            del posneg[0]
                            #the value of hitforwardx1 and hitforwardy1 are returned to the first hit values
                            hitforwardx1=firsthitpoints[0][0]
                            hitforwardy1=firsthitpoints[0][1]
                        
                    else:
                        #if the computer chosen point is an x on the players matrix, then there is a hit and otherwise there is a miss
                        if matrixpoint[hitforwardy1][hitforwardx1]!="X":
                            matrixpoint[hitforwardy1][hitforwardx1]="M"
                            #in case of a miss the points are set back to their original hit points(coordinates of the first hit) and the first elements of udlr and posneg list ane deleted
                            hitforwardx1=firsthitpoints[0][0]
                            hitforwardy1=firsthitpoints[0][1]
                            del posneg[0]
                        #in case of a hit, a point is added to chits
                        if matrixpoint[hitforwardy1][hitforwardx1]=="X":
                            matrixpoint[hitforwardy1][hitforwardx1]="H"
                            chits+=1      
                
                if chitcheck=="no hit":
                    #the index of every list that is not empty inside the user matrix list is added to the indexes list
                    indexes=[i for i, n in enumerate(usermatrix) if len(n)!=0]
                    chy=random.choice(indexes) #chy is a random index chosen from the indexes list
                    #a random x is chosen from the list that was chosen before as chy
                    chx=random.choice(usermatrix[chy])
                    #if the point on the players matrix corresponding to these coordinates were x, a hit would be made. Otherwise, there would be a miss
                    #in case of a hit, chitcheck will change to hit and a point is added to the computers points(chits)
                    if matrixpoint[chy][chx]!="X" and matrixpoint[chy][chx]!="H" and matrixpoint[chy][chx]!="M":
                        matrixpoint[chy][chx]="M"
                        chitcheck="no hit"
                    if matrixpoint[chy][chx]=="X":
                        matrixpoint[chy][chx]="H"
                        chits+=1
                        #for the first chits, the computer add the coordinates to the list of the first hit points
                        if chits==1:
                            firsthitpoints.append([chx,chy])
                        #for other chits, the computer replaces the old coordinates with the new ones
                        if chits>1:
                            firsthitpoints[0][0]=chx
                            firsthitpoints[0][1]=chy
                        hitforwardx1=firsthitpoints[0][0]
                        hitforwardy1=firsthitpoints[0][1]
                        chitcheck="hit"
                    #these coordinates are removed from the usermatrix in order to prevent them from getting picked again
                    usermatrix[chy].remove(chx)
            except:
                continue
                
        except:
            continue
        else:
            asktimes=0 #if both the computer and the user make no mistakes, then the asktimes will equal to zero so that an input is asked from the user in the next round
            #in case of no errors, the places were the player has hit will be replaced with hs in hit instances or they will be replaced with ms in miss instances
            #if a hit occurs, the player will gain points(hits)
            if (hx-1) not in computermatrix[hy-1]:
                cemptylist[hy-1][hx-1]="H"
                hits+=1
            if (hx-1) in computermatrix[hy-1]:
                cemptylist[hy-1][hx-1]="M"
            #the matrixes are printed out for the player to keep track of
            final_list_printer(cemptylist)
            #space for easier visualities
            print(" ")
            final_list_printer(matrixpoint)
            #who ever gets 32 points first will win the game and the player can play again or quit
            if hits==32 and chits<32:
                results="You Won"
                print("You Won")
            if chits==32 and hits<32:
                results="You Lost"
                print("You Lost")
            if chits==32 or hits==32:
                #the results of the game will be added to the n dictionary to keep track of players
                n_tracker[n].append((n,hits,chits,results))
                playover=input("Do you wish to play again? y/n")
                if playover=="y":
                    continue
                if playover!="y":
                    print("Thank You For Playing")
                    print("Your scores were as fallows: " + n_tracker[n])
                    game="q"




        
        
            
        
            
                
        
    
    
    
    
       











