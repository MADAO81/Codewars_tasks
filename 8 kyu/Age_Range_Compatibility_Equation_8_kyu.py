# Age Range Compatibility Equation
# Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself).
# It's the 'recommended' age range in which to date someone.

def dating_range(age):
    if age > 14:
        min_age = (age/2)+7 
        max_age = 2*(age-7)
    else:
        min_age = age - 0.10 * age
        max_age = age + 0.10 * age
    return (f"{int(min_age)}-{int(max_age)}")
