
# Mealy Machine: Binary Pattern 101 Detector

## Description
This project implements a Mealy Machine using Python. It detects the binary pattern `101` in an input string and generates an output sequence.

## Objectives
- Implement a Mealy Machine in Python.
- Demonstrate state transitions for binary inputs.
- Generate output based on the current state and input symbol.
- Test valid binary strings.

## Input Alphabet
The machine accepts the binary symbols:
- `0`
- `1`

## States
- `q0`: No relevant part of the pattern has been matched.
- `q1`: The pattern begins with `1`.
- `q2`: The pattern prefix `10` has been matched.

## Output
- `0`: The pattern has not been completed at this step.
- `1`: The pattern `101` has been detected at this step.

## Transition Table

| Current State | Input 0 | Input 1 |
|---|---|---|
| q0 | q0 / 0 | q1 / 0 |
| q1 | q2 / 0 | q1 / 0 |
| q2 | q0 / 0 | q1 / 1 |

Each table entry shows the next state followed by the output.

## Sample Inputs
- `101`: Pattern detected
- `1101`: Pattern detected
- `000`: Pattern not detected
- `111`: Pattern not detected

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   `python Mealy_Machine_Pattern101.py`

5. Enter a binary string containing only `0` and `1`.
6. Type `exit` to stop the program.

## Author
Renier P. Apal

## Subject
Automata Theory and Formal Languages
