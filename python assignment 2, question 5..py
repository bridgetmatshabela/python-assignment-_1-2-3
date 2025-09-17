from abc import ABC, abstractmethod

#Define the Abstract Base Class (ABC) FileHandler
class FileHandler(ABC):
    def _init_(self, filepath):
         self.filepath = filepath

    @abstractmethod
    def read(self):

       pass

@abstractmethod
def write(self,data):
    """
    
    :param self: 
    :param data: 
    :return: 
    """"""
      pass

  #Concrete class for handling text files
class TextFileHandler(FileHandler):

    def read(self):
try:
        with open(self,filepath,'r',encoding='utf-8')as f:
            return f.read()
            
    except FileNotFoundError:
       return Nonee # Or raise a more specific exception

    def write(self,data):
         with open(self.file[path,'w'encoding ='utf-8') as f:
       f.write(data)

#Concrete class for handling binary files
   class BinaryFileHandler(FileHandler):
   
    def read(self):
    
    try:
        with open(self.filepath,'rb') as file:
            return f.read()
except FileNotFoundError:
    return None Or raise a more specific exception.

    def write(self,data):
    
        if not is instance(data,bytes):
            raise TypeError("BinaryFileHandler expects bytes data")
        with open(self.filepath,'wb') as f:
            f.write(data)

 #Example
 if_name_=="_main_" :
#Text File Handling
text_handler = TextFileHandler("example.text")
text_handler.write("Hello, this is a text file.\nAnother line of text.")








