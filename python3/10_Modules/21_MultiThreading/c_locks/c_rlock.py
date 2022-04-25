"""
Purpose: Traditional Lock vs Re-Entrant Lock
"""
import threading

trad_lock = threading.Lock()

print(f"Main thread name: {threading.main_thread().name}")
print(f"Is it locked: {trad_lock.locked()}")

print("\nFirst try   :", trad_lock.acquire())
print(f"Is it locked: {trad_lock.locked()}")

# trad_lock.acquire()  - it will wait infinite time
# NOTE: Problem is that even if mainthread has acquired lock,
# we cant gain access, unless released

trad_lock.release()  # If released, we can gain access

print("\nSecond try  :", trad_lock.acquire(0))
print(f"Is it locked: {trad_lock.locked()}")
print()

for i in range(3, 10):
    print(f"try {i}th time -{trad_lock.acquire(0)}", end=" => ")
    print(f"Is it locked: {trad_lock.locked()}")
# 'acquire_lock', 'locked_lock', 'release', 'release_lock'
print("============================================================")

# With RLock(re_entrant Lock), if the lock is acquired by same thread,
# we can acquire again, without explicitly releasing
r_lock = threading.RLock()

print(f"\n\nMain thread name: {threading.main_thread().name}")
print(f"Is it locked: {trad_lock.locked()}")

print("\nFirst try   :", r_lock.acquire())
print(f"Is it locked: {trad_lock.locked()}")

print("\nSecond try  :", r_lock.acquire(0))
print(f"Is it locked: {trad_lock.locked()}")
print()


for i in range(3, 10):
    print(f"try {i}th time -{r_lock.acquire(0)}", end=" => ")
    print(f"Is it locked: {trad_lock.locked()}")
# 'acquire_lock',  'locked_lock', 'release', 'release_lock'
