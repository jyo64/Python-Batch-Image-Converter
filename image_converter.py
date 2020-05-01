from PIL import Image
import os
cwd = os.getcwd()
cwdl = len(cwd)

#Make save path
def savepath():
    global saveto
    target = input("Enter destination folder name :")
    saveto = os.path.join(os.getcwd(),target)
    if(os.path.isdir(saveto) == False):
        os.makedirs(saveto)
    else :
        print(target," folder already exists , please provide another name ...")
        savepath()
#saveto = os.path.join(os.getcwd(),'TRIAL')

        
#Function for converting image
def convert(file):
    image = Image.open(file)
    print('Converting:',file)    
    image.save(path(file))


#Function for creating new save location and new image format name
def path(file):
    #print('Input File:',file)
    global saveto
    p = file[cwdl+1:]
    #print('P slice:',p)
    filename = os.path.basename(file)
    #print('Filename:',filename)
    filename = filename.replace(source_format,target_format)
    #print('Dirname Gen:',os.path.dirname(p))
    newpath = os.path.join(saveto,os.path.dirname(p))
    #print('newpath:',newpath)
    if(os.path.isdir(newpath) == False):
        os.mkdir(newpath)    
    newpath = os.path.join(newpath,filename)
    #print('Newpath with filename:',newpath)
    return newpath



def main():
    global source_format
    for dirpath, dirnames, filenames in os.walk(cwd):
        #print('dirpath:',dirpath)
        #print('dirnames:',dirnames)
        for file in filenames:
            ext = (os.path.splitext(file)[-1]).lower()
            if(ext == source_format):
                p = (os.path.join(dirpath,file))
                #print(p)
                convert(p)

source_format = ('.' + input("Enter source format (eg: png) :")).lower()
target_format = ('.' + input("Enter target format (eg: jpg) :")).lower()
#source_format = '.png'
#target_format =  '.jpg'
savepath()
main()

    



