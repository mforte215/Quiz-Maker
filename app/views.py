from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import QuizForm
from .models import Quiz, Question, Choice, ScoreRecord
# Create your views here.
def Index(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(draft=False)
        return render(request, 'app/index.html', {'quizzes': quizzes})

def QuizDetail(request, slug):
    if request.method == 'GET':
        quiz = Quiz.objects.get(slug=slug)
        questions = Question.objects.filter(quiz=quiz)
        quizForm = QuizForm()
        return render(request, 'app/quiz-detail.html', {'quiz': quiz, 'questions': questions, 'quizForm': quizForm})
    if request.method == 'POST':
        print("PRINTING First Question and Answer")
        print(request.POST)
        quiz = Quiz.objects.get(slug=slug)
        questions = Question.objects.filter(quiz=quiz)
        question_number = 0
        correct_answers = 0
        for question in questions:
            question_number+=1
            print(f"QUESTION {question_number}")
            print(question.question_text)
            print("USER RESPONSE")
            print(request.POST[question.question_text])
            if (request.POST[question.question_text] == question.correct_answer):
                print("CORRECT!")
                correct_answers+=1
            else:
                print("WRONG!")
        test_score = (correct_answers / question_number) * 100
        request.session['test_score'] = int(test_score)
        request.session['quiz_name'] = quiz.title
        answer_output = f"YOU GOT A {int(test_score)}%"
        print(answer_output)
        return HttpResponseRedirect(reverse_lazy('score-detail'))

def ScoreDetail(request):
    if request.method == 'GET':
        score = request.session.get('test_score')
        print(f"IN THE NEW VIEW and the score is: {score}")
        return render(request, 'app/score-detail.html', {'score': score})
    if request.method == 'POST':
        score = request.session.get('test_score')
        quiz_name = request.session.get('quiz_name')
        username = request.POST['username']
        quiz = Quiz.objects.get(title=quiz_name)
        score_record = ScoreRecord(score=score, user_name=username, quiz=quiz)
        score_record.save()
        return HttpResponseRedirect(reverse('quiz-scores-detail', kwargs={'slug': quiz.slug}))


def QuizTopScores(request, slug):
    if request.method == 'GET':
        quiz = Quiz.objects.get(slug=slug)
        quiz_scores = ScoreRecord.objects.filter(quiz=quiz).order_by('-score')
        return render(request, 'app/quiz-score-details.html', {'quiz_scores': quiz_scores})

def Search(request):
    if request.method == 'GET':
        return render(request, 'app/search-detail.html', {})
    if request.method == 'POST':
        print("SEARCH VALUE")
        print(request.POST['search-value'])
        search_value = request.POST['search-value']
        quizzes = Quiz.objects.all().filter(draft=False)
        matched_quizzes = []
        for quiz in quizzes:
            if search_value in quiz.title:
                matched_quizzes.append(quiz)

        return render(request, 'app/search-detail.html', {'matched_quizzes': matched_quizzes})

def ReportProblem(request):
    if request.method == 'GET':
        return render(request, 'app/report-problem.html', {})



    