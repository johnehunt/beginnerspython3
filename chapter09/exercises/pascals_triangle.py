def pascals_triangle(n):
    """ Recursive function to calculate Pascals Triangle """
    if n == 1:
        return [[1]] # Base case termination condition
    else:
        result = pascals_triangle(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] # Take from end of result
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result


triangle = pascals_triangle(5)
for row in triangle:
    print(row)
