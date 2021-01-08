from django.shortcuts import render


def emoticon(request):
    # Page Render
    if request.path == '/en/emoticon':
        links = {
            'nav_emoji': '/en/emoji',
            'nav_convert': '/en/convert-case',
            'nav_emoticon': '/en/emoticon'}
        transl = {
            'name_c': 'CONVERT CASE',
            'dev': 'Developed with \U0001F499 by Hireki'
            }
        return render(request, 'emoticon/en_emoticon.html', {
            'links': links, 'transl': transl})
        
    elif request.path == '/pt/emoticon':
        links = {
            'nav_emoji': '/pt/emoji',
            'nav_convert': '/pt/convert-case',
            'nav_emoticon': '/pt/emoticon'
            }
        transl = {
            'name_c': 'LETRAS DIFERENTES',
            'dev':'Desenvolvido com \U0001F499 por Hireki'
            }
        return render(request, 'emoticon/pt_emoticon.html', {
            'links': links, 'transl': transl})