

def basic_resume_score(text):

    score=0
    feedback=[]

    if "machine learning" in text.lower():
        score+=10
        feedback.append("Good machine learning is there")
    else:
        feedback.append("Bad, add ml in your resume")

    if "python" in text.lower():
        score+=10
        feedback.append("gooc, python in your resume")
    else:
        feedback.append("Bad, add python in your resume")

    if len(text.split()) > 300:
        score+10
        feedback.append("your resume is sufficient length")
    else:
        feedback.append("add some extra context to your resume")

    
    return score,feedback

    
