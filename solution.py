def solution(A):
    A.sort()

    rooms = 0
    i = 0 
    N = len(A)

    while i < N:
        current_room_size = 0
        max_capacity = A[i]
        
       
        rooms += 1
        
        while i < N and current_room_size < max_capacity:
            current_room_size += 1
            i += 1
            
    return rooms

print(solution([1,1,1,1,1]))
print(solution([2, 1, 4]))
print(solution([2, 7, 2, 9, 8]))
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))