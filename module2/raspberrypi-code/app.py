from first_n_terms_gs import *
from serial_connection import * 

u = input("Please enter the First Term of your GS: ")
print("You entered: " + u)

r = input("Please enter the Ratio of your GS: ")
print("You entered: " + r)

N = input("Please enter the Number Of Terms of your GS: ")
print("You entered: " + N)

error_check = input("Do you want error detection? Type 'y/n': ")
print("You entered: " + error_check)

if error_check == 'y':
    error_check = True
else:
    error_check = False
    
result = first_n_terms_gs(int(u), int(r), int(N))

print("Here are the first", N, "terms of your GS:")
print(result)

# Open the file in write mode
file = open("filename.txt", "w")

# Write content to the file
content = "This is the content to be written."
file.write(content)

# Close the file
file.close()

write_to_port(result, error_check)
