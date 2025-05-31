import threading

# Define a function to run in a thread
def coder(number):
    print(f'Coder ID: {number}')

# Create and start 5 threads
threads = []
for k in range(5):
    t = threading.Thread(target=coder, args=(k,))
    threads.append(t)
    t.start()
