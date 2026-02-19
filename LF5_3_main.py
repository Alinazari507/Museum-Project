# LF5_3_main.py
from LF5_3_models import Exhibit, Dimensions
from LF5_3_repository import ExhibitRepository

def main():
    # 1. Initialization
    repo = ExhibitRepository("exhibits.json")
    repo.load_from_json()

    # 2. Seeding Data (If database is empty)
    if not repo.get_all():
        print("--- 🆕 Initializing Museum Database ---")
        d1 = Dimensions(150, 100, 10)
        e1 = Exhibit("MUSE-001", "Mona Lisa", "Leonardo da Vinci", 1503, d1)
        
        d2 = Dimensions(120, 90, 5)
        e2 = Exhibit("MUSE-002", "Starry Night", "Vincent van Gogh", 1889, d2)
        
        d3 = Dimensions(200, 180, 10)
        e3 = Exhibit("MUSE-003", "Guernica", "Pablo Picasso", 1937, d3)
        
        repo.add(e1)
        repo.add(e2)
        repo.add(e3)
        repo.save_to_json()

    print("\n" + "="*40)
    print("🏛️  WELCOME TO NEUSTADT MUSEUM SYSTEM")
    print("="*40)

    # 3. USE CASE 1: Display All Exhibits
    print("\n📜 FULL COLLECTION:")
    for work in repo.get_all():
        print(f"- {work}")

    # 4. USE CASE 2: Advanced Filtering (Functional Programming)
    # Goal: Find exhibits from the 19th Century (1800-1899)
    print("\n🔎 SEARCH: 19th Century Masterpieces:")
    century_19 = repo.query(lambda e: 1800 <= e.year <= 1899)
    for work in century_19:
        print(f"   [FOUND] {work.title} by {work.artist}")

    # 5. USE CASE 3: Statistics (Map & Reduce)
    # Goal: Calculate average year of all artworks
    avg_year = repo.calculate_average_year()
    print("\n📊 MUSEUM ANALYTICS:")
    print(f"   Average Creation Year: {int(avg_year)}")
    
    # 6. USE CASE 4: Total Insurance Valuation (Lambda)
    # Let's calculate 10% tax for the entire collection's value (fictional price)
    insurance_calc = lambda items: len(items) * 500  # $500 per item for insurance
    total_insurance = insurance_calc(repo.get_all())
    print(f"   Estimated Insurance Coverage: ${total_insurance}")

    print("\n" + "="*40)
    print("✅ System update complete.")

if __name__ == "__main__":
    main()