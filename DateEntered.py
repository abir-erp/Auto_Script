import random
from datetime import datetime, timedelta

# Input timestamp data with nanoseconds precision
initial_timestamp = "2021-11-19 14:02:10.0000000"

# Function to add random minutes and randomize seconds to a timestamp
def add_random_time_and_seconds(timestamp_str):
    date_str, time_str = timestamp_str.split()
    h, m, s_ns = time_str.split(':')
    s, ns = s_ns.split('.')
    
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s) + random.randint(60, 120)  # Randomize minutes between 1 to 2
    new_ns = int(ns)  # Keep the same nanoseconds
    
    new_h = total_seconds // 3600
    total_seconds %= 3600
    new_m = total_seconds // 60
    new_s = random.randint(0, 59)   # Randomize the seconds
    
    new_time_str = f"{new_h:02}:{new_m:02}:{new_s:02}.{new_ns:07d}"[:23]  # Ensure seven digits in nanoseconds
    return f"{date_str} {new_time_str}"

timestamps = [initial_timestamp]
previous_timestamp = initial_timestamp

# Generate new timestamps based on the previous one
for _ in range(15):
    new_timestamp = add_random_time_and_seconds(previous_timestamp)
    timestamps.append(new_timestamp)
    previous_timestamp = new_timestamp

# Print the updated timestamps
for ts in timestamps:
    print(ts)
