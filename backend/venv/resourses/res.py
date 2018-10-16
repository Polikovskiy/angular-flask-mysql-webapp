
import random

from datetime import datetime, timedelta


def list_6_random_numbers():               # create list of 6 random numbers(quantity transfers): according to the rules

    transfer_to_6Month = random.randint(50, 500)
    transfer_to_6Month_list = [random.randint(1, 500) for x in range(0, 6)]
    multiplayer = transfer_to_6Month/sum(transfer_to_6Month_list)
    list_6_random_numbers = list(map(lambda x: int(x*multiplayer), transfer_to_6Month_list))

    return list_6_random_numbers


def transfer_data_volume():                              # create random volume of data : according to the rules

    min_data_volume = 100
    max_data_volume = 10737418240
    transfer_data_volume = random.randint(min_data_volume, max_data_volume)

    return transfer_data_volume


def transfer_date_list(list_6_random_numbers):            # create list of transfer date per month

    transfers_date_list = []

    start = datetime.strptime('1/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
    int_delta = (30 * 24 * 60 * 60)

    def random_date(start):
        random_second = random.randrange(int_delta)
        return start + timedelta(seconds=random_second)

    for transfers in list_6_random_numbers:
        transfers_date = []
        month = list_6_random_numbers.index(transfers)
        while transfers > 0:
            transfers_date.append(str(random_date(start)))
            transfers -= 1
        start += timedelta(seconds=int_delta)
        transfers_date_list.append(transfers_date)

    return transfers_date_list
