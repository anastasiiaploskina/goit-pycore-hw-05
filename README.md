
# **Python Utility Applications — README**

This repository contains several Python utility scripts demonstrating recursion, generators, parsing, and command-line interaction. Each script is self-contained and showcases a particular programming technique.

---

## **Table of Contents**

* [Task 1 — Fibonacci Utilities](#task-1--fibonacci-utilities)
* [Task 2 — Profit Summation From Text](#task-2--profit-summation-from-text)
* [Task 4 — Assistant Bot](#task-4--assistant-bot)
* [Installation](#installation)
* [Usage](#usage)
* [Dependencies](#dependencies)

---

# **Task 1 — Fibonacci Utilities**


### **Description**

This module implements two different ways to generate Fibonacci numbers:

1. **Memoized recursive Fibonacci function** using a closure and internal cache
2. **Infinite Fibonacci generator** using Python's generator protocol

### **Features**

* Efficient computation with caching
* Infinite sequence generation
* Clean, functional design using closures
* Includes assertions for self-testing

### **Key Functions**

#### **1. caching_fibonacci()**

Returns a Fibonacci function that remembers previous results:

```python
fib = caching_fibonacci()
fib(10)  # 55
```

#### **2. fibonacci_generator()**

Generates Fibonacci numbers indefinitely:

```python
gen = fibonacci_generator()
next(gen)  # 0
next(gen)  # 1
next(gen)  # 1
next(gen)  # 2
```

---

# **Task 2 — Profit Summation From Text**


### **Description**

This script extracts all **integer or floating-point numbers** from a text and computes their total sum.

### **Features**

* Regex-based number extraction
* Generator function for memory-efficient processing
* Handles integers and decimals
* Supports both `.` and `,` as decimal separators
* Clear separation of logic into generator and aggregator functions

### **Key Function**

#### **generator_numbers(text: str)**

Yields numbers found in the text:

```python
for n in generator_numbers("Income: 10.5 and 20"):
    print(n)
```

#### **sum_profit(text: str, func)**

Sums all numbers produced by the generator:

```python
total = sum_profit(text, generator_numbers)
```

### **Example**

```python
text = "1000.01 ... 27.45 ... 324.00"
total_income = sum_profit(text, generator_numbers)
# 1351.46
```

---

# **Task 4 — Assistant Bot**


### **Description**

A command-line assistant bot that stores and manages contacts using a simple REPL (read-eval-print loop).
It supports adding, modifying, and viewing phone numbers.

### **Features**

* Supports commands:
  `hello`, `add`, `change`, `phone`, `all`, `help`, `close`, `exit`
* Validates phone numbers (`+380XXXXXXXXX`)
* Graceful error handling using a custom `@input_error` decorator
* Formatted box output for contact lists
* Fully interactive console program

### **Command Overview**

| Command          | Example                     | Description              |
| ---------------- | --------------------------- | ------------------------ |
| `hello`          | `hello`                     | Greeting                 |
| `add`            | `add John +380631234567`    | Adds a new contact       |
| `change`         | `change John +380987654321` | Changes existing contact |
| `phone`          | `phone John`                | Shows a phone number     |
| `all`            | `all`                       | Display all contacts     |
| `help`           | `help`                      | Show help info           |
| `exit` / `close` | —                           | Exit program             |

### **Example Run**

```
Welcome to the assistant bot!
Enter a command: add Anna +380631112233
Contact added.
Enter a command: phone Anna
Anna's phone number is +380631112233.
```

---

# **Installation**

Clone or download the project, then ensure **Python 3.8+** is installed.

No external packages are required for Tasks 1 or 2.
Task 4 uses only Python’s standard library.

---

# **Usage**

Run any script directly:

```bash
python task_1.py
python task_2.py
python task_4.py
```

---

# **Dependencies**

This project uses only the Python standard library:

* `re`
* `typing`
* `closures`
* `generators`

No external installations required.

