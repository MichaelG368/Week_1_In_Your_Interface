class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.index = 0

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, person):
        if person in self.__myTeam:
            return True
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            person = self.__myTeam[self.index]
        except IndexError:
            raise StopIteration
        self.index +=1
        return person
            
        
def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print('Tim' in classmates)
  print('Sam' in classmates)
  
  for people in classmates:
    print(people)

main()