import numpy

#Intervalos de cálculo
x_min=1
x_max=20
y_min=1
y_max=20
z_min=1
z_max=20
w_min=1
w_max=20
passo=1

result=[]

def quatro_variaveis():
    for x in numpy.arange(x_min,x_max,passo):
        for y in numpy.arange(y_min,y_max,passo):
            for z in numpy.arange(z_min,z_max,passo):
                for w in numpy.arange(w_min,w_max,passo):
                    expr=2*x-y-z+21*w
                    if expr==0:
                        result.append((x,y,z,w))

def tres_variaveis():
    for x in numpy.arange(x_min,x_max,passo):
        for y in numpy.arange(y_min,y_max,passo):
            for z in numpy.arange(z_min,z_max,passo):
                expr=2*x-y-z
                if expr==0:
                    result.append((x,y,z))

def duas_variaveis():
    for x in numpy.arange(x_min,x_max,passo):
        for y in numpy.arange(y_min,y_max,passo):
            expr=2*x-y
            if expr==0:
                result.append((x,y))
    
    

escolha=str(input("How many variables in Diophantine Equation: "))

if escolha=='2':
    duas_variaveis()
    print('Solutions: ')
    print(result)
    
elif escolha=='3':
    tres_variaveis()
    print('Solutions: ')
    print(result)
    
elif escolha=='4':
    quatro_variaveis()
    print('Solutions: ')
    print(result)