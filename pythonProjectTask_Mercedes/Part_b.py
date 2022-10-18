ar_count = []
m = 1
n =10
new_dict = dict()
final = []

for x in range(m, n+1):
    g = x
    count = 0

    if x == 1:
        count = 3


    while (x > 1):

        # if x in final:
        if any(x in d for d in final):
            # print("Present, ", end=" ")
            # print("value =", dic[key])
            count = count + [final[x] for d in final]
            #print("got in loop")
            break


        if x % 2 == 0:
            x = x / 2
            count = count + 1

        else:
            x = x * 3 + 1
            count = count + 1

    ar_count.append(count)
    new_dict = {g: count}
    final.append(new_dict)
    #print(count)

print(ar_count)
print(final)
