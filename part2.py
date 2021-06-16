
from functools import reduce, partial
from random import randint
import math
import random

def fibonacci_series(Number):
    if(Number == 0):
        return 0
    elif(Number == 1):
        return 1
    else:
        return (fibonacci_series(Number - 2) + fibonacci_series(Number - 1))

def is_fibonacci(number: int) -> bool:
    fibonacci_list = [fibonacci_series(x) for x in range(22)]
    return list(filter(lambda x: x == number, fibonacci_list)) != []

def add_2_iterables(a: "iterable", b: "iterable") -> "iterable":
    return [x + y for (x, y) in zip(filter(lambda x: x%2 == 0, a), filter(lambda x: x%2 == 1, b))]

def strip_vowel_from_word(word: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']

    return ''.join([x for x in word if x not in vowels])

def sigmoid_func(arr: list) -> list:
    return [1/(1 + math.exp(-x)) for x in arr]

def shift_characters_by_5(char_string: "Character string") -> str:
    return [chr(ord(char) + 5) if (ord(char) + 5 <= ord('z')) else chr(ord(char) + 5 - ord('z') + ord('a')) for char in char_string ]

def check_paragraph_has_any_swear_words(paragraph: str) -> bool:
    swear_words_list = ["4r5e","5h1t","5hit","a55","anal","anus","ar5e","arrse","arse","ass","ass-fucker","asses","assfucker","assfukka","asshole","assholes","asswhole","a_s_s","b!tch","b00bs","b17ch","b1tch","ballbag","balls","ballsack","bastard","beastial","beastiality","bellend","bestial","bestiality","bi+ch","biatch","bitch","bitcher","bitchers","bitches","bitchin","bitching","bloody","blow job","blowjob","blowjobs","boiolas","bollock","bollok","boner","boob","boobs","booobs","boooobs","booooobs","booooooobs","breasts","buceta","bugger","bum","bunny fucker","butt","butthole","buttmunch","buttplug","c0ck","c0cksucker","carpet muncher","cawk","chink","cipa","cl1t","clit","clitoris","clits","cnut","cock","cock-sucker","cockface","cockhead","cockmunch","cockmuncher","cocks","cocksuck ","cocksucked ","cocksucker","cocksucking","cocksucks ","cocksuka","cocksukka","cok","cokmuncher","coksucka","coon","cox","crap","cum","cummer","cumming","cums","cumshot","cunilingus","cunillingus","cunnilingus","cunt","cuntlick ","cuntlicker ","cuntlicking ","cunts","cyalis","cyberfuc","cyberfuck ","cyberfucked ","cyberfucker","cyberfuckers","cyberfucking ","d1ck","damn","dick","dickhead","dildo","dildos","dink","dinks","dirsa","dlck","dog-fucker","doggin","dogging","donkeyribber","doosh","duche","dyke","ejaculate","ejaculated","ejaculates ","ejaculating ","ejaculatings","ejaculation","ejakulate","f u c k","f u c k e r","f4nny","fag","fagging","faggitt","faggot","faggs","fagot","fagots","fags","fanny","fannyflaps","fannyfucker","fanyy","fatass","fcuk","fcuker","fcuking","feck","fecker","felching","fellate","fellatio","fingerfuck ","fingerfucked ","fingerfucker ","fingerfuckers","fingerfucking ","fingerfucks ","fistfuck","fistfucked ","fistfucker ","fistfuckers ","fistfucking ","fistfuckings ","fistfucks ","flange","fook","fooker","fuck","fucka","fucked","fucker","fuckers","fuckhead","fuckheads","fuckin","fucking","fuckings","fuckingshitmotherfucker","fuckme ","fucks","fuckwhit","fuckwit","fudge packer","fudgepacker","fuk","fuker","fukker","fukkin","fuks","fukwhit","fukwit","fux","fux0r","f_u_c_k","gangbang","gangbanged ","gangbangs ","gaylord","gaysex","goatse","God","god-dam","god-damned","goddamn","goddamned","hardcoresex ","hell","heshe","hoar","hoare","hoer","homo","hore","horniest","horny","hotsex","jack-off ","jackoff","jap","jerk-off ","jism","jiz ","jizm ","jizz","kawk","knob","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kum","kummer","kumming","kums","kunilingus","l3i+ch","l3itch","labia","lmfao","lust","lusting","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","masochist","master-bate","masterb8","masterbat*","masterbat3","masterbate","masterbation","masterbations","masturbate","mo-fo","mof0","mofo","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked ","mothafucker","mothafuckers","mothafuckin","mothafucking ","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","muff","mutha","muthafecker","muthafuckker","muther","mutherfucker","n1gga","n1gger","nazi","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers ","nob","nob jokey","nobhead","nobjocky","nobjokey","numbnuts","nutsack","orgasim ","orgasims ","orgasm","orgasms ","p0rn","pawn","pecker","penis","penisfucker","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","pigfucker","pimpis","piss","pissed","pisser","pissers","pisses ","pissflaps","pissin ","pissing","pissoff ","poop","porn","porno","pornography","pornos","prick","pricks ","pron","pube","pusse","pussi","pussies","pussy","pussys ","rectum","retard","rimjaw","rimming","s hit","s.o.b.","sadist","schlong","screwing","scroat","scrote","scrotum","semen","sex","sh!+","sh!t","sh1t","shag","shagger","shaggin","shagging","shemale","shi+","shit","shitdick","shite","shited","shitey","shitfuck","shitfull","shithead","shiting","shitings","shits","shitted","shitter","shitters ","shitting","shittings","shitty ","skank","slut","sluts","smegma","smut","snatch","son-of-a-bitch","spac","spunk","s_h_i_t","t1tt1e5","t1tties","teets","teez","testical","testicle","tit","titfuck","tits","titt","tittie5","tittiefucker","titties","tittyfuck","tittywank","titwank","tosser","turd","tw4t","twat","twathead","twatty","twunt","twunter","v14gra","v1gra","vagina","viagra","vulva","w00se","wang","wank","wanker","wanky","whoar","whore","willies","willy","xrated","xxx"]

    return any(word for word in paragraph.split(" ") if word in swear_words_list)

def add_even_nums_in_list(num_list: list) -> int:
    return reduce(lambda x,y: x + y if y%2 == 0 else x, num_list, 0)

def find_biggest_char_in_a_str(char_str: str) -> str:
    return reduce(lambda x,y: x if x > y else y, char_str)

def add_3rd_num_in_list(num_list: list) -> list:
    return reduce(lambda x,y: x + num_list[y] if y == 0 or (y+1)%3 == 0 else num_list[x], list(range(len(num_list))), 0)

def random_number_plates() -> list:
    alphabets = [chr(x) for x in range(65, 91)]

    return ["KA" + str(randint(10, 99)) + random.choice(alphabets) + random.choice(alphabets) + str(randint(1000, 9999)) for x in range(15)]

def random_number_plates_generic(range_start: int, range_stop: int, state : str) -> list:
    alphabets = [chr(x) for x in range(65, 91)]

    return [state + str(randint(10, 99)) + random.choice(alphabets) + random.choice(alphabets) + str(randint(range_start, range_stop)) for x in range(15)]

random_number_plates_using_partial_function = partial(random_number_plates_generic, 1000, 9999)

