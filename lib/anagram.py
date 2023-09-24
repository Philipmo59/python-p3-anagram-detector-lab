class Anagram:
    def __init__(self, word) -> None:
        self.word = word
    def match(self, list):
        self.list = list
        matched_list = []
        for word in self.list:
            if len(word) != len(self.word):
                pass
            else:
                    if sorted(word.lower()) == sorted(self.word.lower()):
                        print(word)
                        matched_list.append(word)
                    else:
                         return matched_list
        print(matched_list)
        return matched_list
    

apple = Anagram("Apple")
apple.match(['pplea',"efefefw","apwife","leapp"])