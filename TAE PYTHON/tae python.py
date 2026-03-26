class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(f"✅ Visited: {self.current_page}")

    def back(self):
        if not self.back_stack:
            print("❌ No page to go back")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"⬅ Back to: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("❌ No page to go forward")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"➡ Forward to: {self.current_page}")

    def show_current(self):
        if self.current_page:
            print(f"🌐 Current Page: {self.current_page}")
        else:
            print("❌ No page opened")

    def show_history(self):
        print("\n📜 Back History:", self.back_stack)
        print("📜 Forward History:", self.forward_stack)


# Menu-driven program
def main():
    browser = Browser()

    while True:
        print("\n===== Browser Navigation Menu =====")
        print("1. Visit New Page")
        print("2. Go Back")
        print("3. Go Forward")
        print("4. Show Current Page")
        print("5. Show History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter URL: ")
            browser.visit(url)

        elif choice == '2':
            browser.back()

        elif choice == '3':
            browser.forward()

        elif choice == '4':
            browser.show_current()

        elif choice == '5':
            browser.show_history()

        elif choice == '6':
            print("👋 Exiting Browser Simulator...")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# Run program
main()