def draw_triangle ():
    print ("  *  ")
    print (" *** ")
    print ("*****")
    print()

def draw_square ():
    i = 0
    for i in range (5):
        print ("*****")
    print()

def draw_circle ():
    print (" ** ")
    print ("****")
    print ("****")
    print (" ** ")
    print()


counter = 0
while counter < 3:
    draw_triangle()
    draw_square()
    draw_circle()
    counter = counter + 1
