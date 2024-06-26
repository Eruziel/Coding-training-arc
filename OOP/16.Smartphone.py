class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False
        self.apps_count = 0

    def power(self):
        if self.is_on:
            self.is_on = False
        elif not self.is_on:
            self.is_on = True

    def install(self, app, app_memory):
        if self.memory - app_memory >= 0:
            if self.is_on:
                self.memory -= app_memory
                self.apps_count += 1
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {self.apps_count}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

