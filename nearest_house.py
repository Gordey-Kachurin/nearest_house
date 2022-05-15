house_numbers = input('List numbers separated by space: ')
house_numbers = house_numbers.split(' ' )

# convert to int
for i in range(0, len(house_numbers)):
    house_numbers[i] = int(house_numbers[i])

# hn - short for house_numbers function
def hn(house_numbers):
    distance = 0
    distance_list = []
    for index, item in enumerate(house_numbers):
        if item == 0:
            distance_list.append(item)
            continue # skip the rest of the code and continue to the next interation
        for i in  range(index, len(house_numbers)) :

            if house_numbers[i] != 0:
                distance = distance + 1
                
            else:
                distance_list.append(distance)
                distance = 0
                break # exit inner for loop to continue outer loop
    return distance_list

distance_list = hn(house_numbers)
distance_list_reverced = hn(house_numbers[::-1])

if len(distance_list) < len(house_numbers):
    diff = len(house_numbers) - len(distance_list) 
    for i in range(diff):
        distance_list.append('')

if len(distance_list_reverced) < len(house_numbers):
    diff = len(house_numbers) - len(distance_list_reverced) 
    for i in range(diff):
        distance_list_reverced.append('') 
         

distance_list_reverced = distance_list_reverced[::-1]    

distance_list_combined = []
for i, item in enumerate(distance_list):
     
    if distance_list[i]  == '':
        distance_list_combined.append(distance_list_reverced[i])
        continue
    if distance_list_reverced[i]  == '':
        distance_list_combined.append(distance_list[i])
        continue

    if distance_list[i] == distance_list_reverced[i]:
        distance_list_combined.append(distance_list[i])
    if distance_list[i] < distance_list_reverced[i]:  
        print(distance_list[i], distance_list_reverced[i])
        distance_list_combined.append(distance_list[i])
    if distance_list[i] > distance_list_reverced[i]:     
        distance_list_combined.append(distance_list_reverced[i])

# Test samples
# 1 0 3 4 5 6 7 8 9 0 1 0 3 0 5 6 7 8 9 10
# 1 0 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 0 9 10
# 0 2 3 4 5 6 0 8 9 0
# 0 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 0
print('house_numbers  : ', house_numbers)
print('distance_list  : ',distance_list)
print('distance_list_r: ',distance_list_reverced)
print('distance_list_c: ',distance_list_combined)