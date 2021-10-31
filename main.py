from matplotlib import pyplot as plt

def main():
    file_name = input('Give file name: ')
    top_most_frequent = int(input('Give amount of most frequent words to plot: '))
    file_opened = open(file_name, encoding='utf8')
    lines = file_opened.readlines()
    file_opened.close()
    words = []

    for line in lines:
        words = words + line.split()
    dict_of_words = {}
    for word in words:
        if word in dict_of_words.keys():
            dict_of_words[word] = dict_of_words[word] + 1
        else:
            dict_of_words[word] = 1

    sorted_dictionary = dict(sorted(dict_of_words.items(), key=lambda item: item[1], reverse=True))
    first_twenty_pairs = {}
    if len(sorted_dictionary) < top_most_frequent:
        plt.bar(*zip(*first_twenty_pairs.items()))
        plt.show()
    else:
        i = 0
        for word in sorted_dictionary:
            if i > top_most_frequent:
                break
            else:
                first_twenty_pairs[word] = sorted_dictionary[word]
                i += 1

        plt.barh(*zip(*first_twenty_pairs.items()))
        plt.xticks(rotation=90)
        plt.show()

if __name__ == '__main__':
    main()
