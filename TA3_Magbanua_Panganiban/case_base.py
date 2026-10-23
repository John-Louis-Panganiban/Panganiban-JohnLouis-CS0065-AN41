# Step 3: Define Case Base
case_base = [
    {
        "student": "Student A",
        "error": "Wrong Formula",
        "topic": "Algebra",
        "solution": "Review algebra formulas and complete 5 practice problems."
    },
    {
        "student": "Student B",
        "error": "Arithmetic Error",
        "topic": "Fractions",
        "solution": "Practice fraction operations and complete worksheet exercises."
    },
    {
        "student": "Student C",
        "error": "Sign Error",
        "topic": "Integers",
        "solution": "Review positive and negative number rules."
    },
    {
        "student": "Student D",
        "error": "Wrong Formula",
        "topic": "Geometry",
        "solution": "Study geometry formulas and answer review questions."
    },
    {
        "student": "Student E",
        "error": "Calculation Error",
        "topic": "Decimals",
        "solution": "Complete decimal exercises and check work carefully."
    }
]

# Step 4: Similarity Assessment (Attribuite matching)
new_case = {
    "student": "Student F",
    "error": "Wrong Formula",
    "topic": "Algebra"
}

print("\nNEW PROBLEM")
print("-" * 30)
print(f"Student: {new_case['student']}")
print(f"Error: {new_case['error']}")
print(f"Topic: {new_case['topic']}")

best_case = None
highest_score = -1

print("\nSIMILARITY SCORES")
print("-" * 30)

for case in case_base:
    score = 0

    if case["error"] == new_case["error"]:
        score += 1

    if case["topic"] == new_case["topic"]:
        score += 1

    print(f"{case['student']}: {score}")

    if score > highest_score:
        highest_score = score
        best_case = case

print("\nMOST RELEVANT CASE")
print("-" * 30)
print(f"Student: {best_case['student']}")
print(f"Error: {best_case['error']}")
print(f"Topic: {best_case['topic']}")
print(f"Similarity Score: {highest_score}")


# Step 5: Adapt the Solution
adapted_solution = best_case["solution"]

if new_case["error"] == "Wrong Formula":
    adapted_solution += " Study worked examples and focus on formula selection."

elif new_case["error"] == "Arithmetic Error":
    adapted_solution += " Practice calculation exercises and check each step carefully."

elif new_case["error"] == "Sign Error":
    adapted_solution += " Review positive and negative number rules with guided exercises."

print("\nADAPTED FINAL SOLUTION")
14
print("-" * 30)
15
print(adapted_solution)


# Step 6: Retain Stage
new_case["solution"] = adapted_solution
case_base.append(new_case)

print("\nCASE SAVED")
print("-" * 30)
print("New case saved successfully!")

print("\nUPDATED CASE BASE")
print("-" * 30)

for case in case_base:
    print(f"Student: {case['student']}")
    print(f"Error: {case['error']}")
    print(f"Topic: {case['topic']}")
    print(f"Solution: {case['solution']}")
    print()