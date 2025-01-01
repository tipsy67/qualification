
def str_list_to_int(list_):
    return [int(x) for x in list_]

def create_time_slots():
    duration = 30
    time = '10:00'
    time_list = str_list_to_int(time.split(':'))
    end_time = '16:00'
    end_time_list = str_list_to_int(end_time.split(':'))
    time_slots = []
    while time_list[0] < end_time_list[0]:
        time = f"{time_list[0]:02}" + ':' + f"{time_list[1]:02}"
        time_slots.append((time,time))
        time_list[1] = time_list[1] + duration
        if time_list[1] >=60:
            time_list[0] = time_list[0] + time_list[1]//60
            time_list[1] = time_list[1]%60

    return time_slots

def get_time_slots():
    return create_time_slots()