
import os 




def folderSearcher():
    fileArr = []    
    print(os.listdir())
    currDir = os.getcwd()
    userInput = input('do you want to check FILES, FOLDERS, or GO BACK: ')
    if(userInput == 'files'):
        typeCheck = input('which type of file do you want: ')
        for root, dirs, files in os.walk(currDir):
            for file in files: 
                if file.endswith(typeCheck):
                    filePaths = os.path.abspath(file)
                    fileArr += file
                    print(fileArr)
        #print(fileArr)

    elif(userInput == 'go back'):
        prev = os.path.normpath(currDir + os.sep + os.pardir)
        os.chdir(prev)
        return folderSearcher()

    elif(userInput == 'folders'):
        folderInput = input('which folder do you want to check: ')
        #dirPath = os.path.dirname(currDir)
        print(currDir + '/' + folderInput)
        #print(currDir)
        os.chdir(currDir + '/' + folderInput)
        #print(os.listdir())
        return folderSearcher()
    


folderSearcher()


