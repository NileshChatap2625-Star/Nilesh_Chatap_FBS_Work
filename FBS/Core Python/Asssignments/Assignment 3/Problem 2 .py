### 2. Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter a alphabet:")

if(alphabet in "a,e,i,o,u,A,E,I,O,U"):
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")