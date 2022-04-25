
import os 



def folderSearcher():
    print(os.listdir())
    currDir = os.getcwd()
    userInput = input('do you want to check files or folders: ')
    if(userInput == 'files'):
        typeCheck = input('which type of file do you want: ')
        for root, dirs, files in os.walk(currDir):
            for file in files: 
                if file.endswith(typeCheck):
                    print(root)
    else:
        folderInput = input('which folder do you want to check: ')
        #dirPath = os.path.dirname(currDir)
        print(currDir + '/' + folderInput)
        #print(currDir)
        os.chdir(currDir + '/' + folderInput)
        #print(os.listdir())
        return folderSearcher()
    
    
    
    


folderSearcher()


