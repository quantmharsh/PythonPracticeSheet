# Reading input values
m1 = int(input("initial level of water in jug (in ml)"))
m2 = int(input("level of water in jug required for drinking (in ml)"))
x = int(input("height which small pebble will increase (in ml)"))
y = int(input("height which big pebble will increase (in ml)"))
n = int(input("number of small pebbles"))

# Number of small pebbles required to increase water level to m2
small_pebbles = ((m2-m1)//x)

# If the small pebbles cannot increase water level to m2, return -1
if small_pebbles < n:
    print("-1")
else:
    # Remaining height to be increased after using small pebbles54
    remaining_height = m2 - m1 - (n*x)
    
    # Number of big pebbles required to increase remaining height
    big_pebbles = remaining_height // y
    
    # If big pebbles cannot increase remaining height, add one more big pebble
    if remaining_height % y != 0:
        big_pebbles += 1
    
    print(big_pebbles)
