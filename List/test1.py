#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    # List comprehension to generate coordinates
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    # Filter out coordinates where the sum is not equal to n
    filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

    # Print the result
    print(filtered_coordinates)
