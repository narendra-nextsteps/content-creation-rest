"""Initialize flask restful api."""
from flask_restful import Api
from content_creation import app
from . import question, assessment, theme, my_content, get_questions, topic, \
    get_assessment_details, get_topic_details, signup, login

API = Api(app)

API.add_resource(question.Question, question.QUESTION_API)
API.add_resource(assessment.Assessment, assessment.ASSESSMENT_API)
API.add_resource(my_content.MyContent, my_content.MY_CONTENT_API)
API.add_resource(theme.Theme, theme.THEME_API)
API.add_resource(get_questions.GetQuestions, get_questions.GET_QUESTIONS_API)
API.add_resource(topic.Topic, topic.TOPIC_API)
API.add_resource(get_assessment_details.GetAssessments,
                 get_assessment_details.GET_ASSESSMENT_DETAILS_API)
API.add_resource(get_topic_details.GetTopics,
                 get_topic_details.GET_TOPIC_DETAILS_API)
API.add_resource(signup.SignUp, signup.SIGN_UP_API)
API.add_resource(login.Login, login.LOGIN_API)
