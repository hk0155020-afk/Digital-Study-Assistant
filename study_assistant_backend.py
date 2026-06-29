# ================================================
#   DIGITAL STUDY ASSISTANT — Python Backend
#   This is the Python OOP code behind the
#   HTML interface (study_assistant.html)
#
#   The HTML has 5 tabs — each tab has a
#   matching Python class here:
#
#   HTML Tab          →   Python Class
#   ─────────────────────────────────
#   📋 Tasks          →   TaskManager
#   ⏱  Timer          →   PomodoroTimer
#   🎓 GPA            →   GPACalculator
#   📓 Notes          →   NotesManager
#   ✨ Quotes         →   QuoteManager
#
#   OOP Concepts Used:
#   • Class & Object
#   • Constructor  (__init__)
#   • Self
#   • Encapsulation
#   • Inheritance
#   • Polymorphism
#   • Class Variable
#   • Instance Variable
#   • Composition
# ================================================

import random
from datetime import datetime


# ════════════════════════════════════════════════
#  BASE CLASS  (Parent of all 5 feature classes)
#  OOP: INHERITANCE — all classes inherit this
# ════════════════════════════════════════════════
class Feature:

    def __init__(self, name):        # OOP: Constructor + Self
        self.name = name             # OOP: Instance Variable

    def show_menu(self):             # OOP: Polymorphism (overridden in each child)
        raise NotImplementedError


# ════════════════════════════════════════════════
#  CLASS 1: TaskManager
#  HTML Tab: 📋 Tasks
#  Features: add task, delete task, mark done,
#            show stats (total / done / pending)
# ════════════════════════════════════════════════
class TaskManager(Feature):          # OOP: Inheritance

    def __init__(self):
        super().__init__("Task Manager")
        self.tasks = []              # OOP: Instance Variable — stores all tasks

    # OOP: Polymorphism — overrides Feature.show_menu()
    def show_menu(self):
        print("\n  1. Add Task")
        print("  2. Show All Tasks")
        print("  3. Mark Task as Done")
        print("  4. Delete Task")

    # OOP: Encapsulation — task data is managed inside this class
    def add_task(self, title):
        task = {
            "id":    len(self.tasks) + 1,
            "title": title,
            "done":  False,
            "date":  datetime.now().strftime("%Y-%m-%d")
        }
        self.tasks.append(task)
        print(f"\n  ✔ Task added: '{title}'")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"\n  ✔ Marked done: '{self.tasks[index]['title']}'")
        else:
            print("\n  ✖ Invalid number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"\n  ✔ Deleted: '{removed['title']}'")
        else:
            print("\n  ✖ Invalid number.")

    def show_tasks(self):
        # Stats shown at top of HTML tab
        total   = len(self.tasks)
        done    = sum(1 for t in self.tasks if t["done"])
        pending = total - done

        print(f"\n  Total: {total}  |  Done: {done}  |  Pending: {pending}")
        print("  " + "─" * 38)

        if not self.tasks:
            print("  No tasks yet.")
            return

        for i, t in enumerate(self.tasks):
            status = "☑ DONE" if t["done"] else "☐     "
            print(f"  {i}. [{status}]  {t['title']}  ({t['date']})")


# ════════════════════════════════════════════════
#  CLASS 2: PomodoroTimer
#  HTML Tab: ⏱ Timer
#  Features: 25-min study, 5-min break,
#            start / pause / reset, mode switch
# ════════════════════════════════════════════════
class PomodoroTimer(Feature):        # OOP: Inheritance

    STUDY_MINUTES = 25               # OOP: Class Variable (shared, never changes)
    BREAK_MINUTES = 5                # OOP: Class Variable

    def __init__(self):
        super().__init__("Pomodoro Timer")
        self.mode     = "study"      # OOP: Instance Variable
        self.sessions = 0            # OOP: Instance Variable — counts completed sessions

    def show_menu(self):             # OOP: Polymorphism
        print("\n  1. Start Study Session  (25 min)")
        print("  2. Start Break          (5 min)")
        print("  3. View Session Count")
        print("  4. Show Focus Tips")

    def start_study(self):
        self.mode = "study"
        print(f"\n  ⏱  STUDY SESSION STARTED")
        print(f"  Focus for {self.STUDY_MINUTES} minutes.")  # uses Class Variable
        print("  No phone. No distractions. Go!")

    def start_break(self):
        self.mode = "break"
        self.sessions += 1           # update Instance Variable
        print(f"\n  ☕  BREAK TIME  ({self.BREAK_MINUTES} minutes)")
        print(f"  Sessions completed so far: {self.sessions}")
        if self.sessions % 4 == 0:
            print("  🎉 4 sessions done! Take a long break (20-30 min).")

    def show_tips(self):
        tips = [
            "Put your phone on silent",
            "Close all unnecessary tabs",
            "Write your goal before starting",
            "Drink water before you begin",
            "Work on ONE task at a time"
        ]
        print("\n  Focus Tips:")
        for tip in tips:
            print(f"   •  {tip}")

    def show_sessions(self):
        dots = ("●" * self.sessions) + ("○" * (4 - self.sessions % 4))
        print(f"\n  Sessions completed: {self.sessions}")
        print(f"  Progress: {dots}")


# ════════════════════════════════════════════════
#  CLASS 3: GPACalculator
#  HTML Tab: 🎓 GPA
#  Features: add course with grade + credits,
#            calculate weighted GPA, show result
# ════════════════════════════════════════════════
class GPACalculator(Feature):        # OOP: Inheritance

    # OOP: Class Variable — grade scale shared by all objects
    GRADE_POINTS = {
        "A+": 4.0,  "A": 4.0,  "A-": 3.7,
        "B+": 3.3,  "B": 3.0,  "B-": 2.7,
        "C+": 2.3,  "C": 2.0,  "C-": 1.7,
        "D":  1.0,  "F": 0.0
    }

    def __init__(self):
        super().__init__("GPA Calculator")
        self.courses = []            # OOP: Instance Variable

    def show_menu(self):             # OOP: Polymorphism
        print("\n  1. Add Course")
        print("  2. Show All Courses")
        print("  3. Calculate GPA")
        print("  4. Clear All Courses")

    def add_course(self, name, grade, credits):
        grade = grade.upper()
        if grade not in self.GRADE_POINTS:  # uses Class Variable
            print(f"\n  ✖ Invalid grade '{grade}'.")
            print("     Valid: A+ A A- B+ B B- C+ C C- D F")
            return
        self.courses.append({
            "course":  name,
            "grade":   grade,
            "credits": credits,
            "points":  self.GRADE_POINTS[grade]
        })
        print(f"\n  ✔ Added: {name} | {grade} | {credits} credit(s)")

    def calculate_gpa(self):
        if not self.courses:
            print("\n  No courses added yet.")
            return

        total_weighted = sum(c["points"] * c["credits"] for c in self.courses)
        total_credits  = sum(c["credits"] for c in self.courses)
        gpa = total_weighted / total_credits

        # Same classification as shown in the HTML tab
        if   gpa >= 3.7: result = "🌟 Distinction / Dean's List"
        elif gpa >= 3.3: result = "✨ Very Good"
        elif gpa >= 3.0: result = "👍 Good Standing"
        elif gpa >= 2.7: result = "📈 Above Average"
        elif gpa >= 2.0: result = "📊 Satisfactory"
        elif gpa >= 1.0: result = "⚠️  Below Average"
        else:            result = "❌ Academic Warning"

        print(f"\n  ┌──────────────────────────┐")
        print(f"  │  GPA  :  {gpa:.2f}             │")
        print(f"  │  Result: {result}")
        print(f"  │  Credits: {total_credits} total    │")
        print(f"  └──────────────────────────┘")

    def show_courses(self):
        if not self.courses:
            print("\n  No courses yet.")
            return
        print(f"\n  {'Course':<20} {'Grade':<6} {'Credits':<8} {'Points'}")
        print("  " + "─" * 44)
        for c in self.courses:
            print(f"  {c['course']:<20} {c['grade']:<6} {c['credits']:<8} {c['points']:.1f}")

    def clear_courses(self):
        self.courses.clear()
        print("\n  ✔ All courses cleared.")


# ════════════════════════════════════════════════
#  CLASS 4: NotesManager
#  HTML Tab: 📓 Notes
#  Features: new note, save, view list,
#            read a note, delete note
# ════════════════════════════════════════════════
class NotesManager(Feature):         # OOP: Inheritance

    def __init__(self):
        super().__init__("Notes Manager")
        self.notes = {}              # OOP: Instance Variable — dict {title: content}

    def show_menu(self):             # OOP: Polymorphism
        print("\n  1. Save New Note")
        print("  2. View All Notes")
        print("  3. Read a Note")
        print("  4. Delete a Note")

    def save_note(self, title, content):
        self.notes[title] = {
            "content": content,
            "date":    datetime.now().strftime("%Y-%m-%d")
        }
        print(f"\n  ✔ Note saved: '{title}'")

    def view_notes(self):
        if not self.notes:
            print("\n  No notes saved yet.")
            return
        print("\n  Your Notes:")
        print("  " + "─" * 30)
        for i, title in enumerate(self.notes):
            date = self.notes[title]["date"]
            print(f"  {i}.  {title:<25} {date}")

    def read_note(self, title):
        if title in self.notes:
            print(f"\n  ┌─ {title} ─")
            print(f"  │  {self.notes[title]['content']}")
            print(f"  └─ Saved: {self.notes[title]['date']}")
        else:
            print(f"\n  ✖ Note '{title}' not found.")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            print(f"\n  ✔ Deleted: '{title}'")
        else:
            print(f"\n  ✖ Note '{title}' not found.")


# ════════════════════════════════════════════════
#  CLASS 5: QuoteManager
#  HTML Tab: ✨ Quotes
#  Features: show random quote, next, previous
# ════════════════════════════════════════════════
class QuoteManager(Feature):         # OOP: Inheritance

    # OOP: Class Variable — same quotes for every object
    QUOTES = [
        ("The secret of getting ahead is getting started.",          "Mark Twain"),
        ("An investment in knowledge pays the best interest.",        "Benjamin Franklin"),
        ("Genius is 1% talent and 99% hard work.",                   "Albert Einstein"),
        ("The expert in anything was once a beginner.",              "Helen Hayes"),
        ("Believe you can and you're halfway there.",                 "Theodore Roosevelt"),
        ("Education is the most powerful weapon to change the world.","Nelson Mandela"),
        ("Don't let what you cannot do stop what you can do.",        "John Wooden"),
        ("Push yourself — no one else will do it for you.",           "Unknown"),
    ]

    def __init__(self):
        super().__init__("Quotes")
        self.index = 0               # OOP: Instance Variable — tracks current quote

    def show_menu(self):             # OOP: Polymorphism
        print("\n  1. Random Quote")
        print("  2. Next Quote")
        print("  3. Previous Quote")
        print("  4. Show All Quotes")

    def _display(self, quote, author):   # private helper method
        print(f'\n  ❝ {quote} ❞')
        print(f'     — {author}')
        print(f'     [{self.index + 1} of {len(self.QUOTES)}]')

    def random_quote(self):
        self.index = random.randint(0, len(self.QUOTES) - 1)
        self._display(*self.QUOTES[self.index])

    def next_quote(self):
        self.index = (self.index + 1) % len(self.QUOTES)
        self._display(*self.QUOTES[self.index])

    def prev_quote(self):
        self.index = (self.index - 1) % len(self.QUOTES)
        self._display(*self.QUOTES[self.index])

    def show_all(self):
        print("\n  All Quotes:")
        print("  " + "─" * 50)
        for i, (q, a) in enumerate(self.QUOTES):
            print(f"  {i+1}. \"{q}\"")
            print(f"       — {a}\n")


# ════════════════════════════════════════════════
#  MAIN CLASS: StudyAssistant
#  OOP: COMPOSITION — contains all 5 feature objects
# ════════════════════════════════════════════════
class StudyAssistant:

    def __init__(self):
        # OOP: Composition — creating objects of all 5 classes
        self.task_manager  = TaskManager()
        self.timer         = PomodoroTimer()
        self.gpa_calc      = GPACalculator()
        self.notes_manager = NotesManager()
        self.quotes        = QuoteManager()

    def show_main_menu(self):
        print("\n" + "═" * 42)
        print("      📚 DIGITAL STUDY ASSISTANT")
        print("═" * 42)
        print("  1.  📋  Task Manager")
        print("  2.  ⏱   Pomodoro Timer")
        print("  3.  🎓  GPA Calculator")
        print("  4.  📓  Notes Manager")
        print("  5.  ✨  Motivational Quote")
        print("  0.      Exit")
        print("═" * 42)

    # ── Task Manager menu ──────────────────────
    def run_tasks(self):
        while True:
            self.task_manager.show_menu()  # Polymorphism in action
            print("  0. Back")
            ch = input("\n  Choice: ").strip()
            if ch == "1":
                t = input("  Task title: ").strip()
                self.task_manager.add_task(t)
            elif ch == "2":
                self.task_manager.show_tasks()
            elif ch == "3":
                self.task_manager.show_tasks()
                i = int(input("  Task number: "))
                self.task_manager.mark_done(i)
            elif ch == "4":
                self.task_manager.show_tasks()
                i = int(input("  Task number: "))
                self.task_manager.delete_task(i)
            elif ch == "0":
                break

    # ── Pomodoro Timer menu ────────────────────
    def run_timer(self):
        while True:
            self.timer.show_menu()         # Polymorphism in action
            print("  0. Back")
            ch = input("\n  Choice: ").strip()
            if   ch == "1": self.timer.start_study()
            elif ch == "2": self.timer.start_break()
            elif ch == "3": self.timer.show_sessions()
            elif ch == "4": self.timer.show_tips()
            elif ch == "0": break

    # ── GPA Calculator menu ────────────────────
    def run_gpa(self):
        while True:
            self.gpa_calc.show_menu()      # Polymorphism in action
            print("  0. Back")
            ch = input("\n  Choice: ").strip()
            if ch == "1":
                name    = input("  Course name  : ").strip()
                grade   = input("  Grade (A/B+) : ").strip()
                credits = int(input("  Credits      : "))
                self.gpa_calc.add_course(name, grade, credits)
            elif ch == "2": self.gpa_calc.show_courses()
            elif ch == "3": self.gpa_calc.calculate_gpa()
            elif ch == "4": self.gpa_calc.clear_courses()
            elif ch == "0": break

    # ── Notes Manager menu ─────────────────────
    def run_notes(self):
        while True:
            self.notes_manager.show_menu() # Polymorphism in action
            print("  0. Back")
            ch = input("\n  Choice: ").strip()
            if ch == "1":
                title   = input("  Title  : ").strip()
                content = input("  Content: ").strip()
                self.notes_manager.save_note(title, content)
            elif ch == "2": self.notes_manager.view_notes()
            elif ch == "3":
                title = input("  Note title: ").strip()
                self.notes_manager.read_note(title)
            elif ch == "4":
                title = input("  Note title: ").strip()
                self.notes_manager.delete_note(title)
            elif ch == "0": break

    # ── Quotes menu ────────────────────────────
    def run_quotes(self):
        while True:
            self.quotes.show_menu()        # Polymorphism in action
            print("  0. Back")
            ch = input("\n  Choice: ").strip()
            if   ch == "1": self.quotes.random_quote()
            elif ch == "2": self.quotes.next_quote()
            elif ch == "3": self.quotes.prev_quote()
            elif ch == "4": self.quotes.show_all()
            elif ch == "0": break

    # ── Main run loop ──────────────────────────
    def run(self):
        print("\n  Welcome to your Digital Study Assistant!")
        self.quotes.random_quote()         # show a quote on startup

        while True:
            self.show_main_menu()
            ch = input("  Choose: ").strip()

            if   ch == "1": self.run_tasks()
            elif ch == "2": self.run_timer()
            elif ch == "3": self.run_gpa()
            elif ch == "4": self.run_notes()
            elif ch == "5": self.quotes.random_quote()
            elif ch == "0":
                print("\n  Goodbye! Keep studying! 👋\n")
                break
            else:
                print("\n  ✖ Invalid choice. Try again.")


# ════════════════════════════════════════════════
#  ENTRY POINT
#  Create ONE object of StudyAssistant and run it
# ════════════════════════════════════════════════
if __name__ == "__main__":
    app = StudyAssistant()   # Object created from class
    app.run()                # Method called on object
