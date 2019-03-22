"""Initialize flask restful api."""
from flask_restful import Api
from content_creation import app
from . import question, assessment, theme, my_content, get_questions, topic

API = Api(app)

API.add_resource(question.Question, question.QUESTION_API)
API.add_resource(assessment.Assessment, assessment.ASSESSMENT_API)
API.add_resource(my_content.MyContent, my_content.MY_CONTENT_API)
API.add_resource(theme.Theme, theme.THEME_API)
API.add_resource(get_questions.GetQuestions, get_questions.GET_QUESTIONS_API)
API.add_resource(topic.Topic, topic.TOPIC_API)
