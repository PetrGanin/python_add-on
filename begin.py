import time


timer_begin = time.time()
for i in range(0, 16, 1):
    print(i)

timer_end = time.time()
timer_secs = timer_end - timer_begin
times_msecs = timer_secs * 1000
print(times_msecs)
