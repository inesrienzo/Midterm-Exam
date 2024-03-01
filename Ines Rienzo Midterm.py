# Question 1
a = 6
a = a - 2
print(a*2)  # This will print 8
a = a * 2
print(a+1)  # This will print 9
a = a // 3  # Performs integer division of a by 3
# If you want to see the final value of a, you can print it as well
print(a)  # This will print 2

# Question 2
# Let's execute the code to confirm what it will print
result = (3 + 10**2 / 2) or 70.0
print(result)

# Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Question 4
def palindrome(word):
   if word == word[::-1]:
      return True
   else:
      return False


# Example usage
test_word = "7798338247658278460338648728567428338977"
result = palindrome(test_word)
print(result)

# Question 5
def find_patterns(text):
   count = 0

   for i in range(len(text)):
      if text[i] == 'C':

         for j in range(i + 1, len(text) - 2):

            if text[j:j + 3] == 'jeb':
               count += 1
               break

   return count


text_example = "Cabcjeb is a test string with C123jeb patterns and one without end Cnope."
pattern_count = find_patterns(text_example)
print("Found patterns:", pattern_count)

# Question 6
original_string = "Hello"

try:
   original_string[0] = "J"
except TypeError as e:
   print(f"Error: {e}")

new_string = original_string + ", World!"
print(new_string)

print(original_string)

my_list = [1, 2, 3]
print(f"Original list: {my_list}")

my_list[0] = 10
print(f"Modified list: {my_list}")

my_list.append(4)
print(f"List after adding an element: {my_list}")

my_list.remove(2)
print(f"List after removing an element: {my_list}")



# Question 7
import random

random_numbers = []
for i in range(10):
   random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):
   if random_numbers[i] > 80:
       random_numbers[i] = -random_numbers[i]

print(random_numbers)

# Question 8
def is_valid_url(url):
   # Check if it starts with http:// or https://
   if not (url.startswith("http://") or url.startswith("https://")):
      return False

   # Check if the URL contains a dot
   if '.' not in url:
      return False

   # Check if the URL contains spaces
   if ' ' in url:
      return False

   return True


# Examples
print(is_valid_url("https://www.inesrienzo.com"))  # True
print(is_valid_url("www.inesrienzo.com"))  # False


# Question 9
def calculate_days_since_birthday(birthday):
   current_year = 2024


   birth_year = int(birthday.split("/")[2])




   full_years_passed = current_year - 1 - birth_year




   days_passed = full_years_passed * 365




   leap_years = 0
   for year in range(birth_year + 1,
                     current_year):
       if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
           leap_years += 1




   days_passed += leap_years


   return days_passed




birthday_ines = "05/07/2003"
days_passed_ines = calculate_days_since_birthday(birthday_ines)
print(f"Days passed since Ines's birthday (excluding birth year and current year): {days_passed_ines}")
