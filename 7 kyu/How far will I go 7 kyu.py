# How far will I go?
# You have recently discovered that horses travel in a unique pattern - they're either running (at top speed) or resting (standing still).

# Here's an example of how one particular horse might travel:

# The horse Blaze can run at 14 metres/second for 60 seconds, but must then rest for 45 seconds.
# After 500 seconds Blaze will have traveled 4200 metres.
# Your job is to write a function that returns how far a horse will have traveled after a given time.

# Input:
# totalTime - How long the horse will be traveling (in seconds)

# runTime - How long the horse can run for before having to rest (in seconds)

# restTime - How long the horse have to rest for after running (in seconds)

# speed - The max speed of the horse (in metres/second)

def travel(total_time, run_time, rest_time, speed):
    cycle, remaining_time = divmod(total_time, (run_time + rest_time))
    time_while_running = run_time * cycle + min(remaining_time, run_time)
    distance = speed * time_while_running
    return distance
