from operator import itemgetter
queue = []
queue = eval(input())
#print(queue)
queue.sort(key=itemgetter(1))
#print(queue)
queue.sort(key=itemgetter(0), reverse=True)
#print(queue)

output = []
for item in queue:
    output.insert(item[1], item)
print(output)
