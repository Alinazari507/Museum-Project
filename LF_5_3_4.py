# ==========================================
# LF 5.3.4: Museum Management System
# ==========================================

def main():
    # --- TASK 1: Variables & Data Types ---
    print("--- Task 1: Visitor Data Types ---")
    visitor_name = "Ali"        # str
    age = 25                    # int
    ticket_price = 12.50        # float
    is_member = True            # bool

    print(f"Visitor: {visitor_name} | Type: {type(visitor_name)}")
    print(f"Age: {age} | Type: {type(age)}")
    print(f"Price: {ticket_price} | Type: {type(ticket_price)}")
    print(f"Member: {is_member} | Type: {type(is_member)}\n")


    # --- TASK 2 & 5: Input Logic & Comparison (Museum Age Calculator) ---
    print("--- Task 2 & 5: Exhibit Year Validation ---")
    current_year = 2026
    
    while True:
        try:
            year_input = input("Enter the exhibit creation year (1800-2026): ")
            year = int(year_input)
            
            # Using 'and' for range validation
            if year >= 1800 and year <= current_year:
                print(f"✅ Valid year: {year}. Acceptable for museum.")
                break # Exit loop once valid input is received
            else:
                # Using 'or' for logical feedback
                if year < 1800 or year > current_year:
                    print("❌ Invalid: Year must be between 1800 and 2026.")
        except ValueError:
            print("⚠️ Error: Please enter a valid integer number.")
    print("\n")


    # --- TASK 3: Iteration (For Loop - Exhibit List) ---
    print("--- Task 3: Exhibit List (For Loop) ---")
    exhibits = [
        "Starry Night - Van Gogh", 
        "The Scream - Munch", 
        "Guernica - Picasso",
        "Mona Lisa - Da Vinci",
        "The Night Watch - Rembrandt"
    ]
    
    for index, title in enumerate(exhibits, start=1):
        print(f"{index}. {title}")
    print("\n")


    # --- TASK 4: Search (While Loop - Case Insensitive) ---
    print("--- Task 4: Search Exhibits (While Loop) ---")
    search_term = input("Search for an artist or title: ").lower()
    index = 0
    found = False

    while index < len(exhibits):
        if search_term in exhibits[index].lower():
            print(f"🔍 Found: '{exhibits[index]}' at position {index + 1}")
            found = True
        index += 1
    
    if not found:
        print("🚫 No match found.")
    print("\n")


    # --- OPTIONAL TASK: Create (CLI Inventory System) ---
    print("--- Create: Museum Inventory Builder ---")
    inventory = []
    print("Add new items to inventory (Type 'exit' to finish):")
    
    while True:
        new_item = input("> ")
        if new_item.lower() == "exit":
            break
        if new_item: # Check if input is not empty
            inventory.append(new_item)
    
    print(f"\n✅ Inventory Updated. Total items added: {len(inventory)}")
    print(f"List: {inventory}")

if __name__ == "__main__":
    main()