weight= int(input("Weight : "))
sign= input("(l)bs or (k)g")
if sign=='k':
    k=weight*2.204
    print(f'You are {k} pounds')
elif sign=='l':
    l=weight*0.45359
    print(f'You are {l} kg')