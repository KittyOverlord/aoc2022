def do_thing(info): 
    max_cal = 0
    current_cal = 0
    for i in range(len(info)):
        if i != "":
            current_cal += int(info[i])
        elif current_cal > max_cal:
            max_cal = current_cal
            ind = i
            current_cal = 0
        else:
            current_cal = 0
    return [ind, max_cal]

input = open("AOC1-1Inputs.txt")
list_input = input.getlines()
print(do_thing(list_input))

