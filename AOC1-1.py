def do_thing(info):
    elf_cal = [0]
    i = 0
    for cal in info:
        if cal == "":
            i += 1
            elf_cal.append(0)
        else:
            elf_cal[i] += int(cal)

    min_cal = 0
    ind = 0
    for i in range(len(elf_cal)):
        if elf_cal[i] > min_cal:
            min_cal = elf_cal[i]
            ind = i

    return i
