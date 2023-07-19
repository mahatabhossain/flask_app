test_list = [1, 4, 6, 7, 5, 9]

def print_even(test_list):
    for i in test_list:
        if(i % 2 == 0):
            yield i

print("Original list", test_list)
print("Even number list", end= " ")
for j in  print_even(test_list):
    print(j , end=" " )
print()