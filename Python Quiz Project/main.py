import random

class Question:
     def __init__(self):
          self.quiz1 = [
               {"Question": "What is the name of our galaxy?", "Responses": "(a) Andromeda\n(b) Milky Way\n(c) Canis Major Dwarf\n(d) Draco II", "Answer": "b"}, #0
               {"Question": "What is the Capital City of Canada?", "Responses": "(a) Ottawa\n(b) Toronto\n(c) Vancouver\n(d) Montreal", "Answer": "a"}, #1
               {"Question": "What is the population of Canada?", "Responses": "(a) 26 Million\n(b) 43 Million\n(c) 34 Million\n(d) 38 Million" , "Answer": "d"}, #2
               {"Question": "Who won the 2019 NBA Championship?", "Responses": "(a) Warriors\n(b) Bucks\n(c) Raptors\n(d) Trail Blazers", "Answer": "c"}, #3
               {"Question": "How old is the sun?", "Responses": "(a) 4.6 Billion Years\n(b) 3.9 Billion Years\n(c) 6.2 Billion Years\n(d) 3.4 Billion Years", "Answer": "a"}, #4
               {"Question": "What is the main religion of India?", "Responses": "(a) Christianity\n(b) Hinduism\n(c) Catholicism\n(d) Judaism", "Answer": "b"}, #5
               {"Question": "Who painted the Mona Lisa?", "Responses": "(a) Rafael\n(b) Michelangelo\n(c) Leonardo Da Vinci\n(d) Picasso", "Answer": "c"}, #6
               {"Question": "Which of the following is not a ship?", "Responses": "(a) Schooner\n(b) Clipper\n(c) Galleon\n(d) Barouche", "Answer": "d"}, #7
               {"Question": "What disaster hit San Francisco in 1906?", "Responses": "(a) Earthquake\n(b) Hurricane\n(c) Tsunami\n(d) Avalanche", "Answer": "a"}, #8
               {"Question": "Which of these pandemics occured in 1918 and killed 50 million?", "Responses": "(a) Bubonic Plague\n(b) Spanish Flu\n(c) Snall Pox\n(d) Polio", "Answer": "b"}, #9
          ]
          self.quiz2 = [
               {"Question": "True or False, Australia is wider than the Moon.", "Responses": "(a) True\n(b) False", "Answer": "a"}, #0
               {"Question": "True or False, Octupus has three hearts.", "Responses": "(a) True\n(b) False", "Answer": "a"}, #1
               {"Question": "True or False, Venus is the hottest planet in the solar system.", "Responses": "(a) True\n(b) False", "Answer": "a"}, #2
               {"Question": "True or False, Goldfish only have a memory of three seconds.", "Responses": "(a) True\n(b) False", "Answer": "b"}, #3
               {"Question": "True or False, K is worth four point in Scrabble.", "Responses": "(a) True\n(b) False", "Answer": "b"} #4
          ]
          self.numArray = []

     def quiz(self):
          self.numArray = random.sample(range(0, 5), 5)
          # print(self.numArray)
          score = 0
          for x in range(0, len(self.numArray)):
               print(self.numArray[x])
               print(f"{self.quiz1[self.numArray[x]]['Question']}")
               print(f"{self.quiz1[self.numArray[x]]['Responses']}")
               if self.getResponse(self.numArray[x], self.quiz1) == True:
                    print("Correct")
                    score += 1
          print(str(score) + "/" + str(5), str((score/5) * 100) + "%")

     def trueorfalse(self):
          self.numArray = random.sample(range(0, 5), 5)
          # print(self.numArray)
          score = 0
          for x in range(0, len(self.numArray)):
               print(self.numArray[x])
               print(f"{self.quiz2[self.numArray[x]]['Question']}")
               print(f"{self.quiz2[self.numArray[x]]['Responses']}")
               if self.getResponse(self.numArray[x], self.quiz2) == True:
                    print("Correct")
                    score += 1
          print(str(score) + "/" + str(5), str((score/5) * 100)  + "%")


     def getResponse(self, index, array):
          # print(array[index]['Answer'])
          choice = input("Enter Your Answer:")
          if choice == array[index]['Answer']:
               return True
          else:
               return False

     def userchoicequiz(self):
          x = int(input("How many Questions? (Input 1-10)"))
          self.numArray = random.sample(range(0, 10), x)
          # print(self.numArray)
          score = 0
          for x in range(0, len(self.numArray)):
               print(self.numArray[x])
               print(f"{self.quiz1[self.numArray[x]]['Question']}")
               print(f"{self.quiz1[self.numArray[x]]['Responses']}")
               if self.getResponse(self.numArray[x], self.quiz1) == True:
                    print("Correct")
                    score += 1
          print(str(score) + "/" + str(x+1), str((score/(x+1)) * 100) + "%")


def main():
     question = Question()
     while True:
          print("---------------------------")
          print("Main Menu:")
          print("1. Quiz")
          print("2. True or False")
          print("3. Custom Quiz")
          print("4. Exit")
          print("---------------------------")
          choice = input("Your choice: ")
          if choice.isnumeric() and 0 < int(choice) < 7:
               options = {
                    1: question.quiz,
                    2: question.trueorfalse,
                    3: question.userchoicequiz,
                    4: exit,
               }
               options[int(choice)]()
          else:
               print("The option you have selected does not exist!")

main()