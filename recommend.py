import math

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
                  "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                    "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
         }


def manhattan( rating1, rating2 ):
    distance = 0
    for key1 in rating1:
        if key1 in rating2:
            distance = abs(rating1[key1] - rating2[key1]) + distance
    return distance


def computeNearestNeighbor( username, users ):
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(users[user], users[username], 2)
            distances.append((distance, user))
    # 按距离排序——距离近的排在前面
    distances.sort()
    return distances


def recommend( username, users ):
    """返回推荐结果列表"""
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []
    # 找出这位用户评价过、但自己未曾评价的乐队
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # 按照评分进行排序
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)


def minkowski( rating1, rating2, r ):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)
    return pow(distance, 1.0 / r)


def cossimilar( username1, username2 ):
    x3 = 0
    x1 = cossum(users[username1])
    x2 = cossum(users[username2])
    for user in users[username1]:
        try:
            x3 = x3 + users[username1][user] * users[username2][user]
        except KeyError:
            pass
    return x3 / (x1 * x2)


def cossum( users ):
    sum = 0
    for user in users:
        sum = sum + pow(users[user], 2)
    return math.sqrt(sum)


def pearson( rating1, rating2 ):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # 计算分母
    denominator = math.sqrt(sum_x2 - pow(sum_x, 2) / n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


def KNN( username1, k ):
    recom = []
    for user in users:
        if user != username1:
            recom.append((user, pearson(users[username1], users[user])))
    recom = sorted(recom, key=lambda x: x[1], reverse=True)
    return recom[:k]


def score( username, moviename, k ):
    moivescore = 0
    recommendUser = KNN(username, k)
    sumweight = 0
    for user in recommendUser:
        sumweight = sumweight + user[1]
    for user in recommendUser:
        try:
            moivescore = moivescore + (user[1] / sumweight) * users[user[0]][moviename]
        except:
            pass
    return moivescore


def recommendMovie( username, k, n ):
    movies = []
    recommendmovie = []
    for user in users:
        for movie in users[user]:
            if movie not in movies:
                movies.append(movie)
    for movie in movies:
        if movie not in users[username]:
            recommendmovie.append((movie, score(username, movie, k)))

    return sorted(recommendmovie, key=lambda x: x[1], reverse=True)[:n]


# print(score("Hailey", "Blues Traveler", 6))
print(recommendMovie("Hailey", 5, 3))
