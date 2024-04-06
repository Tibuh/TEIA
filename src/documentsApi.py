import os

class DocumentsApi:
    @staticmethod
    def Documents_avaibles():
         local = "./pdfs"

         if os.path.isdir(local):
            directory_contents = os.listdir(local)
            
            return directory_contents
         else:
            return ""
