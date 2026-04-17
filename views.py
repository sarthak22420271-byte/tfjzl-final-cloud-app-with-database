from django.shortcuts import render
from .models import Submission, Choice, Question

def submit(request):
    if request.method == "POST":
        submission = Submission.objects.create(user=request.user)
        choices = request.POST.getlist('choice')

        for choice_id in choices:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)

        return show_exam_result(request, submission.id)


def show_exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    choices = submission.choices.all()

    total = 0
    correct = 0

    for choice in choices:
        if choice.is_correct:
            correct += 1
        total += 1

    score = (correct / total) * 100

    return render(request, 'exam_result.html', {
        'score': score,
        'choices': choices
    })
