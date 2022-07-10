# --- IMPORTS ---
import subprocess
import time
# ---------------

class Pinger:
    def __init__(self, messages=False, os="WINDOWS") -> None:
        """Initializes Pinger class,\n
        Non-input Attributes:
            cmd (array): subprocess library, array of commands. Currently windows ping command.\n
            results (None): Stores ping results, initializes as None\n

        Args:
            messages (bool, optional): Show all ping results?. Defaults to False.
            os (str, optional): "WINDOWS" or "MACOS". Changes ping command. Defaults to "WINDOWS".
        """
        self.os = os

        self.cmd = ['ping', '-n', '1','8.8.8.8']

        self.results = None
        self.messages = messages
        print("Press 'Control+C' to quit! Otherwise, this will continuously run!\n .run() to run test, see README for other commands")

    # --- Getters, Setters ---
    def getCMD(self):
        return self.cmd

    def setCMD(self, cmd):
        self.cmd = cmd

    def getOS(self):
        return self.os

    def setOS(self, os):
        self.os = os
        if self.os == "WINDOWS":
            self.cmd = ['ping', '-n', '1','8.8.8.8']
        elif self.os == "MACOS":
            self.cmd = ['ping', '-c', '1', '8.8.8.8']
        else:
            print("Unsupported OS, Defaulting to WINDOWS")
            self.os = "WINDOWS"
            self.cmd = ['ping', '-n', '1','8.8.8.8']

    def getMessages(self):
        return self.messages

    def setMessages(self, messages):
        self.messages = messages
    # ------------------------

    # --- Results/Logic ---
    def getAllResults(self):
        if self.messages == True:
            print("All results: \n%s\n" % (self.results))
        return self.results

    def getBadResults(self):
        shouldLog = False

        if "bytes" not in self.results:
            _time = time.ctime()
            print("Timestamp: \n%s\nMessage: %s" % (_time, self.results))
            shouldLog = True

        if shouldLog == True:
            with open("LOGGER.txt", "a") as myfile:
                myfile.write(_time)
                myfile.write(self.results)
                myfile.write("__________________________\n")

    def logger(self): 
        try:
            self.results = ("".join(map(chr, subprocess.check_output(self.cmd, stderr=subprocess.STDOUT))))
        except subprocess.CalledProcessError as e:
            self.results = ("DOWN %s" % (time.ctime()))
            with open("LOGGER.txt", "a") as myfile:
                myfile.write(self.results)
                myfile.write("__________________________\n")
                time.sleep(1)
            self.logger()
        return self.results

    def run(self):
        try:
            while True:
                self.logger()
                self.getAllResults()
                self.getBadResults()
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    # --------------------