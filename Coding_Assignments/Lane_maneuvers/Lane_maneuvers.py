def analyze_drive(lanes: list[int]) -> tuple[int, int]:
    """
    Analyzes the driving behavior based on lane positions.
    
    Args:
        lanes (list[int]): List of lane positions at each second (0, 1, or 2).
    
    Returns:
        tuple[int, int]: (number of lane changes, number of dangerous maneuvers)
    """
    if len(lanes) <= 1:
        return (0, 0)
        
    lane_changes = 0
    dangerous = 0

    for i in range(len(lanes) - 1):
        first = lanes[i]
        second = lanes[i + 1]

        if first != second:
            lane_changes += 1
            if abs(first - second) == 2:
                dangerous += 1

    return (lane_changes, dangerous)
