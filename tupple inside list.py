inventory=[
    ("Apple",50,0.5),
     ("Banana",75,0.3),
     ("Orange",50,0.5)
    ]
Total=0
for a,b,c in inventory:
    print(f"Total Amount{a}is {b*c}")
    Total=Total+(b*c)
    print(Total)

    
