import random

# --- Environment Setup ---
environment = {
    "A": input("Is room A Dirty or Clean? ").capitalize(),
    "B": input("Is room B Dirty or Clean? ").capitalize(),
    "C": input("Is room C Dirty or Clean? ").capitalize()
}

class Agent:
    def __init__(self, environment, location="A"):
        self.environment = environment
        self.location = location

    def perceive_and_act(self):
        # Display current grid
        self.display_environment()

        if self.environment[self.location] == "Dirty":
            print(f"Room {self.location} has been cleaned.")
            self.environment[self.location] = "Clean"
        else:
            self.move()

    def move(self):
        # Randomly choose another room
        possible_rooms = list(self.environment.keys())
        possible_rooms.remove(self.location)
        self.location = random.choice(possible_rooms)
        print(f"Moving to room {self.location}")
        self.display_environment()

    def display_environment(self):
        # Text-based grid visualization
        grid = []
        for room, state in self.environment.items():
            if room == self.location:
                grid.append(f"[{room}-Agent]")
            else:
                grid.append(f"[{room}-{state}]")
        print(" ".join(grid))

# --- Simulation Runner ---
steps = int(input("How many steps should the agent run? "))
agent = Agent(environment)

for step in range(1, steps + 1):
    print(f"\nStep {step}:")
    agent.perceive_and_act()

    # Check if all rooms are clean
    if all(state == "Clean" for state in environment.values()):
        print("All rooms are clean. Agent is idle.")
        agent.display_environment()
        break
