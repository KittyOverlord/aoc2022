def do_thing(info): 
    max_cal = 0
    current_cal = 0
    elf = 1
    for i in range(len(info)):
        if info[i] != "\n":
            current_cal += int(info[i])
        elif current_cal > max_cal:
            max_cal = current_cal
            ind = elf
            current_cal = 0
            elf += 1
        else:
            current_cal = 0
            elf += 1
    return [ind, max_cal]

input = open("AOC1-1Input.txt"); lines = input.readlines()
print(do_thing(lines))

