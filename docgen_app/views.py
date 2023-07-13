from django.shortcuts import render
from django.http import JsonResponse
import subprocess

def code_editor(request):
    if request.method == 'POST' and 'code' in request.POST:
        code = request.POST['code']

        # Execute the code using subprocess and capture the output
        process = subprocess.Popen(
            ['python', '-c', code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()

        # Return the output as a JSON response
        return JsonResponse({'output': output, 'error': error})

    return render(request, 'index.html')

def pdf_view(request):
    import convertapi

    convertapi.api_secret = 'mX7DEmp6J6EeG2Gx'
    result = convertapi.convert('pdf', { 'File': 'docgen_app/static/test.docx' })

    # save to file
    result.file.save('docgen_app/static/test.pdf')
    return render(request, 'document.html')