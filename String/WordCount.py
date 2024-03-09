# Given a sentence, count the distinct words in the sentence

class WordCount:
    def __init__(self):
        self.input_string = None

    def word_count(self, input_string: str):
        self.input_string = input_string
        try:
            res = len(set(self.input_string.split()))
            print(res)

        except Exception as e:
            raise e

    def word_count_dict(self, input_string: str):
        self.input_string = input_string
        try:
            words = self.input_string.split()
            word_dict = {}
            for word in words:
                word_dict[word] = word_dict.get(word, 0) + 1
            return len(word_dict)
        except Exception as e:
            raise e

    def average_word_length(self, input_string: str):
        self.input_string = input_string
        try:
            words = self.input_string.split()   # Splitting the sentence: (O(n)), where (n) is the length of the sentence.
            total = sum(len(word) for word in words)  # Computing the total length: (O(m)), where (m) is the number of words.
            print('Total lenght', total)
            return total / len(words)
        except Exception as e:
            raise e

    def average_word_length_set(self,input_string_set: set):
        self.input_string = input_string_set
        try:
            total = sum(len(word) for word in self.input_string)
            return  len(self.input_string)/total


        except Exception as e :
            raise e


if __name__ == '__main__':
    obj = WordCount()
    str_input = "Hi this is test "
    obj.word_count(str_input)
    res = obj.word_count_dict(str_input)
    print('Total words in dict : ', res)
    avg_length = obj.average_word_length(str_input)
    print('Average word length is : ', avg_length)
    avg_length_set = obj.average_word_length_set(set(str_input.split()))
    print('Average word length in set : ', avg_length)
