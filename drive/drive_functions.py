from credentials import auth
import io
import os
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

class GDrive:
    def __init__(self):
        gauth = auth.GAuth()
        self.service = gauth.authenticate()

    def upload_file(self, file, folder_id):
        file_metadata = {
            'name': file,
            'parents': [folder_id]
        }

        media = MediaFileUpload(
            file,
            mimetype='text/plain',
            resumable=True
        )

        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        return { 'message':'File uploaded to folder!' }


    def list_files_in_folder(self, folder_id):
        results = self.service.files().list(q=f"{folder_id} in parents and trashed=false").execute()

        return results.get('files', [])


    def download_files(self, file_id, filename, download_path='.'):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(download_path, filename), 'wb') 
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        downloads = []
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        return { 'message':'Download completed!' }

    def delete_file(self, file_id):
        self.service.files().delete(fileId=file_id).execute()
        return { 'message':'Deleted file!' }


if __name__ == "__main__":
    gdrive = GDrive()
    files = gdrive.list_files_in_folder("'code'")
    for file in files:
        print(file)
