# My messy phone contacts (15 items total, 5 are messy duplicates)
messy_contacts = [
    "Tunde", "Amaka", "Chidi", "Ngozi", "Emeka", 
    "Bisi", "Kwame", "Aisha", "Femi", "Sade", 
    "tunde ", "AMAKA", " chidi", "ngozi  ", " EMEKA"
]
# Create empty sets to hold our clean data and our duplicates
clean_contacts = set()
duplicates = set()

# Loop through every single messy contact one by one
for contact in messy_contacts:
    
    # 1. Clean the name: remove spaces (.strip) and fix capitals (.title)
    clean_name = contact.strip().title()
    
    # 2. Sort them into the correct baskets
    if clean_name in clean_contacts:
        duplicates.add(clean_name)
    else:
        clean_contacts.add(clean_name)

# 3. Print the final report
print("--- CONTACT CLEANUP REPORT ---")
print(f"Clean Contacts: {clean_contacts}")
print(f"Duplicates Found & Removed: {duplicates}")