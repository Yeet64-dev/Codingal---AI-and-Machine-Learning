n = int(input("Running lap Tracker. How many steps did you take?"))

input("Formula: one calculation, done.  Press Enter to run ")
Running_Points = 1
print("  points =", Running_Points, "  ->  O(1)  constant time  ->  steps never change")

input("Loop: one step per item.  Press Enter to run ")
Running_Points = 0
for i in range(n):
    Running_Points += 1
print("  points =", Running_Points, "  ->  O(n)  linear time  ->  steps grow with n")

input("Double Loop: checks every pair.  Press Enter to run ")
Running_Points = 0
for i in range(n):
    for j in range(n):
        Running_Points += 1
print("  points =", Running_Points, "  ->  O(n^2)  quadratic time")
