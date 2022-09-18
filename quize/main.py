import team as tm

teamA=tm.Team(101,'Chilly')
teamA.addPoint()
teamB=tm.Team(102,'Salt')
teamB.addPoint()
print("***** after first round*****")

teamA.display()
teamB.display()
print("****After Second Round")
teamA.subPoint()
teamB.addPoint()
teamA.display()
teamB.display()
# print(teamB.__iteamid)
print('main')