#620040546
#COMP2190

import random
import math

#main function to encrypt & decrypt the message
def main():
    p, q = 22, 22 #initalize variables with temporary values

    #check if the user enter vaild prime numbers
    while(isPrime(int(p)) == False or isPrime(int(q)) == False):
        p = raw_input("Enter a number (prime): ")
        q = raw_input("Enter other number (prime): ")

        #ask the user to re-enter numbers if it is not prime
        if(isPrime(int(p)) == False or isPrime(int(q)) == False):
            print "\nError, one of the number is not a prime or too small!!!\n"
    
    m = raw_input("Enter data: ") #accept the message to be encrypted by the user

    return encryption(m, int(p), int(q))

#check if the user entered prime numbers greater than or equal to 11
def isPrime(n):
    if(n<=10):
        return False
    else:
        for count in range(11,n):
            if (n%count == 0):
                return False                                   
        return True

#function to encrypt the message entered by the user
def encryption(ctext, p, q):
    tex = [] #break-up each character of the message into a list
    m = [] #convert the charcter from ASCII to decimal
    c = [] #store the encrypted message

    keys = pub_private(p,q)
    n = keys[2]
    phi = keys[3]
    e = keys[4]

    #store the message in a list
    for i in range(0, len(ctext)):
        tex = tex + ([ctext[i]])

    #convert the message from ASCII to its decimal equivalent
    for j in range(0, len(tex)):
        m.append(ord(tex[j]))

    #encrypt the message in the list
    for k in range(0, len(m)):
        new_a = m[k]**e #apply key to the message
        c.append(int(new_a%n))

    print "Encrypted message: " + str(c) 

    #call decrpytion function
    return decryption(c, n, phi, e)

def decryption(c, n, phi, e):
    m = [] #store the decrypted message
    new_m = "" #store the ASCII message
    d = Extended_Euclid(e,phi) #calculate d

    #decrypt the message to it decimal format
    for i in range(0,len(c)):
        m.append(int((c[i]**d)%n))

    #convert the decimal to ASCII characters
    for i in range(0,len(m)):
        new_m = new_m + (chr(m[i]))

    print "Decrpyted message: " + new_m

#function to determine p, q, n, phi, e of the RSA
def pub_private(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    e = n - 1 #Temporary e

    boolean = True
    while(boolean): #Randomly generate e
        e = random.randint(2, n-1)

        if(gcd(e,phi)==1 and e < n):
            boolean = False

    return p,q,n,phi,e


#function to find the extended gcd (from COMP2190)
def Extended_Euclid(m,n):
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, n
    while B3 != 0:
        Q = A3/B3

        T1, T2, T3 = A1- Q * B1, A2 - Q * B2, A3 - Q * B3
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

        d = A1%n

    return d

#function to find the greatest common divisor (from COMP1126)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a



    
