import random
print('winnig rule of the game rock ,paper SCISSOR are :\n'+
      "Rock vs paper-> paoer win \n"+"Rock vs scissor-> rock win \n"+"paper vs scissor-> scissor wins \n")
while True:
    print('Enter your choice \n 1 -Rock 2-paper \n  3-scissor \n') 
    #take the input from user

    choice=int(input('Enter your choice:'))
    #loopin until that user enter invilid choice
    while choice>3 or choice<1:
        choice=int(input('Enter valid choise please:'))
    
    # initilize the choice value crresponding to to the choice_name
    
    if choice==1:
        choice_name='Rock'
        
    elif choice==2:
        choice_name='Scissor'
        
    elif choice==3:
        choice_name='Paper'
    print('user choice is \n', choice_name)
    
    print('now its  computer turns......')
    # computer choose any number b\w 1,2,3 usin randint()
    
    com_choice=random.randint(1, 3)
    # looping untill that com_choice equal to choice value
    while com_choice==choice:
        pass#com_choice=random.randint(1,3)
        # initilize value com_choice_name corres to choice value
    if com_choice==1:
        com_choice_name='rookR'
    if com_choice==2:
        com_choice_name='paper'
    if com_choice==3:
        com_choice_name='scissoR'
    
    print('computer choice is \n',com_choice_name)
    print(choice_name, 'vs', choice_name)
    
    #we need to cheak draw match
    if choice==com_choice:
        print('Its a draw',end='')
        result='draw'
        
    #condtiuon for winning
    if choice==1 and com_choice==2:
        print('paper wins ',end='')
        result='papeR'

    elif choice==2 and com_choice==1:
        print('paper wins *',end='')
        result='PapeR'
        
    elif choice==1 and com_choice==3:
        print('Rock wins** ',end='')
        result='Rock'
        
    elif choice==3 and com_choice==1:
        print('Rock wins ',end='')
        result='Rock'
    
    elif choice==2 and com_choice==3:
        print('Scissors wins*** ',end='')
        result='Scissors'
    
    elif choice==3 and com_choice==2:
        print('Scissors wins *** ',end='')
        result='Scissors'
        
    #if user or cmp wins or deaw
    if result=='DRAW':
        print('<== its a tie ==>' )
    if result==com_choice:
        print('<== user wins**** ==>')
    else:
        print('computer win ')
    
    print('Do you want to play again (y/n)')
    ans=input().lower
    if ans == 'n':
        break
print('Thank you for playing')


'''import random
while True:
    
    print('Enter your choice name: 1-Rock \n 2- cotton \n 3- potato')
    choice=int(input('Enter your choice'))
    # while choice <4 or choice>=1:
    #     choice=int(input('enter valid chopice'))
    
    if choice==1:
        choice_name='Rock'
        
    elif choice==2:
        choice_name='COTTON'
        
    elif choice==3:
        choice_name='POTATO'
            
    print('Now its computer turn')
    print('computer choice')
    
    com_choice_name=random.randint(1, 3)
    
    
    if com_choice==1:
        com_choice_name='rooCK'
        result='rooCK'
        
    elif com_choice==2:
        com_choice_name='cottoN'
        result='cottonR'
        
    elif com_choice==1:
        com_choice_name='potatO'
        result='potatO'
    
    print('computre chpice vs \n ',com_choice_name)
    print('user choice name \n',choice_name)
    if choice==com_choice:
        print('its draw ',end='')
        result='DRaw'
    
    if choice==1 and com_choice==2:
        print('<== USER wins','end='')  
        
    elif choice==2 and com_choice==1:
        print('<== COMPUTER wins','end='') 
        
    elif choice==2 and com_choice==3:
        print('<== COMPUTER wins,'end='') 

    elif choice==3 and com_choice==2:
        print('<== user wins','end='')
        
    elif choice==1 and com_choice==3:
        print('<== user wins','end='')  

    elif choice==3 and com_choice==1:
        print('<== COMPUTER wins')  '''
        
        
 
         
    
        
    
        
    
    