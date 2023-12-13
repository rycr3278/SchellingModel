from Schelling import *

def run_scenario(scenario):
    if scenario == 1:
        world = startUp1and2()
        check1(world)
    elif scenario == 2:
        world = startUp1and2()
        check2(world)
    elif scenario == 3:
        world = startUp3()
        check3(world)
    else:
        print("Invalid scenario")

def main():
    print("Welcome to the Schelling Model Simulation!")
    print("The Schelling Model is a classic simulation of segregation.")
    print("It demonstrates how individual preferences regarding neighbors can lead to the emergence of segregation, even if those preferences are not extreme.")

    print("\nIn this simulation, we have two groups of people: Winter Sports Fans and Summer Sports Fans.")
    print("Each group prefers to live in a neighborhood where there are at least some neighbors with similar interests.")
    
    print("\nThere are three scenarios in this simulation:")
    print("1) Scenario 1: Each home must have less than 4 neighbors of the same type.")
    print("2) Scenario 2: Each home must have between 1 and 4 neighbors of the same type.")
    print("3) Scenario 3: Similar to Scenario 2, but with an additional group who are fans of both Winter and Summer sports.")

    while True:
        try:
            print("\nSelect a scenario to run (1, 2, or 3) or press 0 to exit:")
            scenario = int(input())
            if scenario == 0:
                print("Exiting the simulation.")
                break
            run_scenario(scenario)
        except ValueError:
            print("Please enter a valid number (1, 2, 3, or 0).")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
