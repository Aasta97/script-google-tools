from google.cloud import storage


class Google:
    def __init__(self):
        # Instanciar cliente
        self.storage_client = storage.Client()

    def create_new_bucket(self, bucket_name):
        # O nome do bucket é global e precisa ser um nome que nunca foi utilizado
        # Criar novo bucket
        bucket = self.storage_client.create_bucket(bucket_name)

    def upload_file(self, bucket_name, source_file_name):
        # Selecionar Bucket
        bucket = self.storage_client.bucket(bucket_name)
        # Permitir disponibilizar objetos de dados, chamados blobs
        blob = bucket.blob(source_file_name)
        # Realizar upload
        blob.upload_from_filename(source_file_name)

    def list_files(self, bucket_name):
        # Listar arquivos do bucker
        blobs = self.storage_client.list_blobs(bucket_name)

        # Percorrer blobs
        for blob in blobs:
            print(blob.name)


google = Google()
# google.create_new_bucket("meunomedebucketteste")
# google.upload_file("meunomedebucketteste", "teste.txt")
# google.list_files("meunomedebucketteste")
