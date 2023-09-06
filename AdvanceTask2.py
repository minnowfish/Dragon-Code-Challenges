medalists = ["Usain Bolt", "Michael Phelps", "Simone Biles", "Nadia Comăneci", "Carl Lewis"]
i = 0
swapped = True
swaps = 0
length = len(medalists)
while swapped == True:
  while i < length - 1:
    if medalists[i] > medalists[i+1]:
      temp = medalists[i]
      medalists[i] = medalists[i+1]
      medalists[i+1] = temp
      swaps = swaps + 1
    i = i+ 1
    if swaps == 0:
      swapped = False
    else:
      swaps = 0
      i = 0
        
print(medalists)
