#fix the Pyhton bug code
def lone_sum(a, b, c):
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return total
print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(20, 20, 20)))
print("lone_sum of 1, 2, 3 should be 6: " + str(lone_sum(1, 2, 3)))
print("lone_sum of 1, 2, 1 should be 2: " + str(lone_sum(1, 2, 1)))
print("lone_sum of 4, 5, 6 should be 15: " + str(lone_sum(4, 5, 6)))