import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token=access_token

    def upolad_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)


    f= open(file_from,'rb')
    dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AhrpewlqHh79dOJ4bywfbhdzbHToDV0W9LvGduYAFZhQ7Cbvmyvo06cT9OhnnWWCsrwLlavJ_55NuAh25BJZnvh3jB2Ld6f79rwe46SXVpup0H50nZ748lErQs6x2gIENlqIAKU'
    transferData=TransferData(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = input("enter the full path to dropbox :-") #this is the full path to upload the file to,including name as you wish the file to be called once upload

    #API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved!!!!")


    main()        