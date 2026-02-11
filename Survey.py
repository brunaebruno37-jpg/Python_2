

class AnonymouSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('Survey results: ')
        for response in self.responses:
            print('- '+ response)

question = 'What language did you first learn to speak?'

my_survey = AnonymouSurvey(question)

print(f'Enter "q" at any time to quit.')

while True:
    response = input(' Linguage:')
    if response == 'q':
        break
    my_survey.store_responses(response) 

print('Thank you to everyone who participated in the survey!')

my_survey.show_results()