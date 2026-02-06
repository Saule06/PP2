dict={
    "Saule": 100,
    "Damir": 80,
    "Ayana": 70
    
}

gpa={}
for name,score in dict.items():
    if 95<= score<=100:
        gpa[name]=4.0
    elif 90<=score<95:
        gpa[name]=3.67
    elif 85<=score<90:
        gpa[name]=3.33
    elif 80<=score<85:
        gpa[name]=3.00
    elif 75<=score<80:
        gpa[name]=2.67
    elif 70<=score<75:
        gpa[name]=2.33
    elif 65<=score<70:
        gpa[name]=2.0
    elif 60<=score<65:
        gpa[name]=1.67
    else:
        gpa[name]=0.0

for name, score in gpa.items():
    print(name, "GPA =", score)