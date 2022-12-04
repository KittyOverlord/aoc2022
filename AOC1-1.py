#part 1

input = open("AOC1-1Input.txt"); lines = input.readlines()
print(max([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')]))

#part 2
input = open("AOC1-1Input.txt"); lines = input.readlines()
print([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].pop([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].index(max([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')])))+[sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].pop([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].index(max([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')])))+[sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].pop([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')].index(max([sum([int(j) for j in k.split('-')]) for k in ("-".join([i.replace('\n', '') for i in lines])).split('--')]))))


