def leaderboard(score, time_taken, user_name):
 
    file = open("leaderboard.txt", 'a')
    file.write(f"\t{score}\t{time_taken}\t{user_name}\n")
    file.close()
 
    file = open("leaderboard.txt", 'r')
    readthefile = file.readlines()
    sortedData = sorted(readthefile, reverse=True)
    
    print("==============================")
    print("    Top 5 Winning Scores")
    print()

    print("Pos\t" + "Score\t" + "Time\t" + "Name")

    for line in range(5):
        print (f" {str(line + 1)}{str(sortedData[line])}")


