# Museum Exhibit Management System 🏛️

A Python-based system to manage museum exhibits using Domain-Driven Design (DDD) principles like **Entities** and **Value Objects**.

## Features
* **Validation:** Automatic checks for physical dimensions (no negative values).
* **Smart Tracking:** Year of creation cannot be in the future.
* **Equality Checks:** Value Objects compared by data, Entities compared by unique ID.

## How to Use
To create a new exhibit, first define its dimensions:

```python
dims = Dimensions(100, 80, 10)
exhibit = Exhibit("ART-001", "The Night Watch", "Rembrandt", 1642, dims)