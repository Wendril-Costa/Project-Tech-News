import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)

from tech_news.scraper import get_tech_news


# Requisitos 11 e 12
def analyzer_menu():
    options = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    match options:
        case "0":
            get_tech_news(
                int(input("Digite quantas notícias serão buscadas: "))
            )
        case "1":
            print(search_by_title(input("Digite o título: ")))
        case "2":
            print(
                search_by_date(input("Digite a data no formato dd-mm-aaaa: "))
            )
        case "3":
            print(search_by_category(input("Digite a categoria: ")))
        case "4":
            print(top_5_categories())
        case "5":
            print("Encerrando script")
            return
        case _:
            print("Opção inválida", file=sys.stderr)
