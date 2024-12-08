from youtube_search import YoutubeSearch
from langdetect import detect 

import_lista = input("Z jakiego pliku importować listę? ")
file_name = input("Do jakiego pliku zapisać wyniki?: ")

with open(import_lista, 'r', encoding='utf-8') as file:
    lista = file.read().splitlines()

def is_polish(text):
    try:
        language = detect(text)
        return language == 'pl'
    except:
        return False

def search():
    results = []

    for topic in lista:
        print(f"Szukam filmów o: {topic}")
        results_page = YoutubeSearch(topic, max_results=10).to_dict()

        for item in results_page:
            title = item['title']
            video_url = f"https://youtube.com/watch?v={item['id']}"

            if is_polish(title):
                modified_link = video_url.replace('youtube.com', 'inv.nadeko.net')
                results.append(f"{title} - {modified_link}")

    return results
    
def save_to_file(results):
    with open(file_name, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + "\n\n")
    print("Zapisano do", file_name)

if __name__ == "__main__":
    videos = search()

    save_to_file(videos)                          
