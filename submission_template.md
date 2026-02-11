# AI Code Review Assignment (Python)

## Candidate
- Name: Can Akgül
- Approximate time spent: 45 min

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The code excludes cancelled orders from the total sum but uses the total length of the list. It incorrectly fin the result.
-If the input list is empty, the code attempts to divide by zero.

### Edge cases & risks
- If there is no orders, it should safely return 0.0.
-If there are orders but the count is zero, it should safely return 0.0.

### Code quality / design issues
- Explantaion claims "correctly excludes cancelled orders" but this is not true for average calculation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- The count increment inside the if statement.
- Added a check if count == 0 before the division and at the beginning to return 0.0 immediately if the input list is empty.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I think the most important scenario is empty list case and zero-value valid orders. The code must safely return 0 for consistency.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
-  It does not mention the edge cases. Also its claim about average order value is not correct in the original code.

### Rewritten explanation
- This function calculates the average value of active orders by summing the amounts of all non-cancelled entries and dividing by the count of those valid orders. It includes safety checks to return 0.0 if the input list is empty or if no valid orders are found.

## 4) Final Judgment
- Decision: Reject
- Justification: The code consistently calculates the wrong average because it divides by wrong count.
- Confidence & unknowns: High Confidence. The code is unpredictable because of edge cases and incorrect calculation.
An unknown is that i assumed input has "status" and "amount" keys.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The validation only checks if "@" exists in the string. This accepts invalid emails like "@", "@@", or "test@" as valid.
- No verification of email structure.

### Edge cases & risks
- Non-string inputs (integers, None) would cause errors.
- Emails with whitespace are not trimmed before validation.
- Multiple "@" symbols would pass the check.
- Missing part of the email structure would be considered valid.

### Code quality / design issues
- The validation is too simplistic and does not follow email format structure.
- The explanation claims it "safely ignores invalid entries" but the validation itself is insufficient.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Implemented RFC-compliant regex pattern for proper email validation.
- Added type checking with try/except to handle non-string inputs safely.
- Added `.strip()` to remove leading/trailing whitespace.
- Pattern validates: local part, single @, domain, and TLD with minimum 2 characters.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I would focus on edge cases like empty strings, strings with only "@", multiple "@" symbols inputs. These scenarios are likely to be failed in the code.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It claims to count "valid" emails but the validation is not enough.
- Does not specify what makes an email valid or invalid.
- The implementation contradicts the claim of safely handling invalid entries.

### Rewritten explanation
- This function counts valid email addresses using email structure. A valid email must contain a local part, single "@" symbol, domain name, and top-level domain. It safely handles non-string inputs and whitespace, returning 0 for empty lists.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The code functions might correctly calculate the total numbers. But it is too simple for to be used.
- Confidence & unknowns: High confidence. The fix is easy:replace the basic check with a regex pattern. The core counting logic works fine.
Unknown is that i assume an email does not have whitespaces.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The code excludes None values from the total sum but uses the total length of the list. It incorrectly finds the result.
- If the input list is empty, the code attempts to divide by zero.

### Edge cases & risks
- If there are no values, it should safely return 0.0.
- If there are values but the count is zero, it should safely return 0.0.

### Code quality / design issues
- Explanation claims "safely handles mixed input types" but this is not true for average calculation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- The count increment inside the if statement.
- Added a check if count == 0 before the division and at the beginning to return 0.0 immediately if the input list is empty.
- Added try/except for safe float conversion.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I think the most important scenario is empty list case and all-None values. The code must safely return 0.0 for consistency.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- It does not mention the edge cases. Also its claim about accurate average is not correct in the original code.

### Rewritten explanation
- This function calculates the average of valid measurements by filtering out None values and converting remaining entries to float. It divides the sum by the count of those valid measurements. It includes safety checks to return 0.0 if the input list is empty or if no valid values are found.

## 4) Final Judgment
- Decision: Reject
- Justification: The code consistently calculates the wrong average because it divides by wrong count.
- Confidence & unknowns: High confidence. The code is unpredictable because of edge cases and incorrect calculation.
