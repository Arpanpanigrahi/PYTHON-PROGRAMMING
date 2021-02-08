str1 = input("Please Enter Your Own String:")
vowels = 0
consonants = 0
for i in str1:
    if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
        vowels = vowels + 1
    else:
        print("The consonants in this string are:",i)
        
