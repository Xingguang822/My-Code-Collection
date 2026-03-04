for x in range(0,21):
    for y in range(0,34):
        for z in range(0,100,3):
            if(5*x+3*y+z//3==100)and(x+y+z==100):
                print(x,y,z)

for x in range(0,21):
    for y in range(0,34):
        z=100-x-y
        if(5*x+3*y+z//3==100)and(z%3==0):
            print(x,y,z)