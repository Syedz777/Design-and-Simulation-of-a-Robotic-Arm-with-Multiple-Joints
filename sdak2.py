import numpy as np

def follow_path(path_points):
    for target_position in path_points:
        move_arm(target_position)
        # Add delay or control logic to ensure smooth movement between points

path_points = [
    np.array([0.3, 0.4, 0.1]),
    np.array([0.5, 0.5, 0.2]),
    np.array([0.4, 0.3, 0.1])
]

if __name__ == "__main__":
    follow_path(path_points)
