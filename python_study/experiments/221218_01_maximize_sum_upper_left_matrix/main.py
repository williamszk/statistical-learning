# https://www.geeksforgeeks.org/maximize-sum-n-x-n-upper-left-sub-matrix-given-2n-x-2n-matrix/

# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)


# mod(y-n+1)
# mod(x-n+1)
# (0, 1) 
# (0, 2) # mod(1-4+1)=2
# (3, 1) # mod(0-4+1)=3
# (3, 2)

# (0, 0)
# (0, 3) # mod(y-n+1)=mod(0-4+1)=3
# (3, 0) # mod(x-n+1)=mod(3-4+1)=0
# (3, 3)

# mod(y-n+1)=mod(0-4+1)=3
# mod(x-n+1)=mod(1-4+1)=2
# (1,0)
# (1,3) 
# (2,0)
# (2,3)

# (0,0) (0,1) (0,2) (0,3) (0,4) (0,5)
# (1,0) (1,1) (1,2) (1,3) (1,4) (1,5)
# (2,0) (2,1) (2,2) (2,3) (2,4) (2,5)
# (3,0) (3,1) (3,2) (3,3) (3,4) (3,5)
# (4,0) (4,1) (4,2) (4,3) (4,4) (4,5)
# (5,0) (5,1) (5,2) (5,3) (5,4) (5,5)

# mod(y-n+1)=mod(1-6+1)=4
# mod(x-n+1)=mod(1-6+1)=4
# (1,1)
# (1,4) 
# (4,1)
# (4,4)

def maxSum(mat):

    def find_max(coord, mat):
        n = len(mat)
        x = coord[0]
        y = coord[1]
        alt_x = abs(x - n + 1) 
        alt_y = abs(y - n + 1) 

        possible_coords = [
            (x, y),
            (alt_x, y),
            (x, alt_y),
            (alt_x, alt_y),
        ]

        return max([mat[coord[0]][coord[1]] for coord in possible_coords])


    from itertools import product
    n = len(mat)
    result = 0
    # n = 4 => the matrix is 4x4, and we'll take the 2x2 matrix at the 
    # upper-left corner
    n_corner = n // 2

    for coord in product(range(n_corner), range(n_corner)):
        result += find_max(coord, mat)

    return result


# Driver Code
if __name__ == "__main__":
    R = C = 4
    mat = [
        [112, 42, 83, 119], 
        [56, 125, 56, 49], 
        [15, 78, 101, 43], 
        [62, 98, 114, 108]
        ]

    assert maxSum(mat) == 414
