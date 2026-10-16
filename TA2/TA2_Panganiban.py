# --- Task 1: Environment Setup ---
# Initialize two rooms using a dictionary
environment = {
    "A": input("Is room A Dirty or Clean? ").capitalize(),
    "B": input("Is room B Dirty or Clean? ").capitalize()
}

# --- Task 2: Rule-Based Agent ---
class Agent:
    def __init__(self, environment, location="A"):
        self.environment = environment
        self.location = location

    def perceive_and_act(self):
        # Rule 1: Clean if dirty
        if self.environment[self.location] == "Dirty":
            print(f"Room {self.location} has been cleaned.")
            self.environment[self.location] = "Clean"
        else:
            # Rule 2: Move if clean
            self.move()

    def move(self):
        # Switch between rooms
        self.location = "B" if self.location == "A" else "A"
        print(f"Moving to room {self.location}")

# --- Task 3: Run the Simulation ---
steps = int(input("How many steps should the agent run? "))
agent = Agent(environment)

for step in range(1, steps + 1):
    print(f"\nStep {step}: Agent is in room {agent.location}")
    agent.perceive_and_act()
    print("Environment state:", environment)
