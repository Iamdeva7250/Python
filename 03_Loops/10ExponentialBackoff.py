# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1  # Initial wait time in seconds
max_retries = 5 
attemps = 0

while attemps < max_retries:
    print(f"Attempt {attemps + 1}: Waiting for {wait_time} seconds...")
    time.sleep(wait_time) 
    attemps += 1
    wait_time *= 2  
print("Max retries reached. Exiting.")


