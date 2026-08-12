def calculate_space_weight(earth_weight, destination):
    destination = destination.lower()

    if destination == "Mars":
        return earth_weight * 0.38
    
    elif destination == "Jupiter":
        return earth_weight * 2.34
    
    elif destination == "Moon":
        return earth_weight * 0.16
    else:
        
        print("Error")
        return 0



print(calculate_space_weight(70,"mars"))