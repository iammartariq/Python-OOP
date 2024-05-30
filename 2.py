class String(str):
    def word_count(self):
        return len(self.split()) 
    
    #if we want to count the number of alphabets we will not use split()
    
a = String("Ammar tariq")
print(a.word_count())