# define and declare class Assignment
class Assignment:
    def __init__(self):
        # Initialize list  and  variable for sum of marks and score
        self.total_summative_marks = 0
        self.total_summative_scores = 0
        self.total_formative_marks = 0
        self.total_formative_scores = 0
        self.formative_assignments = []  # for list for  total formative assignments
        self.summative_assignments = []  # for list for total summative assignments
       # telling student to enter your marks
    def input_assignments(self):
        num_assignments = int(input("Enter the total number of assignments: "))
        for count in range(num_assignments):
            # asking assignment name and type
            name = input(f"Enter the name of assignment {count + 1}: ")
            type_ = input(f"Is {name} Formative or Summative? (FA/SA): ").strip().upper()

            if type_ not in ['FA', 'SA']:
                print("Invalid type. Please enter 'FA' for Formative or 'SA' for Summative.")
                continue

            try:
                mark, score = map(int, input(
                    f"Enter marks and score for {name} (e.g., 40-85): "
                ).split('-'))

                if mark < 0 or score < 0:
                    print("Marks and scores must be non-negative. Try again.")
                    continue

                # Adding totals to assignment lists
                if type_ == 'FA':  # if user type FA = formative assignment
                    self.total_formative_marks += mark
                    self.total_formative_scores += score
                    weight = 60 / (len(self.formative_assignments) + 1)
                    self.formative_assignments.append(
                        {"name": name, "mark": mark, "score": score, "weight": weight}
                    )
                elif type_ == 'SA':  # if user type SA = summative assignment
                    self.total_summative_marks += mark
                    self.total_summative_scores += score
                    weight = 40 / (len(self.summative_assignments) + 1)
                    self.summative_assignments.append(
                        {"name": name, "mark": mark, "score": score, "weight": weight}
                    )
            except ValueError:
                print("wrong input. Please enter marks and scores in the format '40-85'.")
                continue

    def calculate_summative(self):
        if self.total_summative_scores == 0:
            print("Total summative score cannot be zero.")
            return 0

        return (self.total_summative_marks * 40) / self.total_summative_scores

    def calculate_formative(self):
        if self.total_formative_scores == 0:
            print("Total formative score cannot be zero.")
            return 0

        return (self.total_formative_marks * 60) / self.total_formative_scores

    def resubmission_eligibility(self):
        return [a for a in self.formative_assignments if a["score"] < 50]

    def generate_transcript(self, order="ascending"):
        all_assignments = self.formative_assignments + self.summative_assignments
        all_assignments.sort(key=lambda x: x["score"], reverse=(order == "descending"))

        print("\nTranscript:")
        print(f"{'Assignment':<20} {'Type':<12} {'Score (%)':<10} {'Weight (%)':<10}")
        print("-" * 60)
        for a in all_assignments:
            type_ = "Formative" if a in self.formative_assignments else "Summative"
            print(f"{a['name']:<20} {type_:<12} {a['score']:<10.2f} {a['weight']:<10.2f}")


class Student:
    def __init__(self, name):
        self.name = name
        self.assignment = Assignment()

    def evaluate(self):
        print(f"\n  - Evaluation for {self.name} -")
        self.assignment.input_assignments()

        formative_total = self.assignment.calculate_formative()
        summative_total = self.assignment.calculate_summative()

        print(f"\nFormative Weighted Score: {formative_total:.2f}%")
        print(f"Summative Weighted Score: {summative_total:.2f}%")

        # condition shows if you fail or pass
        if formative_total >= 30 and summative_total >= 20:
            print("\nCongratulations! You passed the course.")
        else:
            print("\nYou failed the course.")
            if formative_total < 30:
                print("- you have to failed formative.")
            if summative_total < 20:
                print("- you have to retake module.")

        # check eligibility for resubmission on formative assignment
        eligible = self.assignment.resubmission_eligibility()
        if eligible:
            print("\nAssignments eligible for resubmission:")
            for a in eligible:
                print(f"{a['name']} - Score: {a['score']:.2f}%")
        else:
            print("\nNo assignments are eligible for resubmission.")

        # showing transcript order
        order = input("\nWould you like the transcript in ascending or descending order? ").lower()
        self.assignment.generate_transcript(order=order)


# calling function and methods in class
while True:
    name = input("\nEnter the student's name: ")
    student = Student(name)
    student.evaluate()

    repeat = input("\nDo you want to evaluate another student? (yes/no): ").lower()
    if repeat != "yes":
        break
