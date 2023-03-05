import gtts
from googletrans import Translator 
try:
    import pywhatkit as kit
except:
    print("pyWhatKit not import")
import requests
from bs4 import BeautifulSoup
from bing_image_downloader import downloader

class kit:
    
    def transe(self, Text : str, TextLang : str, cvtTo : str ):
        try :
            translator = Translator()
            output : str = translator.translate(Text, src = TextLang, dest = cvtTo)
            return output
        except : 
            return "404-error"

    def dec(self, Text : str ,To_lang : str):
        try :
            translator : Translator = Translator(to_lang = To_lang)
            translation : str = translator.translate(Text)
            return translation
        except :
            return "404-Error try again"

    def textTOVoice(self, Text : str, langu : str, FileName : str, slow : bool = False):
        print("run")
        try :
            audio_file = gtts.gTTS(text = Text, lang=langu, slow=slow)
            audio_file.save(FileName)
        except :
            return "File not process...!"
    
    def TextToHand(self, Text : str , save : str ):
        print("work")
        try : 
            kit.text_to_handwriting(Text, save_to = save)
        except:
            return "File not process...!" #image To text is also must
    
    def scrping(self, Text, paraLen):
        
        def url(query): # this function generateing a links
            links : list = []
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
            # to search
            for j in search(query, num_results=10):
                    links.append(j)
           
            return links

        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text
        link : list = url(Text) #total links

        
        output : list = []
        data : str = "" 
        for i in range(paraLen):
            htmldata = getdata(link[i])
            soup = BeautifulSoup(htmldata, 'html.parser')
            data : str = ''
            for data in soup.find_all("p"):
                output.append(data.get_text())
        return output
    

    def KeyWordToPara(self, Keywords, lenPerPages): #it's also use (SA writing,letters)
        paragraph = self.scrping(Keywords,lenPerPages)
        return paragraph

    def KeyWordToAudio(self, Keywords, lenPerPages, filename):
        print("Collecting detials...")
        paragraph = self.KeyWordToPara(Keywords,lenPerPages)
        string = ""
        for i in range(8):
            string = string + str(paragraph[i])
        print(string)
        print()
        print("Audio converting....")
        self.textTOVoice(string,"en",filename)

    def KeyWordToimage(self, Keyword, limit, dir_name):
        arr = Keyword.split(",")
        for i in range(len(arr)):
            downloader.download(arr[i], limit=limit,  output_dir=dir_name, 
            adult_filter_off=True, force_replace=False, timeout=60)


a=kit()

print(a.transe('hello','en','ta'))

# print(a.scrping("c++",6))
#print(a.KeyWordToAudio("iron man",2,"iron.mp3"))
# print(a.KeyWordToimage("c++",4,"/home/nagipragalathan/Desktop/StudyKit/static/cources"))