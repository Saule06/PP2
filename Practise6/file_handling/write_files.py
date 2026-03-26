with open("sample.txt" , "w", encoding="utf-8") as file:
    file.write("Line 1 : HEllo Python\n")
    file.write("Line 2 : Practical Exercise 6\n")

print("File sample.txt created and data written")


with open("sample.txt" , "a" , encoding="utf-8") as file:
    file.write("Line 3 : appended new writings to  the same file \n ")

print("New file added")

