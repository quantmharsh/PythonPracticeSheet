n = int(input("enter no of workers"))
target_Toys=int(input("enter no of toys"))
day =int(input("enter no of days"))
Toys_made=int(input("enter no of toys made"))
day_passed=int(input("enter no of days passed"))

produtionPerDay=Toys_made/day_passed
menWorkPerDay=produtionPerDay/n
worksLeft=target_Toys-Toys_made
daysLeft=day-day_passed
reqWorkForce=daysLeft*menWorkPerDay
totalMenRequired=worksLeft/reqWorkForce
RemainingMen=totalMenRequired-n
print("Extra Men required",RemainingMen)





