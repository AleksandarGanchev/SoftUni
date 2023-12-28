record_in_secounds = float(input())
distance_in_meters  = float(input())
time_in_secods_per_meter = float(input())


total_distance = distance_in_meters * time_in_secods_per_meter
delay = distance_in_meters // 15
delay_in_seconds = delay * 12.5
total_time = total_distance + delay_in_seconds

time_for_record = total_distance + delay_in_seconds

diff = record_in_secounds - total_time

if record_in_secounds <= total_time:
    print(f'No, he failed! He was {abs(record_in_secounds-total_time):.2f} seconds slower.')

else:
    print (f'Yes, he succeeded! The new world record is {time_for_record:.2f} seconds.')