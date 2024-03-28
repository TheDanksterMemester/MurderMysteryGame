import sys

#this is the state function where the state is stored
def game_state():
    state = {
        'current_map': get_maps(1),
        'player_position': 1,
        'clue_score': 0,
        'interaction_list': [],
        'item_list' : [] ,
        'door_unlocked' : 0,
        'lady_awake' : 0
    }
    #the state here stores all the important information of the game. 
    #The map position, the position of player, the amount of clues,
    #the special interactions, and such.

    show_board(state['current_map'])
    user_movement(state)

#this is the maps function where all the maps are being stored.
#All map art is stored in here
def get_maps(choice):
  MVP_map_1 = {

        1: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ &                 @ │          ",
          "│     │          x          │          ",
          "│                           │          ",
          "│     │                     │          ",
          "│ =   │        =   =        │          ",
          "└─────└─────┌──── ────┐─────┘          ",
          "            │$       =│                ",
          "            │         |                ",
          "            │         │                ",
          "            └────!────┘                "
          ),

      2: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ &                 @ │          ",
          "│     │          x          │          ",
          "│                           │          ",
          "│     │                     │          ",
          "│ =   │        =   =        │          ",
          "└─────└─────┌──── ────┐─────┘          ",
          "            │$       =│                ",
          "            │!        |                ",
          "            │         │                ",
          "            └──── ────┘                "
          ),
       3:(
           "┌─────┌─────────────────────┐          ",
           "│[]   │/                  & │          ",
           "│#            =====         │          ",
           "│     │                     │          ",
           "│──-──+─────────────────────│          ",
           "│     │ &                 @ │          ",
           "│     │          x          │          ",
           "│                           │          ",
           "│     │                     │          ",
           "│ =   │        =   =        │          ",
           "└─────└─────┌──── ────┐─────┘          ",
           "            │$      !=│                ",
           "            │         |                ",
           "            │         │                ",
           "            └──── ────┘                "
           ),

       4: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ &                 @ │          ",
          "│     │          x          │          ",
          "│                           │          ",
          "│     │                     │          ",
          "│ =   │        =   =        │          ",
          "└─────└─────┌────!────┐─────┘          ",
          "            │$       =│                ",
          "            │         |                ",
          "            │         │                ",
          "            └──── ────┘                "
          ),


      5: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ &                 @ │          ",
          "│     │          x          │          ",
          "│                           │          ",
          "│     │                     │          ",
          "│ =   │        = ! =        │          ",
          "└─────└─────┌──── ────┐─────┘          ",
          "            │$       =│                ",
          "            │         |                ",
          "            │         │                ",
          "            └──── ────┘                "
          ),

      6: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ &                 @ │          ",
          "│     │          x          │          ",
          "│                !          │          ",
          "│     │                     │          ",
          "│ =   │        =   =        │          ",
          "└─────└─────┌──── ────┐─────┘          ",
          "            │$       =│                ",
          "            │         |                ",
          "            │         │                ",
          "            └──── ────┘                "
          ),
      7: (
          "┌─────┌─────────────────────┐          ",
          "│[]   │/                  & │          ",
          "│#            =====         │          ",
          "│     │                     │          ",
          "│──-──+─────────────────────│          ",
          "│     │ & !               @ │          ",
          "│     │          x          │          ",
          "│                           │          ",
          "│     │                     │          ",
          "│ =   │        =   =        │          ",
          "└─────└─────┌──── ────┐─────┘          ",
          "            │$       =│                ",
          "            │         |                ",
          "            │         │                ",
          "            └──── ────┘                "
          ),
      8:(
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                !@ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      9: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│     !                     │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      10: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │       !=   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      11: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =!       │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      12: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│    !                      │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      13: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ = ! │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      14: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──-──+─────────────────────│          ",
        "│  !  │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      15: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│──!──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      16: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#            =====         │          ",
        "│  !  │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      17: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#!           =====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      18: (
        "┌─────┌─────────────────────┐          ",
        "│[] ! │/                  & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      19: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#    !       =====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      20: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#     !      =====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),
      21: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                  & │          ",
        "│#           !=====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),

      22: (
        "┌─────┌─────────────────────┐          ",
        "│[]   │/                ! & │          ",
        "│#            =====         │          ",
        "│     │                     │          ",
        "│── ──+─────────────────────│          ",
        "│     │ &                 @ │          ",
        "│     │          x          │          ",
        "│                           │          ",
        "│     │                     │          ",
        "│ =   │        =   =        │          ",
        "└─────└─────┌──── ────┐─────┘          ",
        "            │$       =│                ",
        "            │         |                ",
        "            │         │                ",
        "            └──── ────┘                "
        ),
  }

  return MVP_map_1.get(choice, "Invalid choice")

#this function is used to print out the map as I want it to.
def show_board(board):
    for line in board:
        print(line)

#this is the user commands function where it provides the player with options
#on where to move on the map and whether if they would want to interact with
#an item/npc.
def user_commands(state):

  print('\nChoose an option you would like to do.\n')

  if state['player_position'] == 1 or state['player_position'] == 2 or state['player_position'] == 3 or state['player_position'] == 4:

    print('1) Move to initial position')
    print('2) Move to Mr Dollar ($)')
    print('3) Move to desk (=)')
    print('4) Move to main lounge enterance')
    print('5) --Interactions--')

    if state['player_position'] == 4:
      print('6) Go to the main lounge area')

  if state['player_position'] == 5 or state['player_position'] == 6 or state['player_position'] == 7 or state['player_position'] == 8 or state['player_position'] == 9 or state['player_position'] == 10 or state['player_position'] == 11 :

    print('1) Move to dead body of Xavier (x)')
    print('2) Move to dining hall enterance ')
    print('3) Move to Miss Anderson (&)')
    print('4) Move to Attinburgh Senior (@)')
    print('5) Move to left desk (=)')
    print('6) Move to right desk (=)')
    print('7) --Interactions--')
    print('8) Move Back to main lounge enterance')

    if state['player_position'] == 9:
      print('9) Go to the corridor area')

  if state['player_position'] == 12 or state['player_position'] == 13 or state['player_position'] == 14 or state['player_position'] == 15:

    print('1) Move to desk (=)')
    print('2) Move to locked kitchen door')
    print('3) --Interactions--')
    print('4) Move back to corridor enterance')

    if state['player_position'] == 14 and 'door_key' in state['item_list'] and state['door_unlocked'] >= 1:
      print('5) Move to kitchen door enterance.')

    if state['player_position'] == 15:
      print('6) Enter Kitchen')

  if state['player_position'] == 16 or state['player_position'] == 17 or state['player_position'] == 18 or state['player_position'] == 19:

    print('1) Move to stove (#)')
    print('2) Move to fridge ([])')
    print('3) Move to dining room enterance ')
    print('4) --Interactions--')
    print('5) Move back to kitchen door enterance. ')

    if state['player_position'] == 19:
      print('6) Enter dining room') 

  if state['player_position'] == 20 or state['player_position'] == 21 or state['player_position'] == 22:

    print('1) Move to dining table (=====)')
    print('2) Move to passed out servant (&)')
    print('3) Move back to dining room enterance.')
    print('4) --Interactions--')

  print('\n0) Exit game\n')

  #the print function (bottom) keeps on displaying the message at the very bottom.
  #repeatedly. This is a design choice. 
  #It was done so that the player would be constantly reminded of what they
  #needed to do after they collected all the clues.
  
  if state['clue_score'] == 6:

    print('''
      you have discovered all the clues needed
      to arrest a person. Make sure though, that you know
      who you are arresting. Remember all the conversations
      and clues you have found.

      Arrest the right person and you WIN!
      Arrest the wrong person and you LOSE!

      Good luck!
      
      ''')
       
#these two function are used to make the player move based on 
#the command from the user_commands(state) function.
def user_movement(state):
    user_commands(state)
    run = True
    while run:

      #This code here checks that if the number input is actually a letter, itll then 
      #print out this error message so that the game doesnt break.
      choice = input('Enter the number of the option you would like to perform: ')

      if not choice.isnumeric():
        print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')

      else:
        choice = int(choice)
      

      if state['player_position'] == 1 or state['player_position'] == 2 or state['player_position'] == 3 or state['player_position'] == 4:

        if choice == 1:
            user_movement_function(state,1)
        
        elif choice == 2:
            user_movement_function(state,2)

        elif choice == 3:
            user_movement_function(state,3)

        elif choice == 4:
            user_movement_function(state,4)

        elif choice == 5:
            interactions_menu(state)

        elif state['player_position'] == 4 and choice == 6:
            user_movement_function(state,5)

        elif choice == 0:
          exit()

        else: 
          print('\n--Invalid choice. Please choose provided options--\n')
          show_board(state['current_map'])
          user_commands(state)

      elif state['player_position'] == 5 or state['player_position'] == 6 or state['player_position'] == 7 or state['player_position'] == 8 or state['player_position'] == 9 or state['player_position'] == 10 or state['player_position'] == 11:

        if choice == 1:
          user_movement_function(state,6)

        elif choice == 2:
          user_movement_function(state,9)

        elif choice == 3:
          user_movement_function(state,7)

        elif choice == 4:
          user_movement_function(state,8)

        elif choice == 5:
          user_movement_function(state,10)

        elif choice == 6:
          user_movement_function(state,11)

        elif choice == 7:
          interaction_menu_room_2(state)

        elif choice == 8:
          user_movement_function(state,4)


        elif state['player_position'] == 9 and choice == 9:
          user_movement_function(state,12)

        elif choice == 0:
          exit()

        else: 
          print('\n--Invalid choice. Please choose provided options--\n')
          show_board(state['current_map'])
          user_commands(state)


      elif state['player_position'] == 9 or state['player_position'] == 12 or state['player_position'] == 13 or state['player_position'] == 14 or state['player_position'] == 15:

        if choice == 1:
          user_movement_function(state,13)

        elif choice == 2:
          user_movement_function(state,14)

        elif choice == 3:
          interaction_menu_room_3(state)

        elif choice == 4:
          user_movement_function(state,9)

        elif state['player_position'] == 14 and choice == 5:
          user_movement_function(state,15)

        elif state['player_position'] == 15 and choice == 6:
          user_movement_function(state,16)

        elif choice == 0:
          exit()
          
        else: 
          print('\n--Invalid choice. Please choose provided options--\n')
          show_board(state['current_map'])
          user_commands(state)

      elif state['player_position'] == 16 or state['player_position'] == 17 or state['player_position'] == 18 or state['player_position'] == 19:

        if choice == 1:
          user_movement_function(state,17)

        elif choice == 2:
          user_movement_function(state,18)

        elif choice == 3:
          user_movement_function(state,19)

        elif choice == 4:
          interaction_menu_room_4(state)

        elif choice == 5:
          user_movement_function(state,15)

        elif state['player_position'] == 19 and choice == 6:
          user_movement_function(state,20)

        elif choice == 0:
          exit()

        else: 
          print('\n--Invalid choice. Please choose provided options--\n')
          show_board(state['current_map'])
          user_commands(state)

      elif state['player_position'] == 20 or state['player_position'] == 21 or state['player_position'] == 22:

        if choice == 1:
          user_movement_function(state,21)

        elif choice == 2:
          user_movement_function(state,22)

        elif choice == 4:
          interaction_menu_room_5(state)

        elif choice == 3:
          user_movement_function(state,19)

        elif choice == 0:
          exit()

        else: 
          print('\n--Invalid choice. Please choose provided options--\n')
          show_board(state['current_map'])
          user_commands(state)
          
      
      else:
        print('\n--Invalid choice. Please choose provided options--\n')
        show_board(state['current_map'])

#this is the exit function. this ends the game if the user wishes to
def exit():
  print('\n --Thank you for playing!-- \n')
  run = False 
  sys.exit()
  

#depending on in which room the player is and in what position of the map they are in, 
#these sets of functions will provide the interaction options that the player can do.
#For example, This one is for the first room (Enterance)
def interactions_menu(state):
  run = True
  while run:

    if state['player_position'] == 2:
        print('\n--INTERACTION OPTIONS--\n')
        print('1) Talk to Mr Dollar')
        print('2) Investigate Mr Dollar')

        if state['clue_score'] == 6:
          print('3) ARREST MR DOLLAR')

    if state['player_position'] == 3:
        print('\n--INTERACTION OPTIONS--\n')
        print('1) Investigate the desk')

    print('\n0) Back to move menu\n')

    inter_choice = input('Enter the number of interction you would like to perform: ')
    #This code here checks that if the number input is actually a letter, itll then 
    #print out this error message so that the game doesnt break.
    if inter_choice.isnumeric() == False:
      print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')
    else:
      inter_choice = int(inter_choice)
      
    if state['player_position'] == 1 and inter_choice == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    if state['player_position'] == 2:
      Mr_Dollar_inter(state, inter_choice, run)

      if inter_choice == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    elif  state['player_position'] == 3:
      interactions_desk(state, inter_choice, run)

      if inter_choice == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    if state['player_position'] == 4 and inter_choice == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

#This function provides all the interaction options for room 2 (The Living area)
def interaction_menu_room_2(state):
  run = True
  while run:

    if state['player_position'] == 6:
        print('\n--INTERACTION OPTIONS--\n')
        print('1) Investigate the corpse')

    if state['player_position'] == 7:
          print('\n--INTERACTION OPTIONS--\n')
          print('1) Talk to Miss Anderson')
          print('2) Investigate Miss Anderson')
          print('3) Ask for any possible suspects')

          if state['clue_score'] == 6:
            print('4) ARREST MISS ANDERSON')

    if state['player_position'] == 8:
          print('\n--INTERACTION OPTIONS--\n')
          print('1) Talk to Attinburg Senior')
          print('2) Investigate Attinburg Senior')
          print('3) Ask for any possible suspects')

          if state['clue_score'] == 6:
            print('4) ARREST Attinburg Senior')

    if state['player_position'] == 10:
          print('\n--INTERACTION OPTIONS--\n')
          print('1) Investigate the left desk')

    if state['player_position'] == 11:
          print('\n--INTERACTION OPTIONS--\n')
          print('1) Investigate the right desk')

    print('\n0) Back to move menu\n')

    inter_choice_2 = input('Enter the number of interaction you would like to perform: ')
    
    if inter_choice_2.isnumeric() == False:
      print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')
    else:
      inter_choice_2 = int(inter_choice_2)

    if state['player_position'] == 6:
      corpse_interaction(state, inter_choice_2, run)

      if inter_choice_2 == 0:
            show_board(state['current_map'])
            user_commands(state)
            run = False

    elif state['player_position'] == 7:
      Miss_Anderson_inte(state, inter_choice_2, run)

      if inter_choice_2 == 0:
          show_board(state['current_map'])
          user_commands(state)
          run = False

    elif state['player_position'] == 8:
      Attinburg_Sen_inter(state, inter_choice_2, run)

      if inter_choice_2 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    elif state['player_position'] == 10:
        left_desk(state, inter_choice_2, run)

        if inter_choice_2 == 0:
          show_board(state['current_map'])
          user_commands(state)
          run = False

    elif state['player_position'] == 11:
        right_desk(state, inter_choice_2, run)

        if inter_choice_2 == 0:
          show_board(state['current_map'])
          user_commands(state)
          run = False

    if state['player_position'] == 9 and inter_choice_2 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

    if state['player_position'] == 5 and inter_choice_2 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

#This function provides all the interaction options for room 3 (Corridor)
def interaction_menu_room_3(state):
  run = True
  while run:

    if state['player_position'] == 13:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) Investigate the desk ')

    if state['player_position'] == 14:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) open kitchen door')

    print('\n0) Back to move menu\n')

    inter_choice_3 = input('Enter the number of interction you would like to perform: ')

    if inter_choice_3.isnumeric() == False:
      print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')
    else:
      inter_choice_3 = int(inter_choice_3)

    if state['player_position'] == 13:
      corridor_desk(state, inter_choice_3, run)

      if inter_choice_3 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    elif state['player_position'] == 14 :
      kitchen_door(state, inter_choice_3, run)

      if inter_choice_3 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    if state['player_position'] == 12 and inter_choice_3 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

    if state['player_position'] == 15 and inter_choice_3 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

#This function provides all the interaction options for room 4 (The kitchen)
def interaction_menu_room_4(state):
  run = True
  while run:

    if state['player_position'] == 17:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) Investigate the stove ')

    if  state['player_position'] == 18:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) Investigate the fridge')

    print('\n0) Back to move menu\n')

    inter_choice_4 = input('Enter the number of interction you would like to perform: ')

    if inter_choice_4.isnumeric() == False:
      print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')
    else:
      inter_choice_4 = int(inter_choice_4)

    if state['player_position'] == 17:
      Stove_inter(state, inter_choice_4, run)

      if inter_choice_4 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    elif state['player_position'] == 18:
      fridge_inter(state, inter_choice_4, run)

      if inter_choice_4 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    if state['player_position'] == 16 and inter_choice_4 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

    if state['player_position'] == 19 and inter_choice_4 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False

#This function provides all the interaction options for room 5 (The dining hall)
def interaction_menu_room_5(state):

  run = True
  while run:

    if state['player_position'] == 21:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) Investigate the dining table ')

    if state['player_position'] == 22:
      print('\n--INTERACTION OPTIONS--\n')
      print('1) check on the woman')

      if state['player_position'] == 22 and 'Lemonade' in state['item_list'] and state['lady_awake'] == 1:
        print('2) interrogate woman ')

      if state['clue_score'] == 6:
        print('3) ARREST THE HOUSEMAID')

    print('\n0) Back to move menu\n')

    inter_choice_5 = int(input('Enter the number of interction you would like to perform: '))

    if inter_choice_5.isnumeric() == False:
      print('\nPlease input a number, NOT A LETTER FROM THE ALPHABET!!!!!!')
    else:
      inter_choice_5 = int(inter_choice_5)

    if state['player_position'] == 21:
      dining_table_int(state, inter_choice_5, run)

      if inter_choice_5 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    elif state['player_position'] == 22:
      Passed_out_woman_int(state, inter_choice_5, run)

      if inter_choice_5 == 0:
        show_board(state['current_map'])
        user_commands(state)
        run = False

    if state['player_position'] == 20 and inter_choice_5 == 0:
      show_board(state['current_map'])
      user_commands(state)
      run = False
      
def user_movement_function(state, position):

  state['current_map'] = get_maps(position)
  state['player_position'] = position
  show_board(state['current_map'])
  user_commands(state) #This function here is made to remove any unessesary code. this simplifies things by SO MUCH
  
#This is the interaction function for the Mr_dollar interaction
def Mr_Dollar_inter(state, choice, run):
    if choice == 1:
      print('''\n
      You decide to speak to Mr Dollar. At first glances, 
      he seems to be quite a rich and snobbish man. 
      A materialistic person. When asked about his death,
      he starts to loudly cry.
      He speaks of him as though his death was inevitable.
      When further asked on this, he simply says
      that he was messing with the wrong person and then
      speaks no more of it....
      \n''')

    elif choice == 2:
      characteristic = '$'
      if characteristic not in state['interaction_list']:
          print('''\n
          You start to study Mr Dollar.
          Upon further inspection you seem to notice somthing....
          You seem to have found some blood on his navy blue blazer. 
          You have found a clue!!
          ''')
          state['interaction_list'].append(characteristic)
          state['clue_score'] += 1
          print(f'\nYou now have {state["clue_score"]} clues')

    elif choice == 0:
      run = False


    elif state['clue_score'] == 6 and choice == 3:

      print('''
        You have now arrested Mr Dollar for murder!!!
        He now goes to prison!
        You solved the case!!
        WELL DONE!!  
      ''')
      sys.exit() 
      
    else:
      print('\n--Invalid interaction option--\n')

#this is the interaction function for the desk interaction in room 1 (Enterance)
def interactions_desk(state, choice, run):
    if choice == 1:
      characteristic = '='
      if characteristic not in state['interaction_list']:
            print('''\n
            You have investigated the desk. 
            You seem to have found a bloody knife inside. 
            You have found a clue!!
            ''')
            state['interaction_list'].append(characteristic)
            state['clue_score'] += 1
            print(f'\nYou now have {state["clue_score"]} clues')
      else:
            print('''\n
            You have already investigated the desk and found the clue.
            No need to investigate here again.
            ''')
            print(f'You now have {state["clue_score"]} clues')

    elif choice == 0:
        run = False  

    else:
        print('\n--Invalid interaction option--\n')

#this is the interaction function for the corpse (x) thats in room 2 (The living area)
def corpse_interaction(state, choice, run):
  if choice == 1:
    characteristic = 'x'
    if characteristic not in state['interaction_list']:

          print('''\n
          You have investigated the corpse of Xavier. 
          He lies dead in a pool of his own blood.
          You seem to notice a lot of stab wounds all over his chest,
          piercing his heart and lungs, causing a painful death. 
          You now know that Xavier was murdered by using a large knife.
          ''')

          state['interaction_list'].append(characteristic)
          state['clue_score'] += 1
          print(f'\nYou now have {state["clue_score"]} clues')
    else:
          print('''\n
            You have already investigated the corpse of Xavier 
            and found a clue. No need to investigate here again.
            ''')
          print(f'You now have {state["clue_score"]} clues')

  elif choice == 0:
    run = False  

  else:
    print('\n--Invalid interaction option--\n')

#this is the interaction function for the NPC Miss Anderson (&) in room 2 (The Living Area)
def Miss_Anderson_inte(state, choice, run):
  if choice == 1:
    print('''\n
    You decide to speak to Miss Anderson. 
    You can't help but feel attracted to her due to her beauty.
    You ask her why she was here at this Mansion. 
    She explains that she was invited to celebrate Xavier's birthday.
    She seems horrified at his death....
    ''')

  elif choice == 2:
    print('''\n
      You decide to investigate Miss Anderson. 
      Observing her, she doesn't seem to have any
      sort of blood stains on her person. She also seems
      shaken at Xavier's death. 
    ''')
  elif choice == 3:

    print('''\n
      You decide to ask Miss Anderson for any possible suspects.
      She says that Xavier was a beloved and generous man, 
      far more superior than Mr Dollar.
      She seems to not like Mr Dollar quite a bit.
      You ask if she thinks Mr Dollar could've murdered him.
      She says that though she thinks that Mr Dollar is an 
      intolerable blowhard, she doesn't think he has it in 
      him to kill Xavier.....
    ''')
  elif choice == 0:
    run = False


  elif state['clue_score'] == 6 and choice == 4:

    print('''
      You have now arrested Miss Anderson 
      for murder!!! She now goes to prison!
      Unfortunatly YOU ARRESTED THE WRONG PERSON
      YOU LOOOOOOSEEEEEEEEE!!  
    ''')
    sys.exit()

  else:
    print('\n--Invalid interaction option--\n')

    
#this is the interaction function for the NPC Attinburg Senior (@) in room 2 (The Living Area)
def Attinburg_Sen_inter(state, choice, run):
  if choice == 1:
      print('''\n
      You decide to speak to Attinburg Senior. 
      At first glances, he seems like quite a pleasant man
      He sports a nice red overcoat while wearing a black tuxido 
      underneath.
      When asked about Xavier's death, he looked quite shocked.
      He says that he never thought he would see his good friend
      die so savagely.....
      ''')

  elif choice == 2:
      print('''\n
        You decide to investigate Attinburg Senior. 
        Observing him, You dont seem to notice anything
        suspicious. 
      ''')
  elif choice == 3:
      characteristic = '@'
      if characteristic not in state['interaction_list']:
        print('''\n
          You decide to ask Mr Attingburg Senior for any possible suspects.
          He thinks long and hard about it for a while. 
          After a few moments, he suggests that Mr Dollar might've done it.
          When asked more about it, He says that Xavier and Mr Dollar recently
          had an argument about one of their business dealings gone wrong.
          Mr Dollar lost alot of good money and was severly butthurt about it.

        ''')
        state['interaction_list'].append(characteristic)
        state['clue_score'] += 1
        print(f'\nYou now have {state["clue_score"]} clues')

      else:
        print('''\n
        You have already investigated him 
        and found a clue. No need to investigate here again.
        ''')
        print(f'You now have {state["clue_score"]} clues')

  elif choice == 0:
      run = False
    
  elif state['clue_score'] == 6 and choice == 4:

    print('''
      You have now arrested Attinburg Senior 
      for murder!!! He now goes to prison!
      Unfortunatly YOU ARRESTED THE WRONG PERSON
      YOU LOOOOOOSEEEEEEEEE!!  
    ''')
    sys.exit()
    
  else:
    print('\n--Invalid interaction option--\n')


#this interaction function is for the left desk in room 2 
def left_desk(state, choice, run):
  if choice == 1:
    print('''\n
      you check the left desk table for any clues. 
      However, all you find is some lint, pins 
      and a strange toothbrush..... 
      You are unsure as to why there is a toothbrush
      in this desk. 
      However, you know for a fact that this isn't 
      related to the murder
    ''')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#this interaction function is for the right desk in room 2 
def right_desk(state, choice, run):
  if choice == 1:
    item = 'door_key'
    if 'door_key' not in state['item_list']:
      print('''\n
        You check the right desk table for clues.
        Though you dont find anything specifically 
        you do find the key for the kitchen. 
        you take and keep the key for yourself for future use. 
      ''')
      state['item_list'].append(item)
      print('\n You have now found the kitchen key')
      print(state['item_list'])
    else:
      print('''\n
      You have already investigated the desk.
      No need to investigate here again.
      ''')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#this interaction function is for the corridor desk in room 3 (corridor)
def corridor_desk(state, choice, run):
  if choice == 1:
    print('''\n
      You decide to check the corridor desk for clues.
      unfortunately, you dont find anything. This is a huge bummer.
      The investigation CONTINUES!
    ''')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#this interaction function is for the kitchen door in room 3 (corridor)
#This function is used to check if the player has a key and allows the player
#to enter the next room
def kitchen_door(state, choice, run):
  if choice == 1:
    if 'door_key' in state['item_list']:
      print('''\n
        you have now unlocked the door.
        you can now go through to the 
        kitchen.
    ''')
      state['door_unlocked'] = state['door_unlocked'] + 1

    else:
      print('''\n
          you cant open the door because 
          it is locked...
          Maybe you need to find the key
          to open this kitchen door.
      ''')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#This interaction is for the stove in room 4
def Stove_inter(state, choice, run):

  if choice == 1:
    print('''\n
      You decide to check the stove for clues.
      There wasn't anything cooking but the stove
      does smell like hot, tasty steaks.
      After the investigation, maybe you can have some 
      nice and juicy steaks as a reward for yourself ! 
    ''')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#This interaction is for the fridge in room 4. This has a similar feature where the user can pick up an item and use that item to open up other dialogue.
def fridge_inter(state, choice, run):
  if choice == 1:
    item = 'Lemonade'
    if 'Lemonade' not in state['item_list']:
      print('''\n
        You check the fridge for clues.
        you don't find anything particularly 
        interesting in the fridge. In fact,
        you get to see some mouldy fruits and
        a glass of refreshing lemonade. 
        You take the lemonade for yourself 
        incase it may come in handy!
      ''')
      state['item_list'].append(item)
      print('\n You have now taken a glass of lemonade')
      print(state['item_list'])
    else:
      print('''\n
      You have already investigated the fridge.
      No need to investigate here again.
      ''')
  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#This interaction is for the dining table in room 5.
def dining_table_int(state, choice, run):
  if choice == 1:
    characteristic = '====='
    if characteristic not in state['interaction_list']:
      print('''\n
        You search the dining table for clues.
        The dining table is quite large, especially for 
        serving only 3 people. You notice there are 
        name tags for each of the guests and host on the table.
        You notice that there is a knife missing in Mr Dollar's 
        side of the table. 

      ''')
      state['interaction_list'].append(characteristic)
      state['clue_score'] += 1
      print(f'\nYou now have {state["clue_score"]} clues')

    else:
      print('''\n
        You have already investigated the dining table
        for clues. No need to return here
      ''')
      print(f'You now have {state["clue_score"]} clues')

  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#This interaction is for the passed out lady (&) in room 5.
def Passed_out_woman_int(state, choice, run):
  if choice == 1:
    if 'Lemonade' in state['item_list']:
      print('''\n
        You give the woman a lemonade. She feels much better
        and more refreshed. She is now wide awake!
    ''')
      state['lady_awake'] = state['lady_awake'] + 1

    elif state['lady_awake'] == 1:
        print('''
          The lady is now awake and refreshed. 
          She looked like she passed out from absolute 
          shock.....
        ''')

    else:
      print('''\n
          The woman has passed out. Her mouth is open.
          Maybe you could give her something to bring her back
          to conciousness.....
      ''')

  elif choice == 2 and state['lady_awake'] == 1 and 'Lemonade' in state['item_list']:
    characteristic ='&'
    if characteristic not in state['interaction_list']:
      print('''\n
        The lady has now fully woken up!! It turns out that 
        she is the maid that was serving dinner to everyone. 
        When asked what happened, she said that she saw someone 
        take a knife and tried to stab Xavier but she doesnt remember 
        who as she passed out from shock. All she knows is that 
        it was someone who was wearing a navy 
        blue jacket....
      ''')
      state['interaction_list'].append(characteristic)
      state['clue_score'] += 1
      print(f'\nYou now have {state["clue_score"]} clues')

    else:
      print('''\n
        You have already investigated the housemaid
        for clues. No need to return here
      ''')
      print(f'You now have {state["clue_score"]} clues')

  if state['clue_score'] == 6 and choice == 3:

    print('''
      You have now arrested the housemaid/ 
      for murder!!! She now goes to prison!
      Even though she was passed out at the time...
      Unfortunatly YOU ARRESTED THE WRONG PERSON
      Thinking about it now.... I highly doubt
      that the maid that PASSED OUT would even
      commit murder.....
      Well anyways.....
      YOU LOOOOOOSEEEEEEEEE!!  
    ''')
    sys.exit()


  elif choice == 0:
    run = False

  else:
    print('\n--Invalid interaction option--\n')

#The function here is used to display the instructions for the game as well as an aim for the player.
def instructions():
  run = True
  while run:
    print('''
      AIM: 

      The aim of the game is to collect 
      as many clues as you can and arrest        
      the murderer of Xavier.

      You play as a detective (!) and you need
      to investigate the entire Xavier household for clues
      in order to solve the murder mystery.

      INSTRUCTIONS:

      Explore the house to find clues. You can find clues
      as either items or in a conversation so try to explore.
      Using the menu, input the right options.

      When you collect all the clues, make sure you know who
      the killer is. If you arrest the wrong person, 
      you lose.

      BEST OF LUCK PLAYER



    ''')
    Game_start = input('--press 0 to start--: ')

    if Game_start.isnumeric() == False:
      print('\ninput the number ZERO please!\n')

    else: 
      Game_start = int(Game_start)

      if Game_start == 0:
        game_state()
  
      else:
        print('NOT THE CORRECT INPUT! TRY AGAIN!!!')

#this here displays the title screen of the game. 
def main():
# I used this link below to help generate this title:
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
  print('''


     ███▄ ▄███▓ █    ██  ██▀███  ▓█████▄ ▓█████  ██▀███      ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓ ▐██▌  ▐██▌ 
    ▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒   ▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒ ▐██▌  ▐██▌ 
    ▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒░██   █▌▒███   ▓██ ░▄█ ▒   ▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░ ▐██▌  ▐██▌ 
    ▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄     ▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░ ▓██▒  ▓██▒ 
    ▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒░▒████▓ ░▒████▒░██▓ ▒██▒   ▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░ ▒▄▄   ▒▄▄  
    ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒  ░▀▀▒  ░▀▀▒ 
    ░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   ░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░  ░  ░  ░  ░ 
    ░      ░    ░░░ ░ ░   ░░   ░  ░ ░  ░    ░     ░░   ░    ░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░      ░     ░ 
           ░      ░        ░        ░       ░  ░   ░               ░    ░ ░           ░              ░  ░   ░     ░ ░      ░     ░    
                                  ░                                     ░ ░                                       ░ ░                 


    ''')

  run = True
  while run:

    continue_to_instructions = input('--Press 0 to start--: ')
    
    if continue_to_instructions.isnumeric() == False:
      print('\ninput the number ZERO! not a letter from the alphabet....\n')
    else:
      continue_to_instructions = int(continue_to_instructions)
      
      if continue_to_instructions == 0:
        instructions()

      else:
        print('oof try again buddy')

main()
