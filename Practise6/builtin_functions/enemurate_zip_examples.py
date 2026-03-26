names = ["Alice" , "Bob" , "Charlie"]
scores = [86 , 92 , 100]


print("Enemurate examples..")
for idx , name in enumerate(names , start=1):
    print(f"{idx}. {name}")

print("\nZip examples : ")
for name , score in zip(names , scores):
    print(f"{name} : got score  {score}")


val_str = "100"
val_int = int(val_str)
print(f"\nType check : {type(val_int)} | Value : {val_int}")


