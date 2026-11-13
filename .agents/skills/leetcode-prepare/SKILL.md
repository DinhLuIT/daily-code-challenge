---
name: leetcode-prepare
description: >-
  Use this skill when the user (Đình) asks to prepare, set up, or scaffold a new LeetCode problem,
  or requests the next daily challenge workspace before starting to code.
---

# LeetCode Workspace Preparation Skill

This skill handles the verification, gathering of problem details, and automated setup of problem directories and boilerplate files. It strictly prohibits creating empty or placeholder files.

---

## Workspace Layout Conventions

1. **Batch Directories:**
   - Problems 1 to 100: `problems-from-1-to-100/`
   - Problems 101 to 200: `problems-from-101-to-200/`
   - Problems 201 to 300: `problems-from-201-to-300/`
2. **Problem Directory Naming & Sequential Challenge Indexing:**
   - Problem numbers (`problem-01`, `problem-02`, ...) represent the **sequential challenge index of Đình's daily journey** (e.g., Challenge #01, Challenge #02, ...), **NOT** the LeetCode question ID!
   - Always determine the next challenge index by finding the current highest `problem-XX` across the workspace and adding 1 (e.g., after `problem-01`, the next challenge is `problem-02`, regardless of whether the LeetCode problem ID is #242, #704, etc.).
   - Zero-padded for numbers under 100: `problem-01`, `problem-02`, ..., `problem-99`, `problem-100`.
   - Direct format for 101+: `problem-101`, `problem-102`, etc.
   - The actual LeetCode problem ID (e.g., LeetCode 242) is documented inside the problem's `README.md`, `Solution.java`, `explain.md`, and the batch tracker table.
3. **Required Files per Problem:**
   - `README.md`: Must contain the complete, real problem statement, LeetCode link, constraints, and representative examples.
   - `Solution.java`: Clean Java 17 solution class with the exact LeetCode method signature. **NO `main` method** (the candidate runs directly on LeetCode).
   - `explain.md`: Structured template in Vietnamese with the 5 standard sections, ready to be populated after the interview defense.
4. **Markdown Formatting Rule:**
   - NEVER use emojis or graphical icons in any markdown files across the workspace.

---

## Execution Protocol

### Step 1: Pre-Flight Check & User Confirmation (Mandatory)

> [!IMPORTANT]
> **Never scaffold blind placeholders.** If the problem title, number, or URL is ambiguous, missing, or unspecified, stop and ask the candidate first.

1. **Check Input Completeness:**
   - Did the candidate provide a specific LeetCode URL, problem name, or problem number?
2. **Handle Incomplete / Vague Prompts (e.g. "Làm bài tiếp theo nhé", "Chuẩn bị bài mới"):**
   - **Do NOT** create folders with generic placeholder text.
   - Either ask the candidate:
     *"Which LeetCode problem do you want to tackle? Please provide the title or URL."*
   - Or, if the candidate wants a recommendation from the roadmap, propose 1-2 curated candidates matching their current pattern (e.g., Two Pointers -> *Valid Palindrome*, *Two Sum II*):
     *"For the next problem in the Arrays & Hashing roadmap, I recommend LeetCode #217: Contains Duplicate or LeetCode #242: Valid Anagram. Which one would you like to prepare?"*
   - Wait for the candidate's confirmation before creating files.

### Step 2: Fetch Accurate Problem Specifications
Once the problem is confirmed, obtain:
* Exact LeetCode title, problem number, and canonical URL.
* Difficulty rating (Easy, Medium, Hard).
* Algorithmic pattern / topic category.
* Complete problem statement, constraints, and sample test cases.
* Official LeetCode Java class and method signature.

### Step 3: Scaffold Problem Workspace
Create the problem folder and all 3 files with complete information:
1. **`README.md`**: Complete problem description with examples and constraints.
2. **`Solution.java`**: Package declaration and boilerplate class with the correct method signature and parameter types.
3. **`explain.md`**: Structured 5-section skeleton for post-interview documentation.

### Step 4: Update Batch Progress Tracker
Add or update the row in the corresponding batch tracker (`problems-from-X-to-Y/README.md`) table with:
- Problem number
- Problem title with markdown link
- Topic / Pattern
- Difficulty
- Links to `Solution.java` and `explain.md`
- Status: `In Progress`

### Step 5: Brief the Candidate
Present clickable links to:
- `Solution.java`
- `README.md`
Deliver a concise 1-sentence prompt focusing on the key constraint or invariant to jumpstart the candidate's thinking.
