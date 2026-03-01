# Calculator Test Cases

This document contains functional test cases for a calculator that performs:

- Addition
- Subtraction
- Multiplication
- Division
- Decimal operations
- Negative numbers
- BODMAS / Order of operations
- Error handling for invalid inputs

---

##  Valid Input Test Cases

| Test Case ID | Test Description | Preconditions | Test Steps | Expected Results |
|---|---|---|---|---|
| TC-001 | Addition of two positive integers | Calculator is running | 1. Enter `5 + 3` <br> 2. Press `=` | Result displayed: **8** |
| TC-002 | Addition with negative number | Calculator operational | 1. Enter `10 + (-4)` <br> 2. Press `=` | Result displayed: **6** |
| TC-003 | Addition of decimal numbers | Decimal input supported | 1. Enter `2.5 + 3.75` <br> 2. Press `=` | Result displayed: **6.25** |
| TC-004 | Subtraction of positive numbers | Calculator ready | 1. Enter `9 - 4` <br> 2. Press `=` | Result displayed: **5** |
| TC-005 | Subtraction resulting negative | Calculator ready | 1. Enter `3 - 7` <br> 2. Press `=` | Result displayed: **-4** |
| TC-006 | Multiplication of positive numbers | Calculator ready | 1. Enter `6 × 4` <br> 2. Press `=` | Result displayed: **24** |
| TC-007 | Multiplication with negative number | Negative input supported | 1. Enter `-5 × 3` <br> 2. Press `=` | Result displayed: **-15** |
| TC-008 | Multiplication of decimals | Decimal input supported | 1. Enter `1.5 × 2` <br> 2. Press `=` | Result displayed: **3.0** |
| TC-009 | Division of integers | Calculator ready | 1. Enter `12 ÷ 3` <br> 2. Press `=` | Result displayed: **4** |
| TC-010 | Division resulting decimal | Calculator ready | 1. Enter `7 ÷ 2` <br> 2. Press `=` | Result displayed: **3.5** |
| TC-011 | BODMAS precedence | Multi-operator support | 1. Enter `2 + 3 × 4` <br> 2. Press `=` | Result displayed: **14** |
| TC-012 | BODMAS with parentheses | Parentheses supported | 1. Enter `(2 + 3) × 4` <br> 2. Press `=` | Result displayed: **20** |

---

##  Invalid Input Test Cases

| Test Case ID | Test Description | Preconditions | Test Steps | Expected Results |
|---|---|---|---|---|
| TC-013 | Division by zero | Calculator running | 1. Enter `8 ÷ 0` <br> 2. Press `=` | Error message: **Cannot divide by zero** |
| TC-014 | Non-numeric character input | Input field active | 1. Enter `5 + a` <br> 2. Press `=` | Error message: **Invalid input** |
| TC-015 | Unsupported special character | Input field active | 1. Enter `10 + @` <br> 2. Press `=` | Error message displayed |
| TC-016 | Empty input | Calculator ready | 1. Press `=` without entering anything | Message: **No input provided** |
| TC-017 | Multiple operators together | Expression entry allowed | 1. Enter `5 ++ 3` <br> 2. Press `=` | Error message displayed |
| TC-018 | Incomplete expression | Calculator ready | 1. Enter `9 ×` <br> 2. Press `=` | Error message: **Incomplete expression** |

---

##  Notes
- Calculator must support negative and decimal values.
- Operator precedence must follow BODMAS rules.
- All invalid inputs must return meaningful error messages.
