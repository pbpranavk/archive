from django.urls import path,re_path
from questions import views
from questions.views.questions_view import QuestionView
from questions.views.search_view import SearchView
from questions.views.update_question import UpdateQuestion
from questions.views.comments_view import Comments
from questions.views.answer_view import AnswerView
from questions.views.question_details import QuestionDetails
urlpatterns = [

    path('create_question', QuestionView.as_view(),name = 'create_question'),
    re_path(r'^$', SearchView.searchposts, name = 'searchposts') ,
    path('add_comment/', Comments.add_comment, name = 'add_comment'),
    path('like/', QuestionView.like,name= 'like'),
    path('clike/', Comments.comment_like,name= 'clike'),
    path('edit_ques',QuestionView.edit_ques, name = "edit_ques"),
    path('answer_ques', AnswerView.as_view(), name="answer_ques"),
    path('update_ques', UpdateQuestion.update_question, name= "update_ques"),
    path('dislike/', QuestionView.dislike,name= 'dislike'),
    path('cdislike/', Comments.comment_dislike,name= 'cdislike'),
    path('answer_ques/add_ans', AnswerView.add_answer_comment, name="add_answer_comment" ),
    path('<int:question_id>/', QuestionDetails.details, name='question_details')
]