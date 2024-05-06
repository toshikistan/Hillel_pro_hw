def find_deepest_length(height_points):
    n = len(height_points)
    max_depth = 0

    for i in range(1, n - 1):
        left_max = max(height_points[:i])
        right_max = max(height_points[i + 1 :])

        if height_points[i] < left_max and height_points[i] < right_max:
            max_depth = max(max_depth, min(left_max, right_max) - height_points[i])

    return max_depth


depths = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 7]
print(find_deepest_length(depths))
depths = [1, 2, 6, 1, 2, 2, 3, 0, 1, 5, 7, 8, 1, 0, 3, 7, 8, 4, 1, 3, 5]
print(find_deepest_length(depths))
depths = [1, 2, 6, 1, 2, 2, 3, 0, 1, 5, 7, 8, 6, 7, 9, 2, 1]
print(find_deepest_length(depths))
depths = [1, 2]
print(find_deepest_length(depths))
depths = [1, 2, 1]
print(find_deepest_length(depths))
depths = [1, 1, 2, 1, 1]
print(find_deepest_length(depths))
depths = [1, 1, 2, 0, 1, 1]
print(find_deepest_length(depths))
