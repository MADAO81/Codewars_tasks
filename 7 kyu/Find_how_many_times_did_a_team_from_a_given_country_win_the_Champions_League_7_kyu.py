# https://www.codewars.com/kata/581b30af1ef8ee6aea0015b9/train/python

# def count_wins(winners_list, country):
#     all_values = [val for country in winners_list for val in country.values()]
#     count = 0
#     for i in all_values:
#         if i == country:
#             count +=1
#     return count



# def countWins(winnerList, country):
#     counter = 0
#     for t in winnerList:
#         if t['country'] == country:
#             counter += 1
#     return counter



def count_wins(winners_list, country):
    return sum(x.get('country') == country for x in winners_list)
