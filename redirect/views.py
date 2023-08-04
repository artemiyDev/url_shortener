from django.shortcuts import redirect


def go(request, pk):
    print(pk)
    return redirect("https://www.upwork.com/jobs/Scrape-website-government-forms_~01d0d731da643dcb2a?source=rss")