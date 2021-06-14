# Mainting the window of size k and removing the starting element of window
window_sum = 0
max_sum = 0
start = 0

for end in range(len(arr)):
    window_sum += arr[end]
        
    if end >= k-1: #  Here, once the size is increased to the k, them will starting removing the starting window element and again adding the new element.
        max_sum  = max(max_sum, window_sum)
        window_sum -= arr[start]
        start += 1
        
print(max_sum)




# Second Way to doing with python slicing

max_sum= 0
for i in range(len(arr)-k):
    max_sum= max(sum(arr[i: i+(k)]), max_sum)
    
print(max_sum)
    
