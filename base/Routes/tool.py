from django.shortcuts import render
from googletrans import Translator, LANGUAGES

# def translate(request):
#         text = request.POST['text']
#         src_lang = request.POST['src_lang']
#         dest_lang = request.POST['dest_lang']

#         translator = Translator()
#         translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text

#         context = {
#             'text': text,
#             'src_lang': src_lang,
#             'dest_lang': dest_lang,
#             'translated_text': translated_text,
#             'LANGUAGES':LANGUAGES
#         }

#         return render(request, 'tools/translate.html', context)
def translate_(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        source_lang = request.POST.get('source_lang')
        target_lang = request.POST.get('target_lang')
        translator = Translator()
        translation = translator.translate(text, src=source_lang, dest=target_lang)

        context = {
            'text': text,
            'src_lang': source_lang,
            'dest_lang': target_lang,
            'translated_text': translation,
            'LANGUAGES':LANGUAGES
        }
        return render(request, 'tools/translate.html', {'translation': context})
    else:
        return render(request, 'tools/translate.html')
