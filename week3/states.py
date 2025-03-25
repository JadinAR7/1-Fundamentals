states = ['Washington', 'Oregon', 'Colorado','Kansas', 'New York', 'California', 'Texas']



print(states)

print('-----------------')

print(states[0], states[1])
print(states[1])
print(states[2])
print(states[3])
print(states[4]) 
print(states[5])
print(states[6])

print('-----------------')

print(states[-1])
print(states[-2])
print(states[-3])
print(states[-4])
print(states[-5])
print(states[-6])
print(states[-7])

print('-----------------')

for state in states:
    print(state)

print('-----------------')

while len(states) > 0:
    print(states.pop(0))
    
print('-----------------')



