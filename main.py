import time

t = int(input("Enter the time in seconds: "))

def sayac (t):
    while t:
        dk, sn = divmod (t, 60)
        timer = '{:02d}:{:02d}'.format(dk, sn)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("UYAN!")

sayac(t)