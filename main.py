from matplotlib import pyplot as plt
import re

def main():
    def get_words(file_name_given):

        file_name = file_name_given
        file_opened = open(file_name, encoding='utf8') #open file, read it and regex all words
        text = file_opened.read()
        file_opened.close()
        words = re.findall('[a-zA-Z]{2,}\W', str(text))
        return words

    def create_dict_for_plotting(words_list, number_of_items):

        words = words_list # instantiate variables
        top_most_frequent = number_of_items

        dict_of_words = {}
        for word in words: # create dictionary with the word as the key and count in text as the value
            if word in dict_of_words.keys():
                dict_of_words[word] = dict_of_words[word] + 1
            else:
                dict_of_words[word] = 1

        sorted_dictionary = dict(sorted(dict_of_words.items(), key=lambda item: item[1], reverse=True)) # sort the dict based on values
        pairs_to_plot = {}
        if len(sorted_dictionary) < top_most_frequent:
            plt.bar(*zip(*pairs_to_plot.items()))
            plt.show()
        else:
            i = 0
            for word in sorted_dictionary:
                if i > top_most_frequent:
                    break
                else:
                    pairs_to_plot[word] = sorted_dictionary[word]
                    i += 1
        return pairs_to_plot

    file_name = input('Give file name: ')
    top_most_frequent = int(input('Give amount of most frequent words to plot: '))

    pairs = create_dict_for_plotting(get_words(file_name), top_most_frequent)
    plt.barh(*zip(*pairs.items()))
    plt.xticks(rotation=90)
    plt.show()

if __name__ == '__main__':
    main()
