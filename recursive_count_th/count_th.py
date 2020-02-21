'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    def helper(subword, subcount):
        if len(subword) <= 1:
            return subcount
        if subword[0] == "t" and subword[1] == "h":
            subcount += 1
        return helper(subword[1:], subcount)

    count = helper(word, count)

    return count


def count_th_iter(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == "t" and word[i + 1] == "h":
            count += 1

    return count