#!/usr/bin/env python3
import sys
import os
import argparse
import re

def get_next_problem_number(workspace_root):
    max_num = 0
    pattern = re.compile(r"problem-(\d+)")
    for root, dirs, _ in os.walk(workspace_root):
        for d in dirs:
            match = pattern.match(d)
            if match:
                num = int(match.group(1))
                if num > max_num:
                    max_num = num
    return max_num + 1

def scaffold_problem(workspace_root, problem_num, title, slug, difficulty, pattern):
    start = ((problem_num - 1) // 100) * 100 + 1
    end = start + 99
    batch_dir = f"problems-from-{start}-to-{end}"
    prob_dir_name = f"problem-{problem_num:02d}" if problem_num < 100 else f"problem-{problem_num}"
    
    full_prob_dir = os.path.join(workspace_root, batch_dir, prob_dir_name)
    os.makedirs(full_prob_dir, exist_ok=True)
    
    # 1. README.md
    readme_path = os.path.join(full_prob_dir, "README.md")
    if not os.path.exists(readme_path):
        lc_url = f"https://leetcode.com/problems/{slug}/" if slug else "https://leetcode.com/problems/"
        readme_content = f"""# LeetCode {problem_num:02d}: {title}

- **Liên kết bài toán:** [{slug or title}]({lc_url})
- **Độ khó:** {difficulty}
- **Chủ đề:** {pattern}

---

## 1. Yêu Cầu Đề Bài

(Điền mô tả đề bài toán ở đây)

---

## 2. Ví Dụ

### Ví dụ 1:
```text
Input: 
Output: 
Giải thích: 
```

---

## 3. Ràng Buộc (Constraints)

* 
"""
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

    # 2. Solution.java
    pkg_name = f"{batch_dir.replace('-', '_')}.{prob_dir_name.replace('-', '_')}"
    solution_path = os.path.join(full_prob_dir, "Solution.java")
    if not os.path.exists(solution_path):
        solution_content = f"""package {pkg_name};

class Solution {{
    // TODO: Implement solution for LeetCode {problem_num:02d} ({title})
}}
"""
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(solution_content)

    # 3. explain.md
    explain_path = os.path.join(full_prob_dir, "explain.md")
    if not os.path.exists(explain_path):
        explain_content = f"""# LeetCode {problem_num:02d}: {title}

## 1. Mô tả bài toán
(Sẽ được cập nhật sau buổi vấn đáp phỏng vấn)

## 2. Ý tưởng cốt lõi (Intuition)
(Sẽ được cập nhật sau buổi vấn đáp phỏng vấn)

## 3. Giải thích thuật toán từng bước
(Sẽ được cập nhật sau buổi vấn đáp phỏng vấn)

## 4. Độ phức tạp (Complexity Analysis)
- Thời gian (Time Complexity): O(...)
- Không gian (Space Complexity): O(...)

## 5. Code hoàn chỉnh & Lưu ý tránh bẫy
(Sẽ được cập nhật sau buổi vấn đáp phỏng vấn)
"""
        with open(explain_path, "w", encoding="utf-8") as f:
            f.write(explain_content)

    # 4. Update root README.md tracker if needed
    root_readme = os.path.join(workspace_root, "README.md")
    if os.path.exists(root_readme):
        with open(root_readme, "r", encoding="utf-8") as f:
            root_content = f.read()
        row_signature = f"| {problem_num:02d} |"
        if row_signature not in root_content and "| :-: | :--- |" in root_content:
            rel_sol = f"./{batch_dir}/{prob_dir_name}/Solution.java"
            rel_exp = f"./{batch_dir}/{prob_dir_name}/explain.md"
            lc_link = f"[{title}](https://leetcode.com/problems/{slug}/)" if slug else title
            new_row = f"| {problem_num:02d} | {lc_link} | {pattern} | {difficulty} | [Solution.java]({rel_sol}) | [explain.md]({rel_exp}) | In Progress |\n"
            # Insert after the last table header separator or after the last row
            root_content = root_content.replace(
                "| :-: | :--- | :--- | :-: | :-: | :-: | :-: |\n",
                f"| :-: | :--- | :--- | :-: | :-: | :-: | :-: |\n{new_row}"
            )
            with open(root_readme, "w", encoding="utf-8") as f:
                f.write(root_content)

    print(f"Created problem {problem_num} at: {full_prob_dir}")
    print(f"  - {readme_path}")
    print(f"  - {solution_path}")
    print(f"  - {explain_path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new LeetCode challenge folder and files.")
    parser.add_argument("--num", type=int, help="Problem number (e.g. 2)")
    parser.add_argument("--title", type=str, default="", help="Problem title (e.g. 'Add Two Numbers')")
    parser.add_argument("--slug", type=str, default="", help="LeetCode slug (e.g. 'add-two-numbers')")
    parser.add_argument("--diff", type=str, default="Medium", choices=["Easy", "Medium", "Hard"], help="Difficulty")
    parser.add_argument("--pattern", type=str, default="Algorithms", help="Algorithmic pattern or topic")
    
    args = parser.parse_args()
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    prob_num = args.num if args.num is not None else get_next_problem_number(workspace_root)
    title = args.title if args.title else f"Problem {prob_num}"
    slug = args.slug if args.slug else title.lower().replace(" ", "-")
    
    scaffold_problem(workspace_root, prob_num, title, slug, args.diff, args.pattern)

if __name__ == "__main__":
    main()
