```python
import threading

lock = threading.Lock()

resource = 0

def increment_resource():
    global resource
    lock.acquire()
    try:
        # Simulate some work with the resource
        temp = resource
        temp += 1
        resource = temp  # Non-atomic operation
    finally:
        lock.release()

threads = []
for _ in range(100):
    thread = threading.Thread(target=increment_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Expected: 100, Actual: {resource}")
```