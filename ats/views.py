import re

from django.shortcuts import render, redirect

from .utils import (
    extract_text_from_pdf,
    extract_text_from_docx,
    safe_search,
    extract_recommendations,
)
from .ats_model import analyze_documents


def ats_home(request):
    if request.method == "POST":
        job_description = request.POST.get("job_description")
        resume_file = request.FILES.get("resume")

        file_type = resume_file.name.split(".")[-1].lower()
        if file_type == "pdf":
            resume_text = extract_text_from_pdf(resume_file)
        elif file_type == "docx":
            resume_text = extract_text_from_docx(resume_file)
        else:
            # return error message
            resume_text = "Unsupported file type."

        analysis = analyze_documents(resume_text, job_description)

        response_text = ""
        if "candidates" in analysis:
            for candidate in analysis["candidates"]:
                if "content" in candidate and "parts" in candidate["content"]:
                    for part in candidate["content"]["parts"]:
                        response_text += part.get("text", "")

        result = response_text

        def safe_search(pattern, text, flags=0):
            match = re.search(pattern, text, flags)
            return match.group(1).strip() if match else None

        # Extract match percentage
        match_percentage_text = safe_search(r"Match Percentage:\s*(\d+)%", result)
        match_percentage = int(match_percentage_text) if match_percentage_text else None

        # Extract missing keywords
        missing_keywords_text = safe_search(
            r"Missing Keywords:\s*(.*?)(?:\n\n|Final Thoughts:)", result, re.S
        )
        missing_keywords = []
        if missing_keywords_text:
            # Only take text before first period to avoid full sentences
            if "." in missing_keywords_text:
                missing_keywords_text = missing_keywords_text.split(".")[0]
            missing_keywords = [
                kw.strip() for kw in missing_keywords_text.split(",") if kw.strip()
            ]

        # Extract final thoughts
        final_thoughts = safe_search(
            r"Final Thoughts:\s*\n*\s*(.*?)(?:\n\nRecommendations:)", result, re.S
        )

        # Extract recommendations
        recommendations = extract_recommendations(result)

        # Context
        context = {
            "match_percentage": match_percentage,
            "missing_keywords": missing_keywords,
            "final_thoughts": final_thoughts,
            "recommendations": recommendations,
        }
        request.session["ats_context"] = context

        return redirect("ats:results")
    return render(request, "home.html", {})


def ats_results(request):
    context = request.session.get("ats_context", {})
    return render(request, "ats/results.html", context)
