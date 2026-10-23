
# ==========================================================
# PART 1 - KNOWLEDGE REPRESENTATION
# ==========================================================

print("=" * 50)
print("COMPUTER TROUBLESHOOTING SYSTEM")
print("=" * 50)

print("\nINPUT")
print("Enter the following information about the computer.")

computer_on = input("Is the computer turned on? (yes/no): ").lower()
power_connected = input("Is the power cable connected? (yes/no): ").lower()
screen_black = input("Is the screen black? (yes/no): ").lower()
battery_low = input("Is the battery low? (yes/no): ").lower()
internet_connected = input("Is the internet connected? (yes/no): ").lower()

# Knowledge Base with 3 categories
facts = {
    "system_status": {
        "computer_on": computer_on == "yes",
        "internet_connected": internet_connected == "yes"
    },
    "hardware": {
        "power_connected": power_connected == "yes",
        "battery_low": battery_low == "yes"
    },
    "symptoms": {
        "screen_black": screen_black == "yes"
    }
}

print("\nKnowledge Base created successfully.")


# ==========================================================
# PART 2 - RULE-BASED REASONING
# ==========================================================

print("\n" + "=" * 50)
print("RULE-BASED REASONING (RBR)")
print("=" * 50)

actions = []

# Rule 1
if not facts["system_status"]["computer_on"] and facts["hardware"]["power_connected"]:
    actions.append("Check the battery level or power source.")

# Rule 2
if facts["symptoms"]["screen_black"] and not facts["system_status"]["computer_on"]:
    actions.append("Check the monitor/display connection and power.")

# Rule 3
if facts["hardware"]["battery_low"]:
    actions.append("Charge the computer before troubleshooting further.")

print("\nPROCESS")
print("The inference engine checks the facts against the IF-THEN rules.")

print("\nOUTPUT")
if actions:
    for action in actions:
        print("- " + action)
else:
    print("- No rule was triggered.")


# ==========================================================
# PART 3 - CASE-BASED REASONING
# ==========================================================

print("\n" + "=" * 50)
print("CASE-BASED REASONING (CBR)")
print("=" * 50)

# Past cases
case_base = [
    {
        "problem": [False, True, True, True, False],
        "solution": "Check the battery level and power connection."
    },
    {
        "problem": [True, True, True, False, False],
        "solution": "Check the monitor cable and display settings."
    },
    {
        "problem": [True, True, False, False, False],
        "solution": "Restart the computer and check for software issues."
    },
    {
        "problem": [False, False, True, True, False],
        "solution": "Connect the power cable and charge the computer."
    },
    {
        "problem": [True, False, False, False, True],
        "solution": "Check the power adapter and network settings."
    }
]

# New problem
new_problem = [
    facts["system_status"]["computer_on"],
    facts["hardware"]["power_connected"],
    facts["symptoms"]["screen_black"],
    facts["hardware"]["battery_low"]
]

# RETRIEVE
best_case = None
best_score = -1

for case in case_base:
    score = sum(a == b for a, b in zip(new_problem, case["problem"]))

    if score > best_score:
        best_score = score
        best_case = case

print("\nRETRIEVE")
print("Most similar previous case found.")

# REUSE
solution = best_case["solution"]

print("\nREUSE")
print("Reusing solution:")
print("- " + solution)

# REVISE
print("\nREVISE")
print("Solution reviewed and kept unchanged.")

# RETAIN
case_base.append({
    "problem": new_problem,
    "solution": solution
})

print("\nRETAIN")
print("New case has been added to the case base.")

print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)
