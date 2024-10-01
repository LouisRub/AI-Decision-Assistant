# AI-Decision-Assistant

# Commuting Decision-Making Using Propositional Logic
### Project Overview

This project simulates AI-based decision-making for commuting options using propositional logic. The goal is to help decide whether to Work From Home (WFH), Drive, or take Public Transport based on various conditions such as weather, traffic, and appointments. The project leverages logical rules to evaluate different commuting choices based on the input scenario.

### Key Features:
- Logical Reasoning: The decision-making process uses propositional logic to infer the best commuting option based on the conditions provided.
- Handling: It evaluates multiple scenarios, considering factors such as rain, heavy traffic, early meetings, strikes, appointments, and road construction.
- Automated Model Checking: The system uses a model-checking approach to validate commuting decisions for each scenario.

### Conditions:

- Weather: Rain or no rain.
- Traffic: Heavy traffic or normal traffic.
- Appointments: Doctor’s appointments.
- Early Meetings: Whether there is an early meeting.
- Strikes: Public transport strikes.
- Road Construction: Ongoing road construction.

### Rules in the Knowledge Base:

- If it’s raining or there's an early meeting, you should Work From Home (WFH).
- If it’s not raining and there’s no heavy traffic, you should Drive.
- If there’s no strike and it’s not raining, you should take Public Transport.
- If you have a doctor’s appointment, you should Drive.
- If there’s road construction, you should not Drive.

## How to Run the Python Code
### Prerequisites

Ensure you have the following installed:

Python 3.x

### Running the Script

python commuting_decision.py