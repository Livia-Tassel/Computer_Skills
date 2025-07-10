<center style="font-family: 'Times New Roman', sans-serif; color: orange; font-size: 2em; font-weight: bold">shcircuit</center>
<div style="text-align: right; font-family: 'Times New Roman', serif; font-size: 1em;">Livia Tassel</div>

[TOC]

# 🧠 Python Short-Circuit Logic Summary & Practice

## 📚 Key Concepts

### ✅ `and` Expression
- Syntax: `A and B`
- Behavior:
  - `A` **false**, return `A`
  - `A` **true**, return `B`
>Does **not** force the result to a Boolean — return the actual operand.

### ✅ `or` Expression
- Syntax: `A or B`
- Behavior:
  - `A` **true**, return `A`
  - `A` **false**, return `B`

### ✅ `not` Expression
- Syntax: `not A`
- Behavior: Return `True` if `A` **false**, `False` otherwise.
>`not` is the logical operator that return a **Boolean** value.

### ✅ Falsy Value
- `0`
- `None`
- `False`
- `''`
- `[]`, `{}`, `()`

---

## 💡 Special Notes

| Expression | Explanation |
|------------|-------------|
| `True and 13` | Return `13` |
| `False or 0` | Return `0` |
| `not 10` | Return `False` |
| `not None` | Return `True` |
| `True and 1 / 0` | Raises `Error` |
| `True or 1 / 0` | Return `True` |
