import subprocess
from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm

def evaluate_code(code):
    # Test cases with input/output for evaluation
    test_cases = [
        {"input": "5\n", "expected_output": "25\n"},
        {"input": "3\n", "expected_output": "9\n"}
    ]
    
    results = []
    
    for test_case in test_cases:
        try:
            process = subprocess.Popen(
                ["python3", "-c", code],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(input=test_case["input"])
            
            if stderr:
                results.append("Error: " + stderr.strip())
            elif stdout.strip() == test_case["expected_output"].strip():
                results.append("Pass")
            else:
                results.append(f"Fail (Expected: {test_case['expected_output']}, Got: {stdout})")
        except Exception as e:
            results.append(f"Error: {str(e)}")
    
    return "\n".join(results)

def submit_code(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.result = evaluate_code(submission.code)
            submission.save()
            return redirect("submission_result", submission_id=submission.id)
    else:
        form = SubmissionForm()
    return render(request, "submissions/submit_code.html", {"form": form})

def submission_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    return render(request, "submissions/submission_result.html", {"submission": submission})

def view_submissions(request):
    submissions = Submission.objects.all().order_by("-submitted_at")
    return render(request, "submissions/view_submissions.html", {"submissions": submissions})
# submissions/views.py
from django.shortcuts import render

def home(request):
    return render(request, "submissions/home.html")

