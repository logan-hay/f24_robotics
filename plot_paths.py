import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

SPAWN_POINT = 4
MIN_TRIAL = 1
MAX_TRIAL = 5

def plot_paths():
    image = mpimg.imread('/mnt/c/Users/ljhay/f24_robotics/Homework1/apartment.png')
    fig, ax = plt.subplots()
    ax.imshow(image, extent=[-0.85, 11.45, -0.5, 9.9]) 

    for trial in range(MIN_TRIAL, MAX_TRIAL + 1): 
        file_path = f'trials/spawn_{SPAWN_POINT}/trial_{SPAWN_POINT}_{trial}.trial'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                paths = f.readlines()
                x_vals, y_vals = zip(*[map(float, line.strip().split(',')) for line in paths])
                ax.plot(x_vals, y_vals, marker='o', label=f'Trial {trial}')

    plt.title(f"Robot Paths From Spawn Point {SPAWN_POINT}")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.xlim(0, 10.5)  
    plt.ylim(0, 9.3)
    plt.grid()
    plt.legend()
    
    save_path = f'robot_paths_{SPAWN_POINT}.png'
    plt.savefig(save_path)
    print(f"Saved plot as {save_path}")

    plt.close(fig) 

if __name__ == '__main__':
    plot_paths()
