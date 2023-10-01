import time

word = "HELLO WORLD!"

def animate(text):
    for i in range(len(text)):
        partial_text = text[:i+1]
        print(partial_text, end='\r')
        time.sleep(0.2)
    time.sleep(0.85)

def clear(text):
    print(' ' * len(text), end='\r')
    time.sleep(0.1)
    animate(text)

try:
    while True:
        animate(word)
        clear(word)
except KeyboardInterrupt:
    pass
