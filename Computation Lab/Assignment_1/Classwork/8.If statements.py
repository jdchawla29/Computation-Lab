var = [100, 150, 200, 250]
for i in range(len(var)): # for loop
    print (var[i])
    if var[i] == 200:
        print ("No")
    elif var[i] == 150:
        print ("Sorry")
    elif var[i] == 100:
        print ("Got it")
    else:
        print ("You are not there")