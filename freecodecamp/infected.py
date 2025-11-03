import math

def infected(days:int)-> int:
    infected_pcs = 1
    counter_days = 1
    days_to_patch = 2
    while counter_days <= days:

        infected_pcs = 2 * infected_pcs

        if days_to_patch == 0:
            infected_pcs = infected_pcs - math.ceil(infected_pcs * 0.2)
            days_to_patch = 3

        counter_days += 1

        days_to_patch -= 1

    return infected_pcs

infected(3)