## Race Condition with Non-Atomic Operation Despite Lock
This example demonstrates a race condition in Python, even with the use of a lock.  The issue lies in the non-atomic nature of the increment operation.

**Problem:**
Even though a `threading.Lock` is used, the `increment_resource` function contains a non-atomic operation. The line `resource = temp` is not atomic.  Multiple threads can read the same value of `resource`, increment it, and then write back the incremented value, resulting in lost updates.

**Solution:**
The solution utilizes the `+=` operator,  which in Python for simple data types like integers can be atomic, making the entire operation thread-safe.