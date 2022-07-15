
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
        open(fileArr[0], 'r')
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
    


#folderSearcher(0)



def arrGen():
    empty = []
    controller = 7
    for x in range(controller):
        print(x)


#arrGen()



class fileSearcher:
    def __init__(self, instruct):
        self.instruct = instruct
        self.newArr = []
        self.currFolder = os.getcwd() 
        self.folder = 'folder'
        self.file = 'file'
        self.previousFolder = 'go back'

    def generateCondition(self, conditionArg, conditionVal, trigger):
        if(conditionArg == conditionVal):
            trigger()
        else: 
            return

    def openFileCondition(self, openArg, chosenFile, filePermission):
        if(openArg == os.path.split(chosenFile)[-1]):
            #print(chosenFile)
            open(chosenFile, filePermission)
            print('succcess!')
        else: 
            return


    def search(self):
        print(os.listdir())
        userInput = input('Pick One of the Options to Continue - File, Folder, Go Back: ')
        self.generateCondition(userInput, self.folder, self.folderSearch)
        self.generateCondition(userInput, self.file, self.fileSearch)
        self.generateCondition(userInput, self.previousFolder, self.goBack)

        #if(userInput == 'folder'):
         #   self.folderSearch()
        #elif(userInput == 'file'):
         #   self.fileSearch()
        #elif(userInput == 'go back'):
         #   self.goBack()

    
    def fileSearch(self):
        typeCheck = input('which type of file do you want: ')
        for root, dirs, files in os.walk(self.currFolder):
            for file in files: 
                if file.endswith(typeCheck):
                    filePaths = os.path.join(root, file)
                    #fileArr[counter] = fileArr[counter] + file
                    self.newArr = self.newArr + [filePaths]
                    #counter += 1
                    #print(counter)
                    #print(filePaths)
        print(self.newArr)
        self.fileOpener()


    def fileOpener(self):
        #print(os.path.split(self.newArr[0])[-1])
        openInput = input("Which file do you want to open? ")
        for x in self.newArr:
            #print(x)
            self.openFileCondition(openInput, x, 'r')

    
    def folderSearch(self):
        print(os.listdir())
        folderInput = input('Which folder in the directory do you want to search? ')
        #self.newArr = self.newArr + ['yoloswagmaster69420']
        #print(self.newArr)
        self.currFolder = self.currFolder + '/' + folderInput
        os.chdir(self.currFolder)
        print(self.instruct + self.currFolder)
        self.search()


        #fileArr = fileArr + [self.searcher]
        #print(fileArr)

    
    def goBack(self):
        prev = os.path.normpath(self.currFolder + os.sep + os.pardir)
        self.currFolder = prev
        os.chdir(self.currFolder)
        print('Went back to ----- ' + self.currFolder)
        self.search()



x = fileSearcher('The new directory is ----- ')
x.search()



