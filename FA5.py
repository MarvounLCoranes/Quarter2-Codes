destinations = []
print("Please enter your 5 travel destinations:")
for i in range(5):
    place = input("Destination " + str(i+1) + ": ")
    destinations.append(place)

print()
print("Original Travel Itinerary:")
for i in range(5):
    print(str(i+1) + ". " + destinations[i])

print()
print("Let's update your 2nd and 5th destinations.")
new2 = input("Enter a new destination for position 2: ")
new5 = input("Enter a new destination for position 5: ")

destinations[1] = new2
destinations[4] = new5

print()
print("Updated Travel Itinerary:")
for i in range(5):
    print(str(i+1) + ". " + destinations[i])
