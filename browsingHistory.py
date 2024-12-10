class BrowserHistory:
    def __init__(self):
        self.history = []

    # add a page to history
    def add_page(self, url):
        print("Adding page to history...")
        self.history.append(url)
        print(f"'{url}' added to history.")

    # remove a page from history
    def remove_page(self, url):
        print("Removing page from history...")
        for index, value in enumerate(self.history):
            if value == url:
                self.history.pop(index)
                print(f"Page Removed: {value}")
                return
        print("Page not found in history.")

    # Show the current browsing history
    def completeHistory(self):
        print("Current browsing history: ", self.history)

    # Check if the history is empty or has something within it
    def is_empty(self):
        if len(self.history) == 0:
            print("There is no history stored.")
        else:
            print("The history is not empty! Use completeHistory() to access!")
    
history = BrowserHistory()
history.add_page("Google.com")
history.add_page("Crunchyroll.com")
history.add_page("Twitch.tv")
history.completeHistory()
history.remove_page("Twitch.tv")
history.completeHistory()
history.is_empty()