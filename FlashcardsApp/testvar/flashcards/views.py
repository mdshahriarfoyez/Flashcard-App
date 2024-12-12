from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import FlashcardSet, Flashcard

def list_flashcard_sets(request):
    sets = FlashcardSet.objects.all()
    return render(request, 'flashcards/list.html', {'sets': sets})

def study_flashcard_set(request, set_id):
    flashcard_set = get_object_or_404(FlashcardSet, id=set_id)
    return render(request, 'flashcards/study.html', {'flashcard_set': flashcard_set})

def create_flashcard_set(request):
    if request.method == 'POST':
        # Check daily limit logic
        if FlashcardSet.objects.filter(user=request.user, created_at__date=datetime.date.today()).count() >= 20:
            return JsonResponse({'error': 'Daily limit reached'}, status=403)

        title = request.POST['title']
        description = request.POST.get('description', '')
        flashcard_set = FlashcardSet.objects.create(user=request.user, title=title, description=description)
        return JsonResponse({'message': 'Flashcard set created', 'id': flashcard_set.id})

    return render(request, 'flashcards/create.html')
