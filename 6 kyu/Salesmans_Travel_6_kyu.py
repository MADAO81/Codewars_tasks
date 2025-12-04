# https://www.codewars.com/kata/56af1a20509ce5b9b000001e/train/python

# def travel(r, zipcode):
#     address_list = r.split(",")
#     result = []
#     for address in address_list:
#         ad_split = address.split()
#         zip = ' '.join(ad_split[-2:])
#         if zipcode == zip:
#             result.append(address.replace(zipcode,""))
#     street_num_list = []
#     street_town_list = []
#     for address in result:
#         address_split = address.split()
#         street_num = address_split[0]
#         street_town = ' '.join(address_split[1:])
#         street_num_list.append(street_num)
#         street_town_list.append(street_town)
#     street_num_list = ','.join(street_num_list)
#     street_town_list = ','.join(street_town_list)
#     return '{}:{}/{}'.format(zipcode,street_town_list,street_num_list)


def travel(r, zipcode):
    streets = []
    nums = []
    addresses = r.split(',')
    for address in addresses:
        if ' '.join(address.split()[-2:]) == zipcode:
            streets.append(' '.join(address.split()[1:-2]))
            nums += address.split()[:1]
    return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))
