def CemMidterm2457794 (shareList, file):
    totalShares = 0
    count = 0
    topShareholders = 1
    numShares = input ("Please enter the number of shares: ")
    numShares = int(numShares)
    while numShares != 0:
        shareList.append(numShares)
        totalShares = totalShares + numShares
        numShares = input ("Please enter the number of shares: ")
        numShares = int(numShares)
        if numShares == 0:
            print("Thank you, there is a total of %d " %totalShares, "shares represented here.")
            string = "Thank you, there is a total of " + str(totalShares) + " shares represented here.\n"
            file.write(string)
            majorityVote = (totalShares/2) + 1
            print("Shared needed for majority vote is %d." %majorityVote)
            string = "Shared needed for majority vote is " + str(majorityVote) +".\n"
            file.write(string)

    while shareList:
        count += max(shareList)
        shareList.remove(max(shareList))
        if count >= majorityVote:
            print("You need the support of top %d" %topShareholders,  "shareholders for this number of votes.")
            string = "You need the support of top " +str(topShareholders)+ " shareholders for this number of votes.\n"
            file.write(string)
            break
        else:
            topShareholders += 1

shareList = []
file= open("CemMidterm2457794.txt","w")
CemMidterm2457794(shareList, file)
file.close()