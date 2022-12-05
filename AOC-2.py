print(sum([(1 if ([int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][0] <= [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][2] and [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][1] >= [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][3]) or ([int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][0] >= [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][2] and [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][1] <= [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][3]) else 0) for i in open("AOC-2Input.txt").readlines()]), sum([1 if sum([1 if j in range([int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][0], [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][1] + 1, 1) else 0 for j in range([int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][2], [int(k) for k in i.replace('\n', '').replace(',', '-').split('-')][3] + 1, 1)]) >= 1 else 0 for i in open("AOC-2Input.txt").readlines()])
)




