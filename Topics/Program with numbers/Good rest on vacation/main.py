# put your python code here
days = int(input())
cost_per_day = int(input())
one_way_flight_cost = int(input())
cost_per_night_in_hotel = int(input())
print((days * cost_per_day) + ((days - 1) * cost_per_night_in_hotel) + (one_way_flight_cost * 2))