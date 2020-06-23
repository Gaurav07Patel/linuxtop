
def add(n1,n2,n3,n4):
   return n1+n2+n3+n4
  

def sub(n1,n2,n3,n4):
    return n1-n2-n3-n4 
   

def mult(n1,n2,n3,n4):
    return n1*n2*n3*n4 
   
         
def div(n1,n2,n3,n4):
    return n1/n2/n3/n4  


print('please select your function: \n'
      '1. Addition \n'
      '2. Subtraction \n'
      '3. Multiplication \n'
      '4.Division \n' ) 

choiceOfFunction = int(input('Enter your choice(1-4): '))
listofchoice=[1,2,3,4]
if choiceOfFunction in listofchoice:
          n1 = int(input('Enter 1st num: ') or 8)
          n2 = int(input('Enter 2nd num: ') or 4)      
          n3 = int(input('Enter 3rd num: ') or 2)
          n4 = int(input('Enter 4th num: ') or 1)
     
if choiceOfFunction==1:
     addi=add(n1,n2,n3,n4)     
     print('The addition of the n1+n2+n3+n4 is: ' + str(addi))  
elif choiceOfFunction==2:
     diff=sub(n1,n2,n3,n4)     
     print('The subtraction of the n1-n2-n3-n4 is: ' + str(diff))  
elif choiceOfFunction==3:
     multi=mult(n1,n2,n3,n4)     
     print('The multiplication of the n1*n2*n3*n4 is: ' + str(multi))  
elif choiceOfFunction==4:
     divi=div(n1,n2,n3,n4)     
     print('The division of the n1/n2/n3/n4 is: ' + str(divi))            
else:    
    print('invalid entry!please enter choice between 1 to 4 only!')
    
