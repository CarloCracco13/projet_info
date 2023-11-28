import random as rd 

questions = { "structure_donnee" : {"dict" : "{:,}" , "list" : "[,]" , "tuple" : "{}" }  , "structure_controle" : { "if":"if" , "while":"while" , "for":"for" , "def":"def" } }

general_input = ""
while general_input != "stop" : 
    general_input = input("choisissez un jeux parmis ... : " )
    if general_input == "Python" :
        usr_inp = "" 

        points = 0 
        correct = False
        while usr_inp != "stop" : 
            correct = False
            q_type = rd.sample(sorted(questions), 1 ) 
            q = rd.sample(sorted(questions[q_type[0]]), 1 ) 
            sol  = questions[q_type[0]][q[0]]

            usr_inp = input("nombre de points :" + str(points) + "\n"   + q[0] + " : "  ) 

            if usr_inp == sol : 
             correct = True
             points += 1 

            print(str(correct) + " la bonne sollution est : "+  sol)




