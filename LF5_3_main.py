# LF5_3_main.py
from LF5_3_models import Exhibit, Dimensions
from LF5_3_repository import ExhibitRepository

def main():
    repo = ExhibitRepository()

    # 1. Load data from previous runs
    repo.load_from_json()

    # 2. If the list is empty, let's add some default exhibits
    if not repo.get_all():
        print("Inventory empty. Adding default items...")
        d1 = Dimensions(120, 90, 5)
        e1 = Exhibit("ART-001", "The Starry Night", "Vincent van Gogh", 1889, d1)
        
        d2 = Dimensions(200, 180, 10)
        e2 = Exhibit("ART-002", "Guernica", "Pablo Picasso", 1937, d2)
        
        repo.add(e1)
        repo.add(e2)
        repo.save_to_json()

    # 3. ADVANCED TASK: Use Functional Programming (Filter & Lambda)
    # Find only the works by Picasso
    picasso_works = list(filter(lambda x: x.artist == "Pablo Picasso", repo.get_all()))

    print("\n--- Search Results for Picasso ---")
    for work in picasso_works:
        print(f"Found: {work.title}")

if __name__ == "__main__":
    main()