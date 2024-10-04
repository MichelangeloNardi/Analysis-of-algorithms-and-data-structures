import sys

data = sys.stdin.read()

lines = data.splitlines()

line1 = lines[0].split()
#line1 = input().split()

line2 = list(map(int, lines[1].split()))
#line2 = list(map(int, input().split()))

n = int(line1[0])

k = int(line1[1])


minimum = max(line2)
maximum = sum(line2)


def check_if_feasible(masses, max_capicity, n_flights):
    count_flights = 1
    i = 0
    count_mass = 0
    while i < len(masses):

        count_mass += masses[i]

        if count_mass >max_capicity:
            count_flights += 1
            count_mass = masses[i]
        
        if count_flights > n_flights:
            return False
        
        i += 1
            
    return True


def binary_search(minimum, maximum, masses, n_flights):
    if maximum == minimum + 1:
        if check_if_feasible(masses, minimum, n_flights):
            return minimum
        else:
            return maximum
       
    middle = (minimum + maximum) // 2
    if check_if_feasible(masses, middle, n_flights):
        return binary_search(minimum, middle, masses, n_flights)
    else:
        return binary_search(middle, maximum, masses, n_flights)

result = binary_search(minimum, maximum, line2, k)
print(result)

