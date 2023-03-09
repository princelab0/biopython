from subprocess import Popen

class VoilaRunner:
    def __init__(self, nbPath, port):
        self.nbPath = nbPath
        self.port = port
        self.command = f'voila {self.nbPath} --no-browser --port={self.port}'
        self.processes = []
    
    def start(self):
        if self.processes:
            for i in self.processes:
                i.kill()
        self.processes = []

        self.processes.append(Popen(self.command.split()))

    def killExistingProcesses(self):
        if self.processes:
            for i in self.processes:
                i.kill()
        self.processes = []
        


