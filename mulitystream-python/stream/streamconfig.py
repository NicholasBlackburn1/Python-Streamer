
"""

this file is for handling the information for like twithc and utube stream from obs uwu
"""


import ffmpeg
from utils import consoleLog as log 

class streamconfig(object):

    _streamname : str
    _streamdesc :str
    _streamURL : str
    _streamKey : str

    # intis the stuff
    def __init__(self,streamname : str, desc : str, inputUrl:str, streamurl:str, streamKey: str):
        self.setStreamName(streamname)
        self.setStreamdiscription(desc)
        # url stuff
        self.setinputurl(inputUrl)
        self.setStreamurl(streamurl)
        self.setStreamKey(streamKey)



    # this sets the name of the stream
    def setStreamName(self,name :str):

        if(name is None or ""):
            log.Error("Not allowed stream name to be empty")

        if name is name.isnumeric():
            log.Warning("is allowed stream name to be numbers ")
            self._streamname = name

        self._streamname = name


      # this sets the name of the stream
    def setStreamdiscription(self,desc :str):

        if(desc is None or ""):
            log.Error("Not allowed stream desc to be empty")

        if desc is desc.isnumeric():
            log.Warning("is allowed stream desc to be numbers ")
            self._streamdesc = desc

        self._streamdesc = desc

      # this sets the url of the stream
    def setinputurl(self,url :str):

        if(url is None or ""):
            log.Error("Not allowed stream desc to be empty")
            Exception("cannot have a null Stream url")

        self._streamdesc = url


      # this sets the url of the stream
    def setStreamurl(self,url :str):

        if(url is None or ""):
            log.Error("Not allowed stream desc to be empty")
            Exception("cannot have a null Stream url")

        self._streamdesc = url


    # this sets the key of the stream
    def setStreamKey(self,key :str):

        if(key is None or ""):
            log.Error("Not allowed stream name to be empty")

        self._streamKey = key
        
    
