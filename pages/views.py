from django.shortcuts import render
import re
from pages.forms import InputForms


def home(request):
    return render(request, 'pages/home.html')


def letras_diferentes(request):
    # Form 
    form = InputForms(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.d = form.cleaned_data['origin']

    # Buttons
    if(request.POST.get('submit')):
        if (request.POST.get('submit')) == 'btn-a':
            form.d_new = ''
            for c in form.d:
                if c in fraktur:
                    c = fraktur[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-b':
            form.d_new = ''
            for c in form.d:
                if c in fraktur_b:
                    c = fraktur_b[c]
                form.d_new += c
        
        elif (request.POST.get('submit')) == 'btn-c':
            form.d_new = ''
            for c in form.d:
                if c in monospace:
                    c = monospace[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-d':
            form.d_new = ''
            for c in form.d:
                if c in double_struck:
                    c = double_struck[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-e':
            form.d_new = ''
            for c in form.d:
                if c in script:
                    c = script[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-f':
            form.d_new = ''
            for c in form.d:
                if c in script_b:
                    c = script_b[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-g':
            form.d_new = ''
            for c in form.d:
                c = c.upper()
                if c in circled_n:
                    c = circled_n[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-h':
            form.d_new = ''
            for c in form.d:
                if c in circled:
                    c = circled[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-i':
            form.d_new = ''
            for c in form.d:
                c = c.lower()
                if c in squared:
                    c = squared[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-j':
            form.d_new = ''
            for c in form.d:
                c = c.lower()
                if c in squared_n:
                    c = squared_n[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-k':
            form.d_new = ''
            for c in form.d:
                if c in serif_b:
                    c = serif_b[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-l':
            form.d_new = ''
            for c in form.d:
                if c in serif_i:
                    c = serif_i[c]
                form.d_new += c
        
        elif (request.POST.get('submit')) == 'btn-m':
            form.d_new = ''
            for c in form.d:
                if c in serif_ib:
                    c = serif_ib[c]
                form.d_new += c

        elif (request.POST.get('submit')) == 'btn-n':
            form.d_new = ''
            for c in form.d:
                if c in serif_ib:
                    c = serif_ib[c]
                form.d_new += c

    return render(request, 'pages/letrasDiferentes.html', context)


# template to squared, negative squared regional indicator

serif_ib = {
    'A': '\U0001D468',
    'B': '\U0001D469',
    'C': '\U0001D46A',
    'D': '\U0001D46B',
    'E': '\U0001D46C',
    'F': '\U0001D46D',
    'G': '\U0001D46E',
    'H': '\U0001D46F',
    'I': '\U0001D470',
    'J': '\U0001D471',
    'K': '\U0001D472',
    'L': '\U0001D473',
    'M': '\U0001D474',
    'N': '\U0001D475',
    'O': '\U0001D476',
    'P': '\U0001D477',
    'Q': '\U0001D478',
    'R': '\U0001D479',
    'S': '\U0001D47A',
    'T': '\U0001D47B',
    'U': '\U0001D47C',
    'V': '\U0001D47D',
    'W': '\U0001D47E',
    'X': '\U0001D47F',
    'Y': '\U0001D480',
    'Z': '\U0001D481',
    'a': '\U0001D482',
    'b': '\U0001D483',
    'c': '\U0001D484',
    'd': '\U0001D485',
    'e': '\U0001D486',
    'f': '\U0001D487',
    'g': '\U0001D488',
    'h': '\U0001D489',
    'i': '\U0001D48A',
    'j': '\U0001D48B',
    'k': '\U0001D48C',
    'l': '\U0001D48D',
    'm': '\U0001D48E',
    'n': '\U0001D48F',
    'o': '\U0001D490',
    'p': '\U0001D491',
    'q': '\U0001D492',
    'r': '\U0001D493',
    's': '\U0001D494',
    't': '\U0001D495',
    'u': '\U0001D496',
    'v': '\U0001D497',
    'w': '\U0001D498',
    'x': '\U0001D499',
    'y': '\U0001D49A',
    'z': '\U0001D49B',
}

# H problem
serif_i = {
    'A': '\U0001D434',
    'B': '\U0001D435',
    'C': '\U0001D436',
    'D': '\U0001D437',
    'E': '\U0001D438',
    'F': '\U0001D439',
    'G': '\U0001D43A',
    'H': '\U0001D43B',
    'I': '\U0001D43C',
    'J': '\U0001D43D',
    'K': '\U0001D43E',
    'L': '\U0001D43F',
    'M': '\U0001D440',
    'N': '\U0001D441',
    'O': '\U0001D442',
    'P': '\U0001D443',
    'Q': '\U0001D444',
    'R': '\U0001D445',
    'S': '\U0001D446',
    'T': '\U0001D447',
    'U': '\U0001D448',
    'V': '\U0001D449',
    'W': '\U0001D44A',
    'X': '\U0001D44B',
    'Y': '\U0001D44C',
    'Z': '\U0001D44D',
    'a': '\U0001D44E',
    'b': '\U0001D44F',
    'c': '\U0001D450',
    'd': '\U0001D451',
    'e': '\U0001D452',
    'f': '\U0001D453',
    'g': '\U0001D454',
    'h': '\U0000210E',
    'i': '\U0001D456',
    'j': '\U0001D457',
    'k': '\U0001D458',
    'l': '\U0001D459',
    'm': '\U0001D45A',
    'n': '\U0001D45B',
    'o': '\U0001D45C',
    'p': '\U0001D45D',
    'q': '\U0001D45E',
    'r': '\U0001D45F',
    's': '\U0001D460',
    't': '\U0001D461',
    'u': '\U0001D462',
    'v': '\U0001D463',
    'w': '\U0001D464',
    'x': '\U0001D465',
    'y': '\U0001D466',
    'z': '\U0001D467',
}

serif_b = {
    'A': '\U0001D400',
    'B': '\U0001D401',
    'C': '\U0001D402',
    'D': '\U0001D403',
    'E': '\U0001D404',
    'F': '\U0001D405',
    'G': '\U0001D406',
    'H': '\U0001D407',
    'I': '\U0001D408',
    'J': '\U0001D409',
    'K': '\U0001D40A',
    'L': '\U0001D40B',
    'M': '\U0001D40C',
    'N': '\U0001D40D',
    'O': '\U0001D40E',
    'P': '\U0001D40F',
    'Q': '\U0001D410',
    'R': '\U0001D411',
    'S': '\U0001D412',
    'T': '\U0001D413',
    'U': '\U0001D414',
    'V': '\U0001D415',
    'W': '\U0001D416',
    'X': '\U0001D417',
    'Y': '\U0001D418',
    'Z': '\U0001D419',
    'a': '\U0001D41A',
    'b': '\U0001D41B',
    'c': '\U0001D41C',
    'd': '\U0001D41D',
    'e': '\U0001D41E',
    'f': '\U0001D41F',
    'g': '\U0001D420',
    'h': '\U0001D421',
    'i': '\U0001D422',
    'j': '\U0001D423',
    'k': '\U0001D424',
    'l': '\U0001D425',
    'm': '\U0001D426',
    'n': '\U0001D427',
    'o': '\U0001D428',
    'p': '\U0001D429',
    'q': '\U0001D42A',
    'r': '\U0001D42B',
    's': '\U0001D42C',
    't': '\U0001D42D',
    'u': '\U0001D42E',
    'v': '\U0001D42F',
    'w': '\U0001D430',
    'x': '\U0001D431',
    'y': '\U0001D432',
    'z': '\U0001D433',
}

# A, B, O, P problems
squared_n = {
    'a': '\U0001F170',
    'b': '\U0001F171',
    'c': '\U0001F172',
    'd': '\U0001F173',
    'e': '\U0001F174',
    'f': '\U0001F175',
    'g': '\U0001F176',
    'h': '\U0001F177',
    'i': '\U0001F178',
    'j': '\U0001F179',
    'k': '\U0001F17A',
    'l': '\U0001F17B',
    'm': '\U0001F17C',
    'n': '\U0001F17D',
    'o': '\U0001F17E',
    'p': '\U0001F17F',
    'q': '\U0001F180',
    'r': '\U0001F181',
    's': '\U0001F182',
    't': '\U0001F183',
    'u': '\U0001F184',
    'v': '\U0001F185',
    'w': '\U0001F186',
    'x': '\U0001F187',
    'y': '\U0001F188',
    'z': '\U0001F189',
}

squared = {
    'a': '\U0001F130',
    'b': '\U0001F131',
    'c': '\U0001F132',
    'd': '\U0001F133',
    'e': '\U0001F134',
    'f': '\U0001F135',
    'g': '\U0001F136',
    'h': '\U0001F137',
    'i': '\U0001F138',
    'j': '\U0001F139',
    'k': '\U0001F13A',
    'l': '\U0001F13B',
    'm': '\U0001F13C',
    'n': '\U0001F13D',
    'o': '\U0001F13E',
    'p': '\U0001F13F',
    'q': '\U0001F140',
    'r': '\U0001F141',
    's': '\U0001F142',
    't': '\U0001F143',
    'u': '\U0001F144',
    'v': '\U0001F145',
    'w': '\U0001F146',
    'x': '\U0001F147',
    'y': '\U0001F148',
    'z': '\U0001F149',
}

circled_n = {
    'A': '\U0001F150',
    'B': '\U0001F151',
    'C': '\U0001F152',
    'D': '\U0001F153',
    'E': '\U0001F154',
    'F': '\U0001F155',
    'G': '\U0001F156',
    'H': '\U0001F157',
    'I': '\U0001F158',
    'J': '\U0001F159',
    'K': '\U0001F15A',
    'L': '\U0001F15B',
    'M': '\U0001F15C',
    'N': '\U0001F15D',
    'O': '\U0001F15E',
    'P': '\U0001F15F',
    'Q': '\U0001F160',
    'R': '\U0001F161',
    'S': '\U0001F162',
    'T': '\U0001F163',
    'U': '\U0001F164',
    'V': '\U0001F165',
    'W': '\U0001F166',
    'X': '\U0001F167',
    'Y': '\U0001F168',
    'Z': '\U0001F169',
}

# M problem
circled = {
    'A': u'\u24B6',
    'B': u'\u24B7',
    'C': u'\u24B8',
    'D': u'\u24B9',
    'E': u'\u24BA',
    'F': u'\u24BB',
    'G': u'\u24BC',
    'H': u'\u24BD',
    'I': u'\u24BE',
    'J': u'\u24BF',
    'K': u'\u24C0',
    'L': u'\u24C1',
    'M': u'\u24C2',
    'N': u'\u24C3',
    'O': u'\u24C4',
    'P': u'\u24C5',
    'Q': u'\u24C6',
    'R': u'\u24C7',
    'S': u'\u24C8',
    'T': u'\u24C9',
    'U': u'\u24CA',
    'V': u'\u24CB',
    'W': u'\u24CC',
    'X': u'\u24CD',
    'Y': u'\u24CE',
    'Z': u'\u24CF',
    'a': u'\u24D0',
    'b': u'\u24D1',
    'c': u'\u24D2',
    'd': u'\u24D3',
    'e': u'\u24D4',
    'f': u'\u24D5',
    'g': u'\u24D6',
    'h': u'\u24D7',
    'i': u'\u24D8',
    'j': u'\u24D9',
    'k': u'\u24DA',
    'l': u'\u24DB',
    'm': u'\u24DC',
    'n': u'\u24DD',
    'o': u'\u24DE',
    'p': u'\u24DF',
    'q': u'\u24E0',
    'r': u'\u24E1',
    's': u'\u24E2',
    't': u'\u24E3',
    'u': u'\u24E4',
    'v': u'\u24E5',
    'w': u'\u24E6',
    'x': u'\u24E7',
    'y': u'\u24E8',
    'z': u'\u24E9',
}

script_b = {
    'A': '\U0001D4D0',
    'B': '\U0001D4D1',
    'C': '\U0001D4D2',
    'D': '\U0001D4D3',
    'E': '\U0001D4D4',
    'F': '\U0001D4D5',
    'G': '\U0001D4D6',
    'H': '\U0001D4D7',
    'I': '\U0001D4D8',
    'J': '\U0001D4D9',
    'K': '\U0001D4DA',
    'L': '\U0001D4DB',
    'M': '\U0001D4DC',
    'N': '\U0001D4DD',
    'O': '\U0001D4DE',
    'P': '\U0001D4DF',
    'Q': '\U0001D4E0',
    'R': '\U0001D4E1',
    'S': '\U0001D4E2',
    'T': '\U0001D4E3',
    'U': '\U0001D4E4',
    'V': '\U0001D4E5',
    'W': '\U0001D4E6',
    'X': '\U0001D4E7',
    'Y': '\U0001D4E8',
    'Z': '\U0001D4E9',
    'a': '\U0001D4EA',
    'b': '\U0001D4EB',
    'c': '\U0001D4EC',
    'd': '\U0001D4ED',
    'e': '\U0001D4EE',
    'f': '\U0001D4EF',
    'g': '\U0001D4F0',
    'h': '\U0001D4F1',
    'i': '\U0001D4F2',
    'j': '\U0001D4F3',
    'k': '\U0001D4F4',
    'l': '\U0001D4F5',
    'm': '\U0001D4F6',
    'n': '\U0001D4F7',
    'o': '\U0001D4F8',
    'p': '\U0001D4F9',
    'q': '\U0001D4FA',
    'r': '\U0001D4FB',
    's': '\U0001D4FC',
    't': '\U0001D4FD',
    'u': '\U0001D4FE',
    'v': '\U0001D4FF',
    'w': '\U0001D500',
    'x': '\U0001D501',
    'y': '\U0001D502',
    'z': '\U0001D503',
}

script = {
    'A': '\U0001D49C',
    'B': '\U0000212C',
    'C': '\U0001D49E',
    'D': '\U0001D49F',
    'E': '\U00002130',
    'F': '\U00002131',
    'G': '\U0001D4A2',
    'H': '\U0000210B',
    'I': '\U00002110',
    'J': '\U0001D4A5',
    'K': '\U0001D4A6',
    'L': '\U00002112',
    'M': '\U00002133',
    'N': '\U0001D4A9',
    'O': '\U0001D4AA',
    'P': '\U0001D4AB',
    'Q': '\U0001D4AC',
    'R': '\U0000211B',
    'S': '\U0001D4AE',
    'T': '\U0001D4AF',
    'U': '\U0001D4B0',
    'V': '\U0001D4B1',
    'W': '\U0001D4B2',
    'X': '\U0001D4B3',
    'Y': '\U0001D4B4',
    'Z': '\U0001D4B5',
    'a': '\U0001D4B6',
    'b': '\U0001D4B7',
    'c': '\U0001D4B8',
    'd': '\U0001D4B9',
    'e': '\U0000212F',
    'f': '\U0001D4BB',
    'g': '\U0000210A',
    'h': '\U0001D4BD',
    'i': '\U0001D4BE',
    'j': '\U0001D4BF',
    'k': '\U0001D4C0',
    'l': '\U0001D4C1',
    'm': '\U0001D4C2',
    'n': '\U0001D4C3',
    'o': '\U00002134',
    'p': '\U0001D4C5',
    'q': '\U0001D4C6',
    'r': '\U0001D4C7',
    's': '\U0001D4C8',
    't': '\U0001D4C9',
    'u': '\U0001D4CA',
    'v': '\U0001D4CB',
    'w': '\U0001D4CC',
    'x': '\U0001D4CD',
    'y': '\U0001D4CE',
    'z': '\U0001D4CF',
}

double_struck = {
    'A': '\U0001D538',
    'B': '\U0001D539',
    'C': '\U00002102',
    'D': '\U0001D53B',
    'E': '\U0001D53C',
    'F': '\U0001D53D',
    'G': '\U0001D53E',
    'H': '\U0000210D',
    'I': '\U0001D540',
    'J': '\U0001D541',
    'K': '\U0001D542',
    'L': '\U0001D543',
    'M': '\U0001D544',
    'N': '\U00002115',
    'O': '\U0001D546',
    'P': '\U00002119',
    'Q': '\U0000211A',
    'R': '\U0000211D',
    'S': '\U0001D54A',
    'T': '\U0001D54B',
    'U': '\U0001D54C',
    'V': '\U0001D54D',
    'W': '\U0001D54E',
    'X': '\U0001D54F',
    'Y': '\U0001D550',
    'Z': '\U00002124',
    'a': '\U0001D552',
    'b': '\U0001D553',
    'c': '\U0001D554',
    'd': '\U0001D555',
    'e': '\U0001D556',
    'f': '\U0001D557',
    'g': '\U0001D558',
    'h': '\U0001D559',
    'i': '\U0001D55A',
    'j': '\U0001D55B',
    'k': '\U0001D55C',
    'l': '\U0001D55D',
    'm': '\U0001D55E',
    'n': '\U0001D55F',
    'o': '\U0001D560',
    'p': '\U0001D561',
    'q': '\U0001D562',
    'r': '\U0001D563',
    's': '\U0001D564',
    't': '\U0001D565',
    'u': '\U0001D566',
    'v': '\U0001D567',
    'w': '\U0001D568',
    'x': '\U0001D569',
    'y': '\U0001D56A',
    'z': '\U0001D56B',    
}

monospace = {
    'A': '\U0001D670',
    'B': '\U0001D671',
    'C': '\U0001D672',
    'D': '\U0001D673',
    'E': '\U0001D674',
    'F': '\U0001D675',
    'G': '\U0001D676',
    'H': '\U0001D677',
    'I': '\U0001D678',
    'J': '\U0001D679',
    'K': '\U0001D67A',
    'L': '\U0001D67B',
    'M': '\U0001D67C',
    'N': '\U0001D67D',
    'O': '\U0001D67E',
    'P': '\U0001D67F',
    'Q': '\U0001D680',
    'R': '\U0001D681',
    'S': '\U0001D682',
    'T': '\U0001D683',
    'U': '\U0001D684',
    'V': '\U0001D685',
    'W': '\U0001D686',
    'X': '\U0001D687',
    'Y': '\U0001D688',
    'Z': '\U0001D689',
    'a': '\U0001D68A',
    'b': '\U0001D68B',
    'c': '\U0001D68C',
    'd': '\U0001D68D',
    'e': '\U0001D68E',
    'f': '\U0001D68F',
    'g': '\U0001D690',
    'h': '\U0001D691',
    'i': '\U0001D692',
    'j': '\U0001D693',
    'k': '\U0001D694',
    'l': '\U0001D695',
    'm': '\U0001D696',
    'n': '\U0001D697',
    'o': '\U0001D698',
    'p': '\U0001D699',
    'q': '\U0001D69A',
    'r': '\U0001D69B',
    's': '\U0001D69C',
    't': '\U0001D69D',
    'u': '\U0001D69E',
    'v': '\U0001D69F',
    'w': '\U0001D6A0',
    'x': '\U0001D6A1',
    'y': '\U0001D6A2',
    'z': '\U0001D6A3',    
}

fraktur = {
    'A': '\U0001D504',
    'B': '\U0001D505',
    'C': '\U0000212D',
    'D': '\U0001D507',
    'E': '\U0001D508',
    'F': '\U0001D509',
    'G': '\U0001D50A',
    'H': '\U0000210C',
    'I': '\U00002111',
    'J': '\U0001D50D',
    'K': '\U0001D50E',
    'L': '\U0001D50F',
    'M': '\U0001D510',
    'N': '\U0001D511',
    'O': '\U0001D512',
    'P': '\U0001D513',
    'Q': '\U0001D514',
    'R': '\U0000211C',
    'S': '\U0001D516',
    'T': '\U0001D517',
    'U': '\U0001D518',
    'V': '\U0001D519',
    'W': '\U0001D51A',
    'X': '\U0001D51B',
    'Y': '\U0001D51C',
    'Z': '\U00002128',
    'a': '\U0001D51E',
    'b': '\U0001D51F',
    'c': '\U0001D520',
    'd': '\U0001D521',
    'e': '\U0001D522',
    'f': '\U0001D523',
    'g': '\U0001D524',
    'h': '\U0001D525',
    'i': '\U0001D526',
    'j': '\U0001D527',
    'k': '\U0001D528',
    'l': '\U0001D529',
    'm': '\U0001D52A',
    'n': '\U0001D52B',
    'o': '\U0001D52C',
    'p': '\U0001D52D',
    'q': '\U0001D52E',
    'r': '\U0001D52F',
    's': '\U0001D530',
    't': '\U0001D531',
    'u': '\U0001D532',
    'v': '\U0001D533',
    'w': '\U0001D534',
    'x': '\U0001D535',
    'y': '\U0001D536',
    'z': '\U0001D537',
}

fraktur_b = {
    'A': '\U0001D56C',
    'B': '\U0001D56D',
    'C': '\U0001D56E',
    'D': '\U0001D56F',
    'E': '\U0001D570',
    'F': '\U0001D571',
    'G': '\U0001D572',
    'H': '\U0001D573',
    'I': '\U0001D574',
    'J': '\U0001D575',
    'K': '\U0001D576',
    'L': '\U0001D577',
    'M': '\U0001D578',
    'N': '\U0001D579',
    'O': '\U0001D57A',
    'P': '\U0001D57B',
    'Q': '\U0001D57C',
    'R': '\U0001D57D',
    'S': '\U0001D57E',
    'T': '\U0001D57F',
    'U': '\U0001D580',
    'V': '\U0001D581',
    'W': '\U0001D582',
    'X': '\U0001D583',
    'Y': '\U0001D584',
    'Z': '\U0001D585',
    'a': '\U0001D586',
    'b': '\U0001D587',
    'c': '\U0001D588',
    'd': '\U0001D589',
    'e': '\U0001D58A',
    'f': '\U0001D58B',
    'g': '\U0001D58C',
    'h': '\U0001D58D',
    'i': '\U0001D58E',
    'j': '\U0001D58F',
    'k': '\U0001D590',
    'l': '\U0001D591',
    'm': '\U0001D592',
    'n': '\U0001D593',
    'o': '\U0001D594',
    'p': '\U0001D595',
    'q': '\U0001D596',
    'r': '\U0001D597',
    's': '\U0001D598',
    't': '\U0001D599',
    'u': '\U0001D59A',
    'v': '\U0001D59B',
    'w': '\U0001D59C',
    'x': '\U0001D59D',
    'y': '\U0001D59E',
    'z': '\U0001D59F',    
}