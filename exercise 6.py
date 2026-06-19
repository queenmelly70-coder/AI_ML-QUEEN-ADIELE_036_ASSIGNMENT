all_students = {"Tunde", "Amaka", "Chidi", "Ngozi", "Emeka", "Bisi", "Kwame", "Aisha", "Femi", "Sade"}
monday = {"Tunde", "Amaka", "Chidi", "Kwame"}
tuesday = {"Tunde", "Amaka", "Bisi", "Femi", "Sade"}
wednesday = {"Tunde", "Chidi", "Ngozi", "Bisi"}
perfect_attendance = monday & tuesday & wednesday
print(f"Attended all 3 days: {perfect_attendance}")