# My monthly budget vs actual spending
# Format: ("Category", Budgeted_Amount, Actual_Amount)
budget_data = [
    ("Groceries", 50000, 55000),
    ("Transport", 20000, 18000),
    ("Airtime", 5000, 5000),
    ("Entertainment", 15000, 20000)
]

# We need variables starting at zero to keep a running tally
total_budgeted = 0
total_spent = 0

print("--- BUDGET BREAKDOWN ---")

# Loop through each tuple in our list
for item in budget_data:
    # item[0] is the name, item[1] is budget, item[2] is actual
    category = item[0]
    budget = item[1]
    actual = item[2]
    
    # Add this category's money to our running tally
    total_budgeted = total_budgeted + budget
    total_spent = total_spent + actual
    
    # Check our spending for this specific category
    if actual > budget:
        overspent = actual - budget
        print(f"Alert! You overspent on {category} by {overspent}")
    elif actual < budget:
        saved = budget - actual
        print(f"Great! You saved {saved} on {category}")
    else:
        print(f"Spot on! You spent exactly your budget for {category}")

# Print the final grand totals
print("--- FINAL TOTALS ---")
print(f"Total Budgeted: {total_budgeted}")
print(f"Total Spent: {total_spent}")

if total_spent > total_budgeted:
    print("Conclusion: You went over your total budget this month.")
else:
    print("Conclusion: You stayed within your total budget!")