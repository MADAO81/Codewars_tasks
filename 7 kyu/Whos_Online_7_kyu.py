# https://www.codewars.com/kata/5b6375f707a2664ada00002a/train/python

# from collections import defaultdict

# def who_is_online(friends):
#     d = defaultdict(list)
#     for user in friends:
#         status = 'away' if user['status'] == 'online' and user['last_activity'] > 10 else user['status']
#         d[status].append( user['username'] )
#     return d


def who_is_online(friends):
    # Allocate each name to a group
    online, offline, away = [], [], []
    for d in friends:
        if d['status'] == 'offline':
            offline.append(d['username'])
        elif d['last_activity'] <= 10:
            online.append(d['username'])
        else:
            away.append(d['username'])
    
    # Build a complete result and then filter out keys where there is no value
    result = {'online': online, 'offline': offline, 'away': away}
    return {k: v for k, v in result.items() if v}
