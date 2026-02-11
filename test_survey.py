import unittest

from Survey import AnonymouSurvey

class TestAnonymyousSurvey(unittest.TestCase):

    def setUp(self):
        question = 'What linguage did you first learn to speak?'
        self.my_survey  = AnonymouSurvey(question)
        self.responses = ['Português', 'English', 'Espanhol']

    def teste_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
