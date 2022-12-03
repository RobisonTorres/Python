print('From Code Wars.')
print()

def race(v1, v2, g):
    
    # Given two speeds v1 (A) and v2 (B) and a lead g,
    # how long will it take to B catch A? 
    time = (g / (v2 - v1)) + 0.000001
    t_time = [int(time), (time - int(time)) * 60]
    t_time.append((t_time[1] - int(t_time[1])) * 60)
    return None if v1 >= v2 else list(map(int, t_time))

print(race(80, 91, 37))  # Outputs - 3h21min49s to A catch B.
