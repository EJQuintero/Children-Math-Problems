
def getBlue(var1,var2):
    b = var1 - var2
    return b

def getRed(times,var1,var2):
    r = times * getBlue(var1,var2)
    return r

def getTotal(times,var1,var2):
    t = var1 + getBlue(var1, var2) + getRed(times,var1,var2)
    return t

def main():
    from random import randint
    g = randint(18,68)
    times = randint(6,15)
    fewer = randint(15,24)
    while g < fewer:
        fewer = randint(12,20)
    right = "Good job! That is the right number of marvels."
    print("Jake has",g,"green marvels. He has",times,"times more red marvels than blue marvels.\n"\
        "He has",fewer,"fewer blue marvels than green marvels.")
    
    userg = eval(input('\nHow many green marvels does Jake have?\t'))
    if userg == g:
        print(right)
    else:
        while userg != g:
            userg = eval(input('\nSorry. That is not the right answer, please try again. How many green marvels does Jake have?'))
            if userg == g:
                print(right)

    userb = eval(input('\nHow many blue marvels does Jake have?\t'))
    if userg == g:
        print(right)
    else:
        while userb != getBlue(g, fewer):
            userb = eval(input('\nYou entered the wrong amount of marvels. How many blue marvels does Jake have?\t'))
            if userb == getBlue(g, fewer):
                print(right)

    userr = eval(input('\nHow many red marvels does Jake have?\t'))
    if userr == getRed(times, g, fewer):
        print(right)
    else:
        while userr != getRed(times, g, fewer):
            userr = eval(input('\nYou entered the wrong amount of marvels. How many red marvels does Jake have?\t'))
            if userr == getRed(times, g, fewer):
                print(right)

    usertotal = eval(input('\nHow many marvels does Jake have in total?\t'))
    if usertotal == getTotal(times, g, fewer):
        print(right)
    else:
        while usertotal != getTotal(times,g,fewer):
            usertotal = eval(input('\nYou entered the wrong amount of marvels. How many marvels does Jake have in total?\t'))
            if usertotal == getTotal(times,g,fewer):
                print(right)

main()












