

#define dictionaries
allAboutSports_list = ['arizona cardinals', 'chicago red stars', 'houston rockets', 'indiana fever', 'kentucky derby',
                       'lateral pass', 'line coach', 'pair skating', 'penalty shot', 'round-off', 'taekwondo', 'technical foul', 'toronto blue jays', 'triathlete','triple play', 'washington mystics']
animal_list =['american bison', 'arctic wolf', 'atlantic cod', 'bearded dragon', 'bengal tiger', 'elephant seal', 'giant panda bear', 'ground squirrel', 'guinea pigs',
              'mountain lion', 'prairie dog', 'reptiles', 'rhinoceros', 'siberian husky', 'tyrannosaurus rex']
anatomy_list = ['ball of the foot', 'earlobe']
atSchool_list = ['calculator']
atTheBeach_list=['swimming']
bodyAndHealth_list = ['obsidian']
cars_list = ['bench seat', 'bucket seat', 'center console', 'low beams', 'thermostat', 'windshield']
dessertsAndSweets_list = ['angel food cake', 'chocolate tard', 'coconut custard', 'gingersnaps', 'pineapple cake','poached pears', 'turkish baklava']
eatAndDrink_list = ['dried fruit', 'iceburg lettuce', 'mangosteen', 'watermelon shake']
everydayLife_list = ['marathon a tv show']
everydayObjects_list = []
famousAtheletes_list = []
famousBrands_list= ['albertsons', 'applebees', 'animal planet', 'cracker barrel', 'enterprise rent-a-car', 'kleenex tissues', "lay's chips", 'lego group', 'netflix', 'rockstar energy drink', 'tupperware',]
famousPeople_list = ['dolly parton', 'hippocrates', 'jim morrison', 'kendrick lamar', 'louis armstrong', 'robert frost', 'steve jobs', 'taylor swift']
famousThings_list=['the liberty bell']
famousQuotes_list = []
fictionalCharacters_list = ['godzilla', 'hello kitty', 'mighty mouse', 'popeye the sailor man', 'powerpuff girls']
figuresOfSpeech_list = ['fish out of water', 'go out on a limb', 'heartthrob', 'out of the blue', 'peace of mind', 'run like the wind']
gemsRocksCrystals_list = ['freshwater pearl']
greatVocabWords_list = ['assimilate', 'corroborate']
halloween_list = ['cauldron' ,'poltergeist', 'pumpkins']
history_list = ['ancient sparta', 'alexander hamilton', 'british empire' , 'baroque period', 'chernobyl disaster', "ford's theater", 'house of windsor', 'lewis and clark', 'martin luthor king jr.', 'mayan civilization', 'norman conquest']
inTheKitchen_list = ['matcha green tea', 'outdoor grill', 'pitcher', 'propane grill',  'salt & pepper shakers', 'spearmint']
movies_list = ['casino royale', 'the babysitters club', 'the last unicorn']
musicSong_list = ['born this way', 'clarinet', 'rapping', 'thrift song']
mythsAndLegends_list = ['manticore']
nature_list = ['avalanche', 'coniferous forest', 'flowering', 'gardener', 'grapevine', 'rainforest', 'sediments', 'timberland']
noRepeatingLetters_list = ['charming', 'dynamite' , 'houseplant', 'inspector', 'troublemaking']
nurseryRhymes_list = ['little miss muffet']
occupations_list = ['bodyguard','fitness trainer', 'ecologist', 'opera singer', 'park ranger', 'podiatrist','real estate agent']
officialCrayonColors_list = []
oldFashionedThings_list = ['bed & breakfast', 'home phone', 'rotary phone']
opposites_list = ['absent & present', 'body & soul', 'float & sink', 'messy & neat', 'whisper & scream']
outerSpace_list = ['gamma rays', 'space shuttle', 'jupiter']
oxymorons_list = []
places_list = ['amazon warehouse', 'arlington cemetary', 'caucasus mountains', 'chiropractic clinic', 'community center', 'coney island', 'connecticut', 'dance hall', 'daycare center', 'department store', 'des moines','district court',
               "doctor's office", 'flower shop', 'french quarter', 'georgia', 'history museum', "knott's berry farm", 'lake ontario' 'library of congress', 'madagascar', 'montreal', 'movie theater',
               'ranger station', 'santa monica pier', 'solar power plant', 'stonehenge', 'st. petersburg', 'trinidad and tobago', 'wedding hall']
phrases_list = ['a bunch of fives', 'better half', 'fish out of water', 'in spades', 'grain of salt', 'memory lane', 'plain and simple', 'season primiere']
rhymeTime_list = ['the real deal']
science_list = []
specialDays_list = ['earth day', 'national nurses day', 'world chocolate day']
starsOfStageAndScreen_list = ['benedict cumberbatch', 'brad pitt', 'evangeline lily', 'gwyneth paltrow', 'john david washington', ]
toysAndGames_list = ['hula hoop relay', 'horseshoes', 'mastermind', 'stratego']
transportation_list = ['fireboat', 'wheelbarrow', 'tractor-trailer']
tvShows_list = ['anne with an e', 'looney tunes', 'phineas and ferb', 'sherlock']



#define class
class Array:
    def __init__(self, name, num, theme):
        self.name = name
        self.num = num
        self.theme = theme

    def func(self):
        print('you chose number ' + self.num + ': ' + self.name)
        theme_loop = False
        lengthCheck(self.theme)
        spaceCheck(self.theme)
        letterCheck(self.theme)

    
        if(len(self.theme) < 1):
            print('you eliminated every choice. Try again later.')

        else:
            print('final array:')
            for x in self.theme:
                print(x)



#define main module
def main():
    #initialize input while loop for theme
    theme_loop = True
    print('Welcome to the Coolmath Hangman Solver')

    #theme options
    print('Available Themes: ')
    print(' 1: All About Sports' + '\n' + ' 2: Animals'
          + '\n' + ' 3: Anatomy' + '\n' + ' 4: At School'
          + '\n' + ' 5: At the Beach' + '\n' + ' 6: Body and Health'
          + '\n' + ' 7: Cars' + '\n' + ' 8: Desserts & Sweets'
          + '\n' + ' 9: Eat & Drink' + '\n' + ' 10: Everyday Life'
          + '\n' + ' 11: Everyday Objects' + '\n' + ' 12: Famous Athletes'
          + '\n' + ' 13: Famous Brands' + '\n' + ' 14: Famous People'
          + '\n' + ' 15: Famous Things' + '\n' + ' 16: Famous Quotes'
          + '\n' + ' 17: Fictional Characters' + '\n' + ' 18: Figures of Speech'
          + '\n' + ' 19: Gems Rocks and Crystals' +'\n' + ' 20: Great Vocab Words'
          + '\n' + ' 21: Halloween' + '\n' + ' 22: History'
          + '\n' + ' 23: In the Kitchen' + '\n' + ' 24: Movies'
          + '\n' + ' 25: Music & Song' + '\n' + ' 26: Myths and Legends'
          + '\n' + ' 27: Nature' + '\n' + ' 28: No Repeating Letters'
          + '\n' + ' 29: Nursery Ryhmes' + '\n' + ' 30: Occupations'
          + '\n' + ' 31: Official Crayon Colors' + '\n' + ' 32: Old Fashioned Things'
          + '\n' + ' 33: Opposites' + '\n' + ' 34: Outer Space'
          + '\n' + ' 35: Places' + '\n' + ' 36: Phrases'
          + '\n' + ' 37: Rhyme Time' + '\n' + ' 38: Science'
          + '\n' + ' 39: Special Days' + '\n' +  ' 40: Stars of Stage & Screen' 
          + '\n' + ' 41: Toys & Games' + '\n' +  ' 42: Transportation'
          + '\n' + ' 43: TV Shows'
          )

    #user theme input
    while theme_loop == True:
        choice = str(input('Please Choose your theme(in numbers): '))

        if choice == '1':
            theme = Array("All About Sports", "1", allAboutSports_list)
            theme.func()

        if choice == '2':
            theme = Array("Animals", "2", animal_list)
            theme.func()

        if choice == '3':
            theme = Array("Anatomy", "3", anatomy_list)
            theme.func()

        if choice == '4':
            theme = Array("At School", "4", atSchool_list)
            theme.func()

        if choice == '5':
            theme = Array("At the Beach", "5", atTheBeach_list)
            theme.func()

        if choice == '6':
            theme = Array("Body and Health", "6", bodyAndHealth_list)
            theme.func()

        if choice == '7':
            theme = Array("Cars", "7", cars_list)
            theme.func()

        if choice == '8':
            theme = Array("Desserts & Sweets", "8", dessertsAndSweets_list)
            theme.func()

        if choice == '9':
            theme = Array("Eat & Drink", "9", eatAndDrink_list )
            theme.func()

        if choice == '10':
            theme = Array("Everyday Life", "10", everydayLife_list)
            theme.func()

        if choice == '11':
            theme = Array("Everyday Objects", "11", everydayObjects_list)
            theme.func()

        if choice == '12':
            theme = Array("Famous Athletes", "12", famousAthletes_list)
            theme.func()

        if choice == '13':
            theme = Array("Famous Brands", "13", famousBrands_list)
            theme.func()

        if choice == '14':
            theme = Array("Famous People", "14", famousPeople_list)
            theme.func()

        if choice == '15':
            theme = Array("Famous Things", "15", famousThings_list)
            theme.func()

        if choice == '16':
            theme = Array("Famous Quotes", "16", famousQuotes_list)
            theme.func() 

        if choice == '17':
            theme = Array("Fictional Characters", "17", fictionalCharacters_list)
            theme.func() 

        if choice == '18':
            theme = Array("Figures of Speech ", "18", figuresOfSpeech_list)
            theme.func()

        if choice == '19':
            theme = Array("Gems Rocks & Crystals", "19", gemsRocksCrystals_list)
            theme.func()

        if choice == '20':
            theme = Array("Great Vocab Words", "20", greatVocabWords_list)
            theme.func() 
        
        if choice == '21':
            theme = Array("Halloween", "21", halloween_list)
            theme.func()

        if choice == '22':
            theme = Array("History", "22", history_list)
            theme.func()

        if choice == '23':
            theme = Array("In The Kitchen", "23", inTheKitchen_list)
            theme.func()

        if choice == '24':
            theme = Array("Movies", "24", movies_list)
            theme.func()

        if choice == '25':
            theme = Array("Music & Song", "25", musicSong_list)
            theme.func()

        if choice == '26':
            theme = Array("Myths & Legends", "26", mythsAndLegends_list)
            theme.func() 

        if choice == '27':
            theme = Array("Nature", "27", nature_list)
            theme.func() 

        if choice == '28':
            theme = Array("No Repeating Letters", "28", noRepeatingLetters_list)
            theme.func()

        if choice == '29':
            theme = Array("Nursery Rhymes", "29", nurseryRhymes_list)
            theme.func()

        if choice == '30':
            theme = Array("Occupations", "30", occupations_list)
            theme.func()

        if choice == '31':
            theme = Array("Official Crayon Colors", "31", officialCrayonColors_list)
            theme.func()

        if choice == '32':
            theme = Array("Old Fasioned Things", "32", oldFashionedThings_list)
            theme.func()

        if choice == '33':
            theme = Array("Opposites", "33", opposites_list)
            theme.func()

        if choice == '34':
            theme = Array("Outer Space", "34", outerSpace_list)
            theme.func()

        if choice == '35':
            theme = Array("Places", "35", places_list)
            theme.func()

        if choice == '36':
            theme = Array("Phrases", "36", phrases_list)
            theme.func()

        if choice == '37':
            theme = Array("Rhyme Time", "36", rhymeTime_list)
            theme.func()

        if choice == '38':
            theme = Array("Science", "38", science_list)
            theme.func() 

        if choice == '39':
            theme = Array("Special Days", "39", specialDays_list)
            theme.func()

        if choice == '40':
            theme = Array("Stars of Stage and Screen", "40", starsOfStageAndScreen_list)
            theme.func()

        if choice == '41':
            theme = Array("Toys & Games", "41", toysAndGames_list )
            theme.func()

        if choice == '42':
            theme = Array("Transportation", "42", transportation_list)
            theme.func()

        if choice == '43':
            theme = Array("TV Shows", "43", tvShows_list)
            theme.func()

        else:
            print("bro that ain't a working number")

        

        theme_loop = False

            
def lengthCheck(arr):
    #initalize input while loop for word length and counter
    length_loop = True
    i = 0
    
    #user length input
    while length_loop == True:
        try:
            length = int(input('how long is your word/how many dashes are in your word(including spaces and special characters)? '))
        except ValueError:
            print("bruh choose a number that ain't a number")
        else:
            #if successful, continue with length check
            while i < len(arr):
                wordLength = len(arr[i])

                #print every correct length word
                if(wordLength == length):
                    print(arr[i])
                    i = i + 1
                else:
                    arr.remove(arr[i])
                      
            break
        
def spaceCheck(arr):
    #initialize input while loop for number of spaces
    space_loop = True
    i = 0
    space_count = 0

    #user space input
    while space_loop == True:
        try:
            correct_space_count = int(input('how many spaces are in your word? '))
        except ValueError:
            print("cmon man that's not a number")

        else:
            #if successful, continue with space check
            while i < len(arr):
                
                 #while loop to check each letter in the index
                 for letter in arr[i]:
                     #if statement to add counter for each word
                     if letter == " ":
                         space_count = space_count + 1
                    
                 #at the end of the word loop, if the count matches, print the word. Else, remove the word from the array
                 if space_count == correct_space_count:
                     print(arr[i])
                     i = i + 1
                 else:
                    #NOTE: ONLY THE CORRECRT WORDS SHOULD INCREMENT i, AS THE REMOVED WORDS AUTOMATICALLY MOVE UP THE AWAY
                    arr.remove(arr[i])

                 #initalize space count after each loop
                 space_count = 0
                 
            space_loop = False
    
def letterCheck(arr):
    #initialize input while loop for specific letter, how many letters and counter
    letter_loop = True
    #i = 0
    repeatLetters = 0

    while letter_loop == True:
        i = 0
        continue_loop = True
         
        try:
            letter = str(input('what letter or special character is in your word? '))
        except:
            print('error occured during character check')

        #now check for number of specific letter
        else:
            if len(letter) != 1:
                print('please put in one letter')

            #if there is no error, then the length has to be one. If it is false, then the loop will occur 
            else:
                
                try:
                    nLetters = int(input('how many of the letter/character ' + letter + ' is in your word? '))

                except ValueError:
                    print("bruh choose a number that ain't a number")

                #if successful, loop to check occurs    
                else:
                    while i < len(arr):
                        #while loop to check every letter in the index
                        for x in arr[i]:
                            if x.lower() == letter.lower():
                                repeatLetters = repeatLetters + 1

                        #at the end of the word loop, if the count matches, print the word. Else, remove the word from the array
                        if repeatLetters == nLetters:
                            print(arr[i])
                            i = i + 1

                        else:
                            arr.remove(arr[i])

                        #initliazlize repeat letters
                        repeatLetters = 0
                        

                if len(arr) < 2:
                    print('character check finished, final answer')
                    continue_loop = False
                    letter_loop = False
                

                while continue_loop == True:
                    #if statement to ask whether or not to continue
                    keepGoing = str(input('continue filtering?(y/n)'))
                    if keepGoing.lower() != 'y' and keepGoing.lower() != 'n':
                        print('oh my god its y or n just choose one of that')
                    else:
                        if keepGoing.lower() == 'y':
                            continue_loop = False

                        if keepGoing.lower() == 'n':
                            continue_loop = False
                            letter_loop = False

            
    
    
    
#run main module
main()


