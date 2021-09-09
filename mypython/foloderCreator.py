import os

class folderAuto:

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)


    def main(self):

        path = input('Enter the path you want to create the folder.\nex) C:\\folder\here \n => ')
        name = input('Enter the folder name.\nex) Unit_ \n => ')
        try:
            start_index = int(input('Enter the start index.\nex) 3 \n => '))
            end_index = int(input('Enter the end index.\nex) 7 \n => '))
        except ValueError:
            print('!ONLY INPUT THE NUMBER!')
        else:
            # _index = []
            # _index.append(start_index)
            # _index.append(end_index)
            # _index.sort
            print('Setting is done')

gimoring = folderAuto()
gimoring.main()