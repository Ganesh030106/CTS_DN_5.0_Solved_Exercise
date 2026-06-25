class Notifier:
    def send(self, msg): print(f"Sending: {msg}")

class NotifierDecorator(Notifier):
    def __init__(self, wrapped): self.wrapped = wrapped
    def send(self, msg): self.wrapped.send(msg)

class SMSDecorator(NotifierDecorator):
    def send(self, msg):
        super().send(msg)
        print("Also sending via SMS")


notifier = SMSDecorator(Notifier())
notifier.send("Hello!")