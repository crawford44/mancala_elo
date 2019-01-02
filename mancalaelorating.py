playersList = []
eloList = []
gameOutcomesList = []

#Essentially a multiplier for the Elo equation (K)
#Decreasing this value will decrease the effect of a loss or win on a players rating
KValue = 32

print('MANCALA ELO CALCULATOR')

#Must initiate at least 2 players
player = input('Input player name:')
playersList.append(player)
player = input('Input player name:')

while player.upper() != 'DONE':
    playersList.append(player)
    player = input('Input player name (Enter DONE when finished):')

#Set beginning Elo ratings (800 for complete beginner)
for plyr in playersList:
    baseElo = int(input(plyr+' base rating (800 for complete beginner): '))
    eloList.append(baseElo)

#Must input at least 1 game for Elo ratings to change
gameCount = 1
print('Game '+str(gameCount)+':')
p1Name = input('    Input name of player 1')
p2Name = input('    Input name of player 2')
p1FinalPieces = int(input('    Enter player 1\'s final piece count'))
p2FinalPieces = int(input('    Enter player 2\'s final piece count'))
gameOutcome = p1FinalPieces-p2FinalPieces
gameCount += 1

while p1Name.upper() != 'DONE':
    gameOutcomesList.append([p1Name,p2Name,gameOutcome])
    print('Game '+str(gameCount)+':')
    p1Name = input('    Input name of player 1 (Enter DONE when finished)')
    if p1Name.upper() != 'DONE':
        p2Name = input('    Input name of player 2')
        p1FinalPieces = int(input('    Enter player 1\'s final piece count'))
        p2FinalPieces = int(input('    Enter player 2\'s final piece count'))
        gameOutcome = p1FinalPieces-p2FinalPieces
    gameCount += 1

print(str(gameCount)+' game(s) recorded')

#Calculate Elo ratings after each game
for game in gameOutcomesList:
    #Determine ratings before the game
    p1OriginalRating=eloList[playersList.index(game[0])]
    p2OriginalRating=eloList[playersList.index(game[1])]
    
    
    p1TransformedRating=10**(p1OriginalRating/400)
    p2TransformedRating=10**(p2OriginalRating/400)
    #print('transformed ratings',p1TransformedRating,p2TransformedRating)

    p1ExpectedScore=p1TransformedRating/(p1TransformedRating+p2TransformedRating)
    p2ExpectedScore=p2TransformedRating/(p1TransformedRating+p2TransformedRating)
    #print('expected scores',p1ExpectedScore,p2ExpectedScore)

    p1ActualScore=.5+(game[2]/48)
    p2ActualScore=.5-(game[2]/48)
    #print('actual scores',p1ActualScore,p2ActualScore)

    p1NewElo=p1OriginalRating+(KValue*(p1ActualScore-p1ExpectedScore))
    p2NewElo=p2OriginalRating+(KValue*(p2ActualScore-p2ExpectedScore))
    #print('new elo',p1NewElo,p2NewElo)

    eloList[playersList.index(game[0])]=p1NewElo
    eloList[playersList.index(game[1])]=p2NewElo

#Display final Elo ratings for all players
for name in playersList:
    print(name+' final rating = ',end='')
    print(eloList[playersList.index(name)])
