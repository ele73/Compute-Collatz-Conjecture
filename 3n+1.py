def show_collatz(n):
    res = int(n)
    print("Step 0: " + str(int(res)))
    for i in range(1, 10000):
        if res % 2 == 0:
            res /= 2
            print("Step " + str(i) + ": " + str(int(res)))
        elif res == 1:
            print("n = " + str(n))
            return True
            n_steps = i+1
            return n_steps
            break
        else:
            res = (3*res+1)
            print("Step " + str(i) + ": " + str(int(res)))

def collatz_true(n):
    global c1
    c1 = False
    for e in range(n):
        res = e+1
        for i in range(100000):
            if res % 2 == 0:
                res /= 2
            elif res == 1:
                c1 = True
                n_steps = i
                break
            else:
                res = (3*res+1)
        if c1 == True:
            print(str(e+1) + ": " + str(n_steps) + " steps.") 

def collatz_true1(n):
    global c1
    c1 = False
    for e in range(n, n+10000):
        res = e+1
        for i in range(100000):
            if res % 2 == 0:
                res /= 2
            elif res == 1:
                c1 = True
                n_steps = i
                break
            else:
                res = (3*res+1)
        if c1 == True:
            print(str(e+1) + ": " + str(n_steps) + " steps.")            
