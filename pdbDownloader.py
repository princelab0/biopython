import requests

class PDBDownloader:
    def __init__(self):
        self.base_url = "https://files.rcsb.org/download/"

    def download(self, id, callback=lambda progress:0, fileName="temp.pdb"):
        url = f"{self.base_url}/{id}.pdb"

        with open(fileName, "wb") as file:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                file.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    done = int(100 * dl / total_length)
                    callback(done)
                callback(100)