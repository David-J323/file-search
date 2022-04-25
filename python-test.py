
import os 



def fileSearcher():
    print(os.listdir())
    currDir = os.getcwd()
    #userInput = input('which folder do you want to check: ')

    #currDir = os.getcwd()
    #print(currDir)
    #userFind = input('What file are you looking for: ') 
    dirPath = os.path.dirname(os.path.realpath(currDir))
    print(dirPath)
    #os.chdir(dirPath)
    #print(os.listdir)
    #for root, dirs, files in os.walk(currDir):
    
    


fileSearcher()


