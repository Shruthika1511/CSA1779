print("VACUUM CLEANER PROBLEM")
print("B.SHRUTHIKA-192110238")
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.current_position = (0, 0)
    def move_left(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
    def move_right(self):
        if self.current_position[1] < len(self.environment[0]) - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
    def clean(self):
        row, col = self.current_position
        self.environment[row][col] = "Clean"
    def run(self):
        num_rows = len(self.environment)
        num_cols = len(self.environment[0])
        for row in range(num_rows):
            for col in range(num_cols):
                self.current_position = (row, col)
                if self.environment[row][col] == "Dirty":
                    print(f"Current position: {self.current_position} - Cleaning...")
                    self.clean()
                else:
                    print(f"Current position: {self.current_position} - Already clean")
                if col < num_cols - 1:
                    print("Moving right")
                    self.move_right()
                elif row < num_rows - 1:
                    print("Moving to the next row")
                    self.move_left()
                print("-" * 20)
environment = [
    ["Dirty", "Clean", "Dirty"],
    ["Clean", "Dirty", "Clean"]
]
agent = VacuumCleanerAgent(environment)
agent.run()
