import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import DifficultyForm

def trainersEquation(request):
    return render(request, 'trainers_equation.html')

def trainersNumbers(request):
    return render(request, 'trainers_numbers.html')

def trainersUnequal(request):
    return render(request, 'trainers_unequal.html')

def generate_linear_equation(large_numbers=False):
    if large_numbers:
        a = random.randint(10, 100)
        b = random.randint(-100, 100)
        x = random.randint(-100, 100)
    else:
        a = random.randint(1, 10)
        b = random.randint(-10, 10)
        x = random.randint(-10, 10)

    result = a * x + b
    return f"{a} * x + {b} = {result}", x

def generate_quadratic_equation(large_numbers=False):
    if large_numbers:
        a = random.randint(10, 100)
        b = random.randint(-100, 100)
        c = random.randint(-100, 100)
        x = random.randint(-10, 10)
    else:
        a = random.randint(1, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        x = random.randint(-10, 10)

    result = a * x ** 2 + b * x + c
    return f"{a} * x^2 + {b} * x + {c} = {result}", x

def generate_equations(num_equations=10, equation_type="linear", large_numbers=False):
    equations = []
    for _ in range(num_equations):
        if equation_type == "linear":
            equation, solution = generate_linear_equation(large_numbers)
        elif equation_type == "quadratic":
            equation, solution = generate_quadratic_equation(large_numbers)
        equations.append((equation, solution))
    return equations

def select_difficulty(request):
    if request.method == 'POST':
        form = DifficultyForm(request.POST)
        if form.is_valid():
            additional_difficulties = form.cleaned_data['additional_difficulty']
            request.session['additional_difficulties'] = additional_difficulties
            return redirect('main:play_game')
    else:
        form = DifficultyForm()

    return render(request, 'card_trainer_equation1.html', {'form': form})

def play_game(request):
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        correct_solution = request.session.get('correct_solution')

        try:
            is_correct = int(user_answer) == correct_solution if user_answer is not None else False
        except ValueError:
            return JsonResponse({'error': 'Некорректный ввод'}, status=400)

        score = request.session.get('score', 0)
        correct_count = request.session.get('correct_count', 0)
        incorrect_count = request.session.get('incorrect_count', 0)
        level = request.session.get('level', 1)

        if is_correct:
            score += 100
            correct_count += 1
        else:
            incorrect_count += 1

        request.session['score'] = score
        request.session['correct_count'] = correct_count
        request.session['incorrect_count'] = incorrect_count

        equations = request.session.get('equations', [])
        if not equations:
            return JsonResponse({
                'equation': None,
                'score': score,
                'level': level,
                'correct_count': correct_count,
                'incorrect_count': incorrect_count
            })

        if equations:
            equation, solution = equations.pop(0)
            level += 1  # Увеличиваем уровень после каждого ответа
            request.session['equations'] = equations
            request.session['correct_solution'] = solution
            request.session['level'] = level
        else:
            equation, solution = None, None

        return JsonResponse({
            'equation': equation,
            'score': score,
            'level': level,
            'correct_count': correct_count,
            'incorrect_count': incorrect_count
        })

    else:
        additional_difficulties = request.session.get('additional_difficulties', [])
        large_numbers = 'large_numbers' in additional_difficulties
        equation_type = 'linear' if 'linear_equations' in additional_difficulties else 'quadratic'

        equations = generate_equations(equation_type=equation_type, large_numbers=large_numbers)
        request.session['equations'] = equations
        request.session['score'] = 0
        request.session['correct_count'] = 0
        request.session['incorrect_count'] = 0
        request.session['level'] = 1

        equation, solution = equations.pop(0)
        request.session['equations'] = equations
        request.session['correct_solution'] = solution

        return render(request, 'trainers_generator.html', {
            'equation': equation,
            'solution': solution,
            'score': 0,
            'level': 1,
            'correct_count': 0,
            'incorrect_count': 0
        })

