def fuse_readings(sensor1: list[int], sensor2: list[int], sensor3: list[int]) -> list:
    """
    Combines sensor readings using majority vote logic.  
    If no majority exists (all different), fall back to the average of the three readings.  
    
    Args:
        sensor1, sensor2, sensor3 (list[int]): Readings from 3 sensors.
    
    Returns:
        list: Final fused readings for each timestep.
              - Majority value if at least 2 sensors agree.
              - Average value if no consensus.
    """
       """

    if not sensor1 or not sensor2 or not sensor3:
        return []

    fused = []
    for s1, s2, s3 in zip(sensor1, sensor2, sensor3):
        if s1 == s2 or s1 == s3:
            fused.append(s1)
        elif s2 == s3:
            fused.append(s2)
        else:
            fused.append((s1 + s2 + s3) / 3)
    return fused


sensor1 = [80, 70, 60, 90]
sensor2 = [80, 72, 60, 91]
sensor3 = [82, 70, 59, 90]

print(fuse_readings(sensor1, sensor2, sensor3))  # Expected: [80, 70, 60, 90]

s1 = [10, 20, 30]
s2 = [40, 50, 60]
s3 = [70, 80, 90]

print(fuse_readings(s1, s2, s3))  # Expected: [40.0, 50.0, 60.0]

