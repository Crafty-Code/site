+++
title = "Writing Clean Functions: The Single Responsibility Principle in Practice"
description = "How to write functions that do one thing well — and why it makes your codebase dramatically easier to maintain."
date = 2024-10-01T09:00:00+01:00
author = "Jeff"
category = "Software Engineering"
tags = ["clean-code", "software-engineering", "best-practices", "refactoring"]
keywords = ["clean code", "single responsibility principle", "functions", "refactoring", "software engineering"]
difficulty = "intermediate"
toc = true
draft = false
+++

Good functions are the building blocks of good software. Yet it is surprisingly easy to write functions that do too much, know too much, or mean too little.

## The Single Responsibility Principle

The Single Responsibility Principle (SRP) states that a function should do one thing, do it well, and do it only. When a function has a single, clear purpose, it becomes:

- Easier to name
- Easier to test
- Easier to reuse
- Easier to change without fear

If you find yourself reaching for the word "and" when describing what a function does, it is doing too much.

## A Practical Example

Consider this function:

```python
def process_user(user_data):
    # Validate
    if not user_data.get("email"):
        raise ValueError("Email required")
    # Save to DB
    db.save(user_data)
    # Send welcome email
    send_email(user_data["email"], "Welcome!")
```

This function validates, persists, and sends an email. It has three reasons to change. Split it:

```python
def validate_user(user_data):
    if not user_data.get("email"):
        raise ValueError("Email required")

def save_user(user_data):
    db.save(user_data)

def send_welcome_email(email):
    send_email(email, "Welcome!")
```

Now each function is independently testable and replaceable.

## Naming Is a Signal

If you struggle to name a function without using vague words like `handle`, `process`, or `manage`, that is a signal the function is doing too much. A well-scoped function almost names itself.

## Keep Functions Short

Short functions are not a goal in themselves, but they are a natural outcome of good design. A function that fits on one screen is one you can reason about without scrolling.

Aim for functions where the abstraction level is consistent throughout — don't mix high-level orchestration with low-level implementation details in the same function.

## Conclusion

Clean functions are a discipline, not a talent. The habit of asking "does this function do exactly one thing?" pays compounding dividends as a codebase grows.
