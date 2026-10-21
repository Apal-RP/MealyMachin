class Pattern101MealyMachine:
    def __init__(self):
        self.state = "q0"

        # Transition function: delta(state, input) -> next_state
        self.transitions = {
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q2", "1": "q1"},
            "q2": {"0": "q0", "1": "q1"},
        }

    def step(self, symbol: str) -> tuple[int, str]:
        """Processes one binary digit and returns (output_bit, new_state)."""
        if symbol not in {"0", "1"}:
            raise ValueError("Input must contain only 0 and 1.")

        # Output 1 when the input completes the pattern 101.
        output = 1 if self.state == "q2" and symbol == "1" else 0

        # Move to the next state.
        self.state = self.transitions[self.state][symbol]
        return output, self.state

    def run(self, input_string: str):
        """Runs the machine and prints a step-by-step trace."""
        self.state = "q0"
        output_bits = []

        print("\n--- Execution Trace ---")
        print(f"{'Step':<6} | {'Input':<8} | {'Next State':<12} | {'Output'}")
        print("-" * 43)

        for idx, symbol in enumerate(input_string, start=1):
            if symbol not in {"0", "1"}:
                print(f"Invalid input {symbol!r}. Use only 0 and 1.")
                return

            output, next_state = self.step(symbol)
            output_bits.append(str(output))
            print(f"{idx:<6} | {symbol:<8} | {next_state:<12} | {output}")

        output_sequence = "".join(output_bits)
        detected = "YES" if "1" in output_sequence else "NO"

        print("-" * 43)
        print(f"Final State:       {self.state}")
        print(f"Output Sequence:   {output_sequence}")
        print(f"Pattern 101 Found: {detected}\n")


if __name__ == "__main__":
    machine = Pattern101MealyMachine()

    print("=" * 48)
    print("Mealy Machine: Binary Pattern 101 Detector")
    print("=" * 48)
    print("Valid input examples:")
    print("  Pattern found:     101, 1101, 1010, 10101")
    print("  Pattern not found: 000, 111, 100, 110")
    print("Type 'exit' to quit.")
    print("=" * 48)

    while True:
        try:
            user_input = input("Enter a binary string: ").strip()
            if user_input.lower() == "exit":
                break
            if not user_input:
                print("Please enter a binary string.\n")
                continue
            machine.run(user_input)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break
