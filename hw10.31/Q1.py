# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:54:02 2019

@author: jiang
"""
while True:
    TicketType = input('TicketType: ')
    if TicketType == 'E' or TicketType == 'S':
        break


while True:
    try:
        BaggageWeight = float(input('Weight: '))
        if BaggageWeight >= 0:
            break
    except ValueError:
        continue

    

if TicketType == 'E':
    BaggageAllowance = 16
    ChargeRate = 3.5
else:
    BaggageAllowance = 20
    ChargeRate = 5.75


ExcessWeight = BaggageWeight - BaggageAllowance


if ExcessWeight > 0:
    Charge = ExcessWeight * ChargeRate
else:
    Charge = 0

    
print('Charge: ', Charge)
    

