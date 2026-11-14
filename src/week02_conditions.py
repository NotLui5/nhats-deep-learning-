"""Week 2: Conditions, Booleans, others."""


def is_worsening(previous = int, current = float):
    """Return True for decline, False otherwise, or None if a score is missing."""
    if current < previous:
        return True
    if previous is None or current is None:
        return None
    else:
        return "sajsjajsajs"

x = is_worsening(5, 3)  #  x = "sajsjajsajs" # dtype = str

# Expected results were written before running the script.
# These are synthetic values (valid clock scores: 0 to 5, or None).
print("1. Decline     | Expected: True  | Observed:", is_worsening(5, 3))
# print("2. Improvement | Expected: False | Observed:", is_worsening(2, 4))
# print("3. No change   | Expected: False | Observed:", is_worsening(3, 3))
# print("4. Zero score  | Expected: True  | Observed:", is_worsening(1, 0))
# print("5. Previous NA | Expected: None  | Observed:", is_worsening(None, 3))
# print("6. Current NA  | Expected: None  | Observed:", is_worsening(4, None))
