Gender = input("Enter Gender (M/F) :")
age = int(input("Enter age :"))

if(Gender== "F"):
    if(age>=18):
      print("Girl is eligible")
    else:
       print("girl is not eligible")
else:
   if(age>=21):
      print("boy is eligible")
   else:
      print("boy is not eligible")          
