import threading

lock = threading.Lock()

resource = 0

def increment_resource():
    global resource
    with lock:
        resource += 1  # Atomic operation

threads = []
for _ in range(100):
    thread = threading.Thread(target=increment_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Expected: 100, Actual: {resource}")