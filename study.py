# study_time.py

"""
First have a tuple within a list
Then sort the list and return the best_start, best_end and max_attendance
set the three return values to zero


"""
availability = [
    (9, 11),
    (10, 12),
    (8, 11),
    (10, 13),
    (7, 11),
    (11, 14),
    (9, 15)
]
# function with parameters the available time saying it's a tuple within the list which are nade up if integers. 
# the output will be the start, end and atttendance in int

def find_best_study_time(availability: list[tuple[int, int]]) -> tuple[int, int, int]:
    """
    Return (start_time, end_time, attendance) for the earliest interval
    with the greatest number of available students.
    """
    # YOUR CODE HERE

    
    """
    times = an empty list that will look through availability and the pass it to set and then to sorted.

    for each interval in availability:
        for each time in interval:
            append to times

    """


   times = sorted(set(time for interval in availability for time in interval))


    """
    best_start time = o
    best_start end = 0
    maximum attendance = 0
    """
   best_start = best_end = 0
   max_attendance = 0



   for i in range(len(times) - 1):

        start = times[i]
        end = times[i=1]

        attendance = 0

        for s, e in availability:
            if s <= start and e >= end;
            attendance += 1

        if attendance > max_attendance:
            max_attendance = attendance
            best_start = start
            best_end = end

    return best_start, best_end, max_attendance

best_start, best_end, attendance = find_best_study_time(availability)
print(f"Best study time: {best_start}-{best_end}")
print(f"Expected attendance: {attendance} students")