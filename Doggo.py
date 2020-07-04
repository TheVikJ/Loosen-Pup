import dog
import time
import os

while True:
    dog.getDog(directory='/users/<USER>/lenovo/Desktop', filename='dog')
    print("How about a break? Here's a new doggo pic! V◕ฺω◕ฺV")
    time.sleep(2700)
    os.remove("/users/<USER>/Desktop/dog.jpg")
