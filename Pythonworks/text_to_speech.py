import pyttsx3
class Filesound():
    def __init__(self):
        self.sp=pyttsx3.init()

    def soundmake(self,text):
        voices=self.sp.getProperty('voices')
        self.sp.setProperty('voice', voices[1].id) #female sound 
        self.sp.say(text)
        self.sp.runAndWait()
        self.sp.stop()

    def filecontent(self,filename):
        f=open(filename,'r')
        self.text=f.read()
        return self.text

obj=Filesound()
fl=obj.filecontent("messi22.txt")
obj.soundmake(fl)

        
        
        
        
        


