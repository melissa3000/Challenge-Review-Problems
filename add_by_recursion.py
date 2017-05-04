# def rec_sum(n):
#     if n == 0:
#         return 0
#     return n + rec_sum(n-1)


# rec_sum(4)



# def sum_func(n):
#     if n < 10:
#         return n

#     return n%10 + sum_func(n/10)

# sum_func(4321)



def word_split(phrase,list_of_words, output = None):

    if output is None:
        output = []


    # for item in list_of_words:
    #     if item in phrase:
    #         output.append(item)
    #         return word_split(phrase.replace(item, ''), list_of_words, output)


    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output




word_split('themanran',['the','ran','man']) #==>['the', 'man', 'ran']
word_split('themanran',['clown','ran','man']) #==> []