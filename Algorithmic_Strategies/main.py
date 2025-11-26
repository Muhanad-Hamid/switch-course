def get_largest_num(a, b, c):
    largest_num = a
    if b > a:
        largest_num = b
    if c > largest_num:
        largest_num = c
    return largest_num

def get_highest_scoring_word(str):
    words = str.split()
    highest_scoring_word = ""
    highest_score = -1
    for word in words:
        score = sum(ord(ch) - ord('a') + 1 for ch in word)
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word
    return highest_scoring_word