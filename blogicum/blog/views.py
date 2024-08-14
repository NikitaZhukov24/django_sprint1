"""This module provides views functions for blog app."""
from django.http import Http404
from django.shortcuts import render

# Create your views here.
posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]

post_ids = {post['id']: position
            for position, post in enumerate(posts) if 'id' in post}


def index(request):
    """View function index."""
    template = 'blog/index.html'
    return render(request, template, {'posts': posts[::-1]})


def post_detail(request, id: int):
    """View function post_detail ."""
    template = 'blog/detail.html'
    try:
        # Исходя из исправления комментария, указанного ниже
        # "Не забывай, что ID поста - это не позиция в списке, а поле id в словаре. 
        # Поэтому для поиска по ID удобнее было бы создать еще один словарь, в котором будут храниться
        # пары ID поста - позиция в списке. И этот словарь лучше вне функции объявить, чтобы лишний раз
        # не создавать его"
        # Следует обратить внимание на ключевые слова
        # "Пары ID поста - позиция в списке"
        # Именно таким и сделан словарь post_ids
        return render(request, template, {'post': posts[post_ids[id]]})
    except KeyError:
        raise Http404("Post does not exist")


def category_posts(request, category_slug):
    """View function category_posts."""
    template = 'blog/category.html'
    return render(request, template, {'category_slug': category_slug,
                                      'posts': posts})
