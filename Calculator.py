# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:42:59 2019

@author: jiang
"""

def Addition(A, B):
    Result = A + B
    return Result


def Subtraction(A, B):
    Result = A - B
    return Result


def Multiplication(A, B):
    Result = A * B
    return Result 

def Division(A, B):
    Result = A / B
    return Result


def StandardlizeFormula(Formula):
    NewFormula = ''
    for element in range(len(Formula)):
        if Formula[element] == '+' or Formula[element] == '*' or Formula[element] == '/':
            NewFormula += ' ' + Formula[element] + ' '
        elif Formula[element] == '-':
            if element == 0 or Formula[element-1] == '+' or Formula[element-1] == '*' or Formula[element-1] == '/':
                NewFormula += '-'
            else:
                NewFormula += ' - '
        elif Formula[element] == '(':
            NewFormula += '( '
        elif Formula[element] == ')':
            NewFormula += ' )'
        else:
            NewFormula += Formula[element]
    return NewFormula.split()


def Process(NewFormula):
    while '(' in NewFormula:
        Paren1 = 0
        Paren2 = 0
        FirstParen = NewFormula.index('(')
        for i in range(len(NewFormula)):
            if NewFormula[i] == '(':
                Paren1 += 1
            elif NewFormula[i] == ')':
                Paren2 += 1
            if Paren1 == Paren2 and Paren1 != 0:
                SecondParen = i
                break
        TempList = NewFormula[FirstParen + 1:SecondParen]
        NewFormula = NewFormula[:FirstParen] + NewFormula[SecondParen:]
        NewFormula[FirstParen] = Process(TempList)
    return Calculate(NewFormula)
    

def Calculate(List):
    while '*' in List or '/' in List:
        for i in List:
            if i == '*':
                Position = List.index(i)
                TempCal = Multiplication(float(List[Position - 1]), float(List[Position + 1]))
                del(List[Position])
                del(List[Position])
                List[Position - 1] = str(TempCal)
                break
            if i == '/':
                Position = List.index(i)
                TempCal = Division(float(List[Position - 1]), float(List[Position + 1]))
                del(List[Position])
                del(List[Position])
                List[Position - 1] = str(TempCal)
                break
    for i in range(int((len(List) - 1)/2)):
        if List[1] == '+':
            TempCal = Addition(float(List[0]), float(List[2]))
        else:
            TempCal = Subtraction(float(List[0]), float(List[2]))
        del(List[1])
        del(List[1])
        List[0] = str(TempCal)
    return List[0]

def Main():
    Rubbish = '!@#$%^&_=|\}{] [:;?><.,`~qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    while True:
        while True:
            Found = False
            Formula = input('Enter your formula here: ')
            if Formula == '':
                return None
            for i in Rubbish:
                if i in Formula:
                    Found = True
                    print('Unexpected operand')
                    break
                if not Found:
                    break
            NewFormula = StandardlizeFormula(Formula)
            Result = Process(NewFormula)
            print('The Result is: ', Result)


Main()

    
    
    
    
    
    
    
    
    
    
    
    
    