---
name: leetcode-prepare
description: >-
  Use this skill when the user (Đình) asks to prepare, set up, or scaffold a new LeetCode problem,
  or requests the next daily challenge workspace before starting to code.
---

# LeetCode Workspace Preparation Skill

This skill automates the creation and setup of problem directories and boilerplate files, eliminating manual scaffolding so the candidate can focus immediately on problem-solving.

---

## Workspace Layout Conventions

1. **Batch Directories:**
   - Problems 1 to 100: `problems-from-1-to-100/`
   - Problems 101 to 200: `problems-from-101-to-200/`
   - Problems 201 to 300: `problems-from-201-to-300/`
2. **Problem Directory Naming:**
   - Zero-padded for numbers under 100: `problem-01`, `problem-02`, ..., `problem-99`, `problem-100`.
   - Direct format for 101+: `problem-101`, `problem-102`, etc.
3. **Required Files per Problem:**
   - `README.md`: Contains problem statement, LeetCode link, constraints, and representative examples.
   - `Solution.java`: Clean Java 17 solution class with appropriate package and method signature. **NO `main` method** (the candidate runs directly on LeetCode).
   - `explain.md`: Empty template with 5 structured Vietnamese sections ready to be populated after the interview defense.
4. **Markdown Formatting Rule:**
   - NEVER use emojis or graphical icons in any markdown files across the workspace.

---

## Execution Steps

When the candidate requests to prepare a problem (e.g., *"Hôm nay làm bài tiếp theo nhé"* or *"Chuẩn bị bài 2 Add Two Numbers"*):

### Step 1: Identify Problem Details
* Determine the problem number:
  - If specified by the candidate (e.g. LeetCode #2), use that number.
  - If not specified, inspect existing folders and select the next sequential number.
* Identify title, slug, difficulty (Easy / Medium / Hard), and pattern (e.g., Two Pointers, Linked List, Sliding Window).

### Step 2: Scaffold Files
Run the built-in scaffolding script:
```bash
python3 scripts/prepare.py --num <NUMBER> --title "<TITLE>" --slug "<SLUG>" --diff "<DIFFICULTY>" --pattern "<PATTERN>"
```
Or create the directory and the 3 standard files directly.

### Step 3: Populate Problem README.md
Ensure `README.md` contains accurate problem details:
- Problem title and LeetCode link.
- Difficulty and Topic/Pattern.
- Input / Output examples.
- Constraints and any follow-up question.

### Step 4: Update Master Progress Tracker
Add a new row to the table in the root `README.md` with:
- Problem number
- Problem title with markdown link
- Topic / Pattern
- Difficulty
- Links to `Solution.java` and `explain.md`
- Status: `In Progress`

### Step 5: Present the Workspace to the Candidate
Provide clickable links to:
- `Solution.java`
- `README.md`
Give a 1-sentence thought-provoking prompt about the core challenge of the problem to initiate the session.
