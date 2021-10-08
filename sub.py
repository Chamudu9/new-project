Tem=input('Enter a Temperature:')
scale=raw_input('Enter the Scale(F,C):')
if scale=='C':
    Answ=float(Tem*9.00/5.00+32.00)
    print'Temperature in Fahrenheit :',Answ,'F'
else:
    Answ=float(Tem-32.00)*5.00/9.00
    print'Temperature in Celsius :',Answ,'C'
