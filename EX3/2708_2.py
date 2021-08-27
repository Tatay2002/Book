print("Sinovac >> SV")
print("Astrazeneca >> AZ")
print("none >> none")
print("Have been infected before >> YES")
print("Have been infected before >> NO")

X = input("First dose : ")
Y = input("Second dose : ")
Z = input("Third dose :  ")
M = input("Have you ever infected : ")

if(X == 'SV'and Y == 'SV' and Z == 'none'):
    print("Get the Pfizer as a booster.")
elif(X == 'SP'and Y == 'SP' and Z == 'none'):
    print("Get the Pfizer as a booster.")
elif(X == 'SV'and Y == 'none' and Z == 'none'):
    print("Get the Pfizer as a booster.")
elif(X == 'AZ'and Y == 'none' and Z == 'none'):
    print("Get the Pfizer as a booster.")
elif(X == 'SP'and Y == 'none' and Z == 'none'):
    print("Get the Pfizer as a booster.")
elif(X == 'SV'and Y == 'SV' and Z == 'AZ'):
    print("Not getting the Pfizer as a booster.")
elif(X == 'SV'and Y == 'AZ' and Z == 'none'):
    print("Not getting the Pfizer as a booster.")
elif(X == 'AZ'and Y == 'AZ' and Z == 'none'):
    print("Not getting the Pfizer as a booster.")
elif (X == 'none'and Y == 'none'and Z == 'none' and M == 'YES'):
    print("Get the Pfizer as a booster.")
elif (X == 'none'and Y == 'none'and Z == 'none' and M == 'NO'):
    print("Get the Pfizer as a booster.")

