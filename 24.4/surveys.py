class Question:
    def __init__(self, text, choices=None, allow_text=False):
        if not choices:
            choices = ["Yes", "No"]
        self.text = text
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions


customer_survey = Survey(
    "Customer Feedback Survey",
    "Please provide your feedback by answering the following questions.",
    [
        Question("Have you previously visited our store?"),
        Question("Did you shop with someone else today?"),
        Question("On average, what is your monthly spending on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to visit our store again?"),
    ])

personality_test = Survey(
    "Personality Assessment",
    "Discover more about your personality with our quiz!",
    [
        Question("Do you ever daydream about coding?"),
        Question("Do you have coding-related nightmares?"),
        Question("Which animal do you prefer: porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("In your opinion, which function name is the worst and why?",
                 ["do_something()", "execute_task()", "wtf()"],
                 allow_text=True),
    ]
)

survey_collection = {
    "customer_feedback": customer_survey,
    "personality_assessment": personality_test,
}
