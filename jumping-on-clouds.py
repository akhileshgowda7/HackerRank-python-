def jumpingOnClouds(clouds):
    # Write your code here
    current_cloud = 0
    jumps = 0
    while current_cloud < len(clouds) - 1:
        if current_cloud + 2 < len(clouds) and clouds[current_cloud + 2] == 0:
            current_cloud += 2
        elif current_cloud + 1 < len(clouds) and clouds[current_cloud + 1] == 0:
            current_cloud += 1
        else:
            current_cloud += 1
        jumps += 1
    return jumps