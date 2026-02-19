# 🏛️ Neustadt Museum Management System

A professional Python-based museum management system implementing Clean Architecture and Functional Programming patterns.

## 🚀 Key Features
- **Repository Pattern:** Decouples domain logic from JSON storage.
- **Advanced Query Engine:** Uses lambda functions and filters for real-time data retrieval.
- **Data Analytics:** Implements `map` and `reduce` to calculate museum statistics (e.g., average exhibit age).
- **OOP Excellence:** Uses Entities (Exhibit) and Value Objects (Dimensions) for robust modeling.

## 🛠️ Project Structure
- `LF5_3_models.py`: Domain entities and core logic.
- `LF5_3_repository.py`: Data access layer and functional aggregators.
- `LF5_3_main.py`: Application orchestrator and user interaction.
- `exhibits.json`: Persistent data storage.

## 💻 How to Run
1. Ensure you have Python 3.x installed.
2. Run the main script:
   ```bash
   python LF5_3_main.py