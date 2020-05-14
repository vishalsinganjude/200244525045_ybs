# Q5. Given a two list. Create a third list by picking an odd-index element from the first list and even index
# elements from second.

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
odd_lst = [ listOne[i] for i in range(len(listOne)) if i % 2 == 1]
even_lst = [ listTwo[i] for i in range(len(listTwo)) if i % 2 == 0]
print("Element at odd-index positions from list one :\n", odd_lst)
print("Element at even-index positions from list two :\n", even_lst)
print("Printing Final third list :\n", odd_lst + even_lst)
