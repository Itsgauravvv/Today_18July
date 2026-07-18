# a1 = int(input("Enter the first number: "))
# if a1%2==0:
#     print(f"The number {a1} is even")
# else:
#     print(f"The number {a1} is odd")
    
    
    
    
# x = input("Enter the letter: ")
# if x.lower() in 'aeiou':
#     print(f"The letter {x} is a vowel")
# else:
#     print(f"The letter {x} is a consonant.")
    
x = input("Enter the letter: ")
y = x.strip().lower()
if y in 'aeiou':
    print(f"The letter {y} is a vowel")
else:
    print(f"The letter {y} is a consonant.")