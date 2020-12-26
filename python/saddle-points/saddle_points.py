def saddle_points(matrix):
    if any(map(lambda row: len(row) != len(matrix[0]), matrix)):
        raise ValueError("Wrong matrix format")
    saddle_points = []

    potential_point_row = [
        [[row_idx, i] for i, value in enumerate(row) if value == max(row)]
        for row_idx, row in enumerate(matrix)
    ]

    for points in potential_point_row:
        for point_row, point_col in points:
            if matrix[point_row][point_col] == min(
                list(map(list, zip(*matrix)))[point_col]
            ):
                saddle_points.append({"row": point_row + 1, "column": point_col + 1})

    return saddle_points
