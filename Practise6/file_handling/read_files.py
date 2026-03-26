with open("sample.txt" , "r") as f:
    content = f.read()
    print("------contern----\n")
    print(content)


with open("sample.txt" , "r") as f:
    print("----reading line by line----")
    for i , line in enumerate(f , 1):
        print(f"Row {i}: {line.strip()}")
