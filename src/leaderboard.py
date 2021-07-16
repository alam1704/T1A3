def leaderboard(score, time_taken, user_name):
 
    file = open("leaderboard.txt", 'a')
    file.write(f"{score}     {time_taken}       {user_name}\n")
    file.close()
 
    file = open("leaderboard.txt", 'r')
    readthefile = file.readlines()
    sortedData = sorted(readthefile, reverse=True)
    
#def sorter(item):
#    score = item[1]
#    time = item[2]
#    return (score, time)

#sorted_list = sorted(leaderboard(), key=sorter)
#print(sorted_list)

    print("==============================")
    print("    Top 5 Winning Scores")
    print()

    print("Pos        " + "Score     " + "Time     " + "   Name")

    for line in range(5):
        print (" " + str(line + 1) + "\t    " + str(sortedData[line]))




