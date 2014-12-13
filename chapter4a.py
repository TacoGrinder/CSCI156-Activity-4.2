__author__ = 'Sean'

def byten(n):
    if n % 10 == 0:
        print(str(n) + " is divisible by ten.")
    else:
        print(str(n)+" is not divisible by ten.")
    if n == 10:
        print("Duh!")
    elif 10 % n == 0:
        print (str(n) + " is a factor of ten.")
    else:
        print (str(n) + " is not a factor of ten.")

byten(20)