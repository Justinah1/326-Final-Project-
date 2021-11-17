""" This python script would be used to implement the experimental 
skeleton code of some of our methods that we've decided on for the final project"""


def highscore(file_path):
    """This method is used to keep track of the highscores 
    of the top 10 players in the game
    
    Args:
    file_path (str): this is the path to the text file needed to run the program
    """
    UserName = str(input("Enter a UserName: "))
    s = int(input("Enter new score: "))
    l =[UserName,s]
    with open(file_path, "r", encoding="utf-8") as f:
        f = f.readlines()
        score = []
        for line in f:
            line = line.strip()
            score.append(line.split(" "))
    
    score.sort(key=lambda x:int(x[1]), reverse = True)
    lowest_score = int(score[-1][1])
    highest_score = int(score[0][1])
    if s <= lowest_score:
        if len(score)>=10:
            score.pop()
        score.insert(-1, l)
    elif s >= highest_score:
        if len(score) >= 10:
            score.pop()
        score.insert(0, l)
    elif s > lowest_score and s < highest_score:
        if len(score)>= 10:
            score.pop()
        score.append(l)
        
    score.sort(key=lambda x:int(x[1]), reverse = True)
    # with open(file_path, "w", encoding="utf-8") as f:
    #     for content in score:
    #         f.write(content)
    # f.close()
    # updated_list = str(score)
    # with open(file_path, "w", encoding="utf-8") as f:
    #     for content in str(score):
    #         f.write('\t'.join(content) + "\n")
    print(score)
        
    
            
        

highscore("highscore.txt")