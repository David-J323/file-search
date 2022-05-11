
import os 




def folderSearcher(counter):  
    fileArr = []  
    print(os.listdir())
    currDir = os.getcwd()
    counter = 0
    userInput = input('do you want to check FILES, FOLDERS, or GO BACK: ')
    if(userInput == 'files'):
        typeCheck = input('which type of file do you want: ')
        for root, dirs, files in os.walk(currDir):
            for file in files: 
                if file.endswith(typeCheck):
                    filePaths = os.path.join(root, file)
                    #fileArr[counter] = fileArr[counter] + file
                    fileArr = fileArr + [filePaths]
                    counter += 1
                    #print(counter)
                    #print(filePaths)
                    print(fileArr)
        #for x in range(counter):
            #fileArr = fileArr + ['']
            #print(fileArr)

    elif(userInput == 'go back'):
        prev = os.path.normpath(currDir + os.sep + os.pardir)
        os.chdir(prev)
        return folderSearcher(0)

    elif(userInput == 'folders'):
        folderInput = input('which folder do you want to check: ')
        #dirPath = os.path.dirname(currDir)
        print(currDir + '/' + folderInput)
        #print(currDir)
        os.chdir(currDir + '/' + folderInput)
        #print(os.listdir())
        return folderSearcher(0)
    


folderSearcher(0)



def arrGen():
    empty = []
    controller = 7
    for x in range(controller):
        print(x)


#arrGen()

