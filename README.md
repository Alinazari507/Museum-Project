# 🏛️ Neustadt Museum: Data Foundation Prototype

A professional Python-based management system for the Neustadt Museum, establishing a standardized environment through **Clean Architecture**, **Domain-Driven Design (DDD)**, and **Functional Programming**.

---

## 🏗️ Methodology: 20% Analog / 80% Digital

### 🧱 Analog Domain Modeling (20%)
To fulfill the **Ganzheitliche Aufgabe** requirements, the architecture was visualized using **LEGO Classic 10696**:
* **Baseplates:** Representing the `Repository` (Memory Space).
* **Entities (Eyes):** Representing unique exhibits with a persistent identity.
* **Small Bricks:** Representing `Value Objects` (Dimensions) attached to entities.

### 💻 Digital Engineering (80%)
* **Repository Pattern:** Decouples domain logic from JSON storage, ensuring the system is technology-agnostic.
* **Functional Pipeline:** Advanced filtering and data analytics (Map-Reduce) using `lambda` and `filter` for side-effect-free operations.
* **Strict Modeling:** Separation of **Entities** (Exhibit) and **Value Objects** (Dimensions).



---

## 🚀 Key Features & Paradigms

* **Advanced Query Engine:** Dynamic search using functional lambda expressions.
* **Data Analytics:** Map-Reduce paradigm for calculating museum metrics (e.g., average exhibit age).
* **Quality Assurance:** Integrated Unit Testing suite to ensure identity integrity and data validation.
* **Dev-Ops Standards:** Professional `.gitignore` for environment isolation and atomic Git commits.



---

## 📂 Project Structure
* `LF5_3_models.py`: Domain Layer (The "What").
* `LF5_3_repository.py`: Infrastructure Layer (The "How").
* `LF5_3_main.py`: Application Layer (The Orchestrator).
* `test_suite.py`: Quality Assurance (Unit Tests).
* `exhibits.json`: Persistent Data Storage.

---

## 💻 How to Run

### 1. Run the Application
```bash
python LF5_3_main.py