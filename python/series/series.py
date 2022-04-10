def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("The series is not long enough.")
    return [
        series[i : i + length]
        for i, _ in enumerate(series)
        if len(series[i : i + length]) == length
    ]
