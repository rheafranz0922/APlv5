from datetime import date
def calculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return age

print(calculateAge(date(2018, 8, 5)), "years")