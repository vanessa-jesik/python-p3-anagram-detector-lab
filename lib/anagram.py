class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_list):
        return [possibility for possibility in possible_list if
                sorted(possibility) == sorted(self.word)]