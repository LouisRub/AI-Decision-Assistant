from logic import *

# Define symbols for different conditions
Rain = Symbol("Rain")
HeavyTraffic = Symbol("HeavyTraffic")
EarlyMeeting = Symbol("EarlyMeeting")
Strike = Symbol("Strike")
Appointment = Symbol("Appointment")
RoadConstruction = Symbol("RoadConstruction")

# Define symbols for different commuting options
WFH = Symbol("WFH")
Drive = Symbol("Drive")
PublicTransport = Symbol("PublicTransport")

# Create knowledge base
knowledge = And(
    # If it's raining or there's an early meeting, you should work from home.
    Implication(Or(Rain, EarlyMeeting), WFH),
    # If it's not raining and there's no heavy traffic, you should drive.
    Implication(And(Not(Rain), Not(HeavyTraffic)), Drive),
    # If there's no strike and it's not raining, you should take public transport.
    Implication(And(Not(Strike), Not(Rain)), PublicTransport),
    # If you have a doctor's appointment, you should drive.
    Implication(Appointment, Drive),
    # If there's road construction, you should not drive.
    Implication(RoadConstruction, Not(Drive))
)



# Define function to check each scenario
def check_scenario(knowledge, scenario):
    # Evaluate the queries against the current scenario model
    return {
        "WFH": model_check(knowledge, Implication(scenario,WFH)),
        "Drive": model_check(knowledge, Implication(scenario,Drive)),
        "Public Transport": model_check(knowledge, Implication(scenario,PublicTransport))
    }


# Define different scenarios
scenarios = [
    And(Rain, HeavyTraffic, Not(EarlyMeeting), Not(Strike), Not(Appointment), Not(RoadConstruction)),
    And(Not(Rain), Not(HeavyTraffic), Not(EarlyMeeting), Strike, Not(Appointment), Not(RoadConstruction)),
    And(Not(Rain), Not(HeavyTraffic), Not(EarlyMeeting), Not(Strike), Not(Appointment), Not(RoadConstruction))
]

# Check each scenario
for i, scenario in enumerate(scenarios):
    print(f"Scenario {i + 1}:")
    result = check_scenario(knowledge, scenario)
    print(f"WFH: {result['WFH']}")
    print(f"Drive: {result['Drive']}")
    print(f"Public Transport: {result['Public Transport']}")
    print()


