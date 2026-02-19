# 🏛️ Neustadt Museum: Data Foundation Prototype

A professional Python-based management system for the Neustadt Museum, establishing a standardized environment through **Clean Architecture**, **Domain-Driven Design (DDD)**, and **Functional Programming**.

---

## 🏗️ Methodology: 20% Analog / 80% Digital

### 🧱 Analog Domain Modeling (20%)
<<<<<<< HEAD
To fulfill the **Ganzheitliche Aufgabe** requirements, the architecture was visualized using **LEGO Classic 10696**:
* **Baseplates:** Representing the `Repository` (Memory Space).
* **Entities (Eyes):** Representing unique exhibits with a persistent identity.
* **Small Bricks:** Representing `Value Objects` (Dimensions) attached to entities.
=======
To fulfill the **Ganzheitliche Aufgabe** requirements, we visualized the domain logic using **LEGO Classic 10696**. This physical modeling helped us define core architectural boundaries:

1. **The Repository & Data Foundation:** Establishing the baseplate as the memory space.
   ![Step 1: Parsing Raw Data](analog.jpeg)

2. **Entity Identity (K3):** Using "Eyes" to represent unique exhibits. Each entity is assigned a unique identifier to represent its identity in the system.
   ![Step 2: ID MUSE-001](analog1.jpeg)

3. **Collection Scaling:** Modeling how multiple entities (MUSE-002, MUSE-003) are organized within the repository.
   ![Step 3: ID MUSE-002](analog2.jpeg)
   ![Step 4: Final Domain Overview](analog3.jpeg)
>>>>>>> 64022f64d941dc0971550f990a13fd60ec8cf01a

### 💻 Digital Engineering (80%)
* **Repository Pattern:** Decouples domain logic from JSON storage, ensuring the system is technology-agnostic.
* **Functional Pipeline:** Advanced filtering and data analytics (Map-Reduce) using `lambda` and `filter` for side-effect-free operations.
* **Strict Modeling:** Separation of **Entities** (Exhibit) and **Value Objects** (Dimensions).

<<<<<<< HEAD


=======
>>>>>>> 64022f64d941dc0971550f990a13fd60ec8cf01a
---

## 🚀 Key Features & Paradigms

<<<<<<< HEAD
* **Advanced Query Engine:** Dynamic search using functional lambda expressions.
* **Data Analytics:** Map-Reduce paradigm for calculating museum metrics (e.g., average exhibit age).
* **Quality Assurance:** Integrated Unit Testing suite to ensure identity integrity and data validation.
* **Dev-Ops Standards:** Professional `.gitignore` for environment isolation and atomic Git commits.


=======
* **Advanced Query Engine:** Dynamic search using functional lambda expressions to filter exhibits by year, artist, or type.
* **Data Analytics:** Implementation of the Map-Reduce pattern to calculate museum metrics, such as the average age of the collection.
* **Quality Assurance:** Integrated Unit Testing suite to ensure identity integrity and data validation.
* **Dev-Ops Standards:** Professional `.gitignore` configuration for environment isolation and atomic Git commits.

---

## 🔍 Technical Analysis (K4)

### Data Format Comparison
After evaluating **JSON, XML, and YAML** for museum archiving:
* **JSON (Selected):** Best for its lightweight structure and native compatibility with Python dictionaries.
* **XML:** Rejected due to high verbosity and complexity for this specific use case.
* **YAML:** Excellent for configuration but less efficient for large data object reconstruction.
>>>>>>> 64022f64d941dc0971550f990a13fd60ec8cf01a

---

## 📂 Project Structure
<<<<<<< HEAD
* `LF5_3_models.py`: Domain Layer (The "What").
* `LF5_3_repository.py`: Infrastructure Layer (The "How").
* `LF5_3_main.py`: Application Layer (The Orchestrator).
* `test_suite.py`: Quality Assurance (Unit Tests).
* `exhibits.json`: Persistent Data Storage.
=======
* `LF5_3_models.py`: Domain Layer (Entities & Value Objects).
* `LF5_3_repository.py`: Infrastructure Layer (Persistence & Functional Logic).
* `LF5_3_main.py`: Application Layer (Orchestrator).
* `test_suite.py`: Quality Assurance (Unit Tests).
* `exhibits.json`: Data Storage.
>>>>>>> 64022f64d941dc0971550f990a13fd60ec8cf01a

---

## 💻 How to Run

<<<<<<< HEAD
### 1. Run the Application
```bash
python LF5_3_main.py
=======
### 1. Start the Application
```bash
python LF5_3_main.py
python test_suite.py
>>>>>>> 64022f64d941dc0971550f990a13fd60ec8cf01a
