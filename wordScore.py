def highestScoringWord(sentence):
    max_score=0
    highest_scoring_word=""
    words=sentence.split()
    for word in words:
        word_score=0
        for letter in word:
            word_score +=(ord(letter)-96)
        if word_score>max_score:
             max_score=word_score
             highest_scoring_word=word

    return highest_scoring_word
