def print_trains(trains):
    for train in trains:
        print('*', train)

def trains_in_direction(trains, direction):
    trains_direction = []
    for train in trains:
        if train['direction'] == direction:
            trains_direction.append(train)
    return trains_direction

def map_trains_to_freq(trains):
    trains_by_frequency = {}
    for train in trains:
        name = train['train']
        freq = train['frequency_in_minutes']
        if freq in trains_by_frequency:
            trains_by_frequency[freq].append(name)
        else:
            trains_by_frequency[freq] = [name]
    return trains_by_frequency

# all the trains
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# train 111
train_111 = trains[len(trains) - 1]
print()
print("Train 111:")
print(train_111)

# frequency of train 80B
print()
print("Frequency of train 80B is:")
train_80B_freq = trains[5]['frequency_in_minutes']
print(train_80B_freq)

#direction of train 610
print()
print("Direction of train 610 is:")
train_610_dir = trains[2]['direction']
print(train_610_dir)

# trains traveling north
north_trains = trains_in_direction(trains, 'north')
print()
print("All trains traveling north:")
print_trains(north_trains)

# trains traveling east
east_trains = trains_in_direction(trains, 'east')
print()
print("All trains traveling east:")
print_trains(east_trains)

# add new key/value pair to train 72C called first_departure_time
trains[0]['first_departure_time'] = 7
print()
print("The list of all trains:")
print_trains(trains)

# show trains for each frequency
trains_by_frequency = map_trains_to_freq(trains)
print()
print("Here are the trains by frequency:")
print(trains_by_frequency)
