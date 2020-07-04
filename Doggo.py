import dog
import time
import os
import win10toast

toaster = win10toast.ToastNotifier()

while True:
    dog.getDog(directory='/users/lenovo/Desktop', filename='dog')
    print("Woof! Woof!")
    toaster.show_toast('Python', "There's a new doggo pic!", duration = 15)
    time.sleep(2700)
    os.remove("dog.jpg")
