from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline # Для полоценного поиска
from django.db.models import Q # Импортируем класс Q из модуля django.db.models для создания сложных запросов к базе данных

def q_search(query):
    if query.isdigit() and len(query) <= 3:
        return Products.objects.filter(id=int(query))
    

    vector = SearchVector('description', 'name') # Создаем векторный индекс для полнотекстового поиска по полям description и name
    query = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
    
    result = result.annotate(headline=SearchHeadline('name', query, start_sel='<span style="background-color: yellow;">', stop_sel='</span>')) # Добавляем аннотацию headline с выделением найденных слов
    result = result.annotate(bodyline=SearchHeadline('description', query, start_sel='<span style="background-color: yellow;">', stop_sel='</span>'))

    return result