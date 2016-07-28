# Based on the children's game Hot Potato, using a Queue...
# Toss the potato 1-10 times and whoever is holding the potato is eliminated
# The last remaining person is the winner.

from queue import Queue
import random

def hotPotato(namelist):
    # Instantiate a queue and insert everyone's names into it
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    # Store 'elimination statements' into a dict
    elim_dict = {0: "'s hands burnt off! Now they have no hands, only stumps.", 
                 1: " drops the potato, for no good reason.", 
                 2: " gets sick from the smell of burning human flesh.",
                 3: " is hit in the face with the scalding potato, and screams in agony.",
                 4: " has had enough of this sick game."}

    # While queue is larger than 1
    while simqueue.size() > 1:
        # Determine how many times to toss the potato
        tosses = random.randint(1,10)
        if tosses == 1:
            print("Tossing " + str(tosses) + " time...")
        else:
            print("Tossing " + str(tosses) + " times...")

        # Move a person from the beg of the queue to the end of the queue, to simulate a toss
        for i in range(tosses):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue) # Comment out for cleaner output

        # After the tosses, person holding potato is eliminated
        # Randomly select an elimination statement from the elim_dict
        elim_code = random.randint(0,4)
        print(str(simqueue.peek()) + elim_dict[elim_code])

        simqueue.dequeue()

    # Return the 1 person leftover
    return (str(simqueue.dequeue()) + " is the winner! He gets to keep the potato.")

print(hotPotato(["Bill","David","Susan","Jane","Kent","Adam", "Robert"]))
