import numpy as np
import random as rand
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def startUp1and2():
    # Initialize a world for Scenarios 1 and 2 with 50 winter and 50 summer sports fans.
    # Randomly make 12 homes vacant and reshape into a 10x10 matrix.
    init_array = [1 if i < 50 else 2 for i in range(100)]
    rand.shuffle(init_array)
    for _ in range(12):
        rand_int = rand.randint(0, 99)
        init_array[rand_int] = 0
    world = np.array(init_array).reshape(10, 10)
    print(world)
    return world

def startUp3():
    # Initialize a world for Scenario 3 with 33 winter, 33 summer, and 34 mixed sports fans.
    # Randomly make 12 homes vacant and reshape into a 10x10 matrix.
    init_array = [1 if i < 33 else 2 if i < 66 else 3 for i in range(100)]
    rand.shuffle(init_array)
    for _ in range(12):
        rand_int = rand.randint(0, 99)
        init_array[rand_int] = 0
    world = np.array(init_array).reshape(10, 10)
    print(world)
    return world

def vacancies(world):
    # Find and return a list of vacant home locations in the world matrix.
    return np.argwhere(world == 0).tolist()

def move(row, col, vacant_homes, world):
    # Move a family from the given home to a random vacant home.
    rand_vac_house = rand.choice(vacant_homes)
    world[rand_vac_house[0], rand_vac_house[1]] = world[row, col]
    world[row, col] = 0
    return world

def whosAround(row, col, world):
    # Identify and return the neighboring cells of a given cell, wrapping around edges.
    rows, cols = world.shape
    neighbors = [
        world[row, (col - 1) % cols],
        world[row, (col + 1) % cols],
        world[(row - 1) % rows, (col - 1) % cols],
        world[(row - 1) % rows, col],
        world[(row - 1) % rows, (col + 1) % cols],
        world[(row + 1) % rows, (col - 1) % cols],
        world[(row + 1) % rows, col],
        world[(row + 1) % rows, (col + 1) % cols]
    ]
    return neighbors

def SchellingModel1(world):
    # Apply the Schelling model for Scenario 1. Homes must have less than 4 same-type neighbors.
    diff_check = 0
    for row_index in range(len(world)):
        for col_index in range(len(world[row_index])):
            if world[row_index][col_index] == 0:
                continue
            neighbors = whosAround(row_index, col_index, world)
            same_neighbor = sum(1 for neighbor in neighbors if neighbor == world[row_index][col_index])
            if same_neighbor < 4:
                diff_check += 1
                move(row_index, col_index, vacancies(world), world)
    return world, diff_check

def SchellingModel2(world):
    # Apply the Schelling model for Scenario 2. Homes must have between 1 and 4 same-type neighbors.
    diff_check = 0
    for row_index in range(len(world)):
        for col_index in range(len(world[row_index])):
            if world[row_index][col_index] == 0:
                continue
            neighbors = whosAround(row_index, col_index, world)
            same_neighbor = sum(1 for neighbor in neighbors if neighbor == world[row_index][col_index])
            if same_neighbor < 1 or same_neighbor > 4:
                diff_check += 1
                move(row_index, col_index, vacancies(world), world)
    return world, diff_check

def SchellingModel3(world):
    # Apply the Schelling model for Scenario 3. Different criteria for different sports fans.
    diff_check = 0
    for row_index in range(len(world)):
        for col_index in range(len(world[row_index])):
            if world[row_index][col_index] == 0:
                continue
            neighbors = whosAround(row_index, col_index, world)
            curr_val = world[row_index][col_index]
            same_neighbor = sum(1 for neighbor in neighbors if (curr_val in [1, 2] and neighbor in [3, curr_val]) or (curr_val == 3 and neighbor in [1, 2, 3]))
            if same_neighbor < 4:
                diff_check += 1
                move(row_index, col_index, vacancies(world), world)
    return world, diff_check

def check1(world):
    print("Scenario 1: Each home must have less than 4 neighbors of the same type.")
    print("Starting the simulation with a mix of Winter and Summer sports fans.")
    
    # Create a copy of the world for the "before" state
    world_before = world.copy()

    # Run SchellingModel1 and update the world matrix for the "after" state
    world, diff_check = SchellingModel1(world)
    while diff_check > 12:
        world, diff_check = SchellingModel1(world)

    
    labels = ['Vacant', 'Winter Sports Fan', 'Summer Sports Fan']
    cmap = plt.cm.plasma
    norm = plt.Normalize(vmin=0, vmax=2)
    patches = [mpatches.Patch(color=cmap(norm(i)), label=label) 
               for i, label in enumerate(labels)]

    # Plotting - Before
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(world_before, cmap=cmap, norm=norm)
    plt.title('Before Schelling Model: Scenario 1')

    # Plotting - After
    plt.subplot(1, 2, 2)
    plt.imshow(world, cmap=cmap, norm=norm)
    plt.title('After Schelling Model: Scenario 1')


    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    

    print("The left plot shows the initial random distribution of homes.")
    print("The right plot shows the distribution after applying the Schelling model.")
    print("Notice the emergence of clusters where fans of the same sport prefer to reside together.")
    plt.show()
    return world

def check2(world):
    print("Scenario 2: Each home must have between 1 and 4 neighbors of the same type.")
    print("Starting the simulation with a mix of Winter and Summer sports fans.")

    world_before = world.copy()

    world, diff_check = SchellingModel2(world)
    while diff_check > 12:
        world, diff_check = SchellingModel2(world)


    labels = ['Vacant', 'Winter Sports Fan', 'Summer Sports Fan']
    cmap = plt.cm.plasma
    norm = plt.Normalize(vmin=0, vmax=2)  # Assuming values are 0, 1, 2
    patches = [mpatches.Patch(color=cmap(norm(i)), label=label) 
               for i, label in enumerate(labels)]

    # Plotting - Before
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(world_before, cmap=cmap, norm=norm)
    plt.title('Before Schelling Model: Scenario 2')

    # Plotting - After
    plt.subplot(1, 2, 2)
    plt.imshow(world, cmap=cmap, norm=norm)
    plt.title('After Schelling Model: Scenario 2')


    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    

    print("The left plot shows the initial state, and the right plot shows the state after segregation.")
    print("This model demonstrates a moderate preference, leading to less pronounced segregation.")
    plt.show()
    return world

def check3(world):
    print("Scenario 3: Adapted model for fans of both Winter and Summer sports.")
    print("Starting with a mix of Winter, Summer, and Both-Seasons sports fans.")

    world_before = world.copy()

    world, diff_check = SchellingModel3(world)
    while diff_check > 12:
        world, diff_check = SchellingModel3(world)


    labels = ['Vacant', 'Winter Sports Fan', 'Summer Sports Fan', 'Both Seasons Fan']
    cmap = plt.cm.plasma
    norm = plt.Normalize(vmin=0, vmax=3)  # Assuming values are 0, 1, 2, 3
    patches = [mpatches.Patch(color=cmap(norm(i)), label=label) 
               for i, label in enumerate(labels)]

    # Plotting - Before
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(world_before, cmap=cmap, norm=norm)
    plt.title('Before Schelling Model: Scenario 3')

    # Plotting - After
    plt.subplot(1, 2, 2)
    plt.imshow(world, cmap=cmap, norm=norm)
    plt.title('After Schelling Model: Scenario 3')


    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    

    print("The left plot is the initial random setup, and the right plot is the result after segregation.")
    print("This scenario shows how a third group (fans of both seasons) affects the segregation dynamics.")
    plt.show()
    return world

