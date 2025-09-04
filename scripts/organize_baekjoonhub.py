#!/usr/bin/env python3
import os, re, shutil, subprocess
from datetime import datetime, timezone, timedelta

# ===== 공통 =====
KST = timezone(timedelta(hours=9))
LANG_BY_EXT = {".py": "Python", ".sql": "SQL"}

PLATFORM_ALIASES = {
    "boj":"BOJ","baekjoon":"BOJ","백준":"BOJ",
    "swea":"SWEA","sw expert":"SWEA","sw expert academy":"SWEA",
    "programmers":"Programmers","프로그래머스":"Programmers",
    "leetcode":"LeetCode","leet code":"LeetCode","lc":"LeetCode","리트코드":"LeetCode",
    "hackerrank":"HackerRank","해커랭크":"HackerRank","hr":"HackerRank",
}
ALLOW_PLATFORMS = {"BOJ","SWEA","Programmers","LeetCode","HackerRank"}

IGNORE_DIRS = {".git",".github","scripts",".venv","venv","__pycache__"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def detect_language(file):
    return LANG_BY_EXT.get(os.path.splitext(file)[1].lower())

def detect_platform(parts_lower):
    for p in parts_lower:
        for key, name in PLATFORM_ALIASES.items():
            if key in p:
                return name
    return None

def git_last_commit_date_kst(path):
    """파일의 마지막 커밋 날짜(KST, YYYY-MM-DD)"""
    try:
        iso = subprocess.check_output(
            ["git","log","-1","--format=%cI", path],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        if iso:
            dt = datetime.fromisoformat(iso.replace("Z","+00:00")).astimezone(KST)
            return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    # 기록이 없으면 오늘
    return datetime.now(KST).strftime("%Y-%m-%d")

def git_last_commit_message(path):
    try:
        msg = subprocess.check_output(
            ["git","log","-1","--pretty=%B", path],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return msg
    except Exception:
        return ""

def extract_id_title(path, filename_stem, parent_hint: str | None):
    """
    문제번호 & 제목 추출:
    - 파일명 '12345_제목', '12345. 제목', '12345-제목' 우선
    - 실패하면 부모폴더에서 같은 패턴 시도
    - 그래도 실패하면 번호 없음
    """
    def parse(s):
        m = re.match(r"^\s*(\d+)[.\s_-]+(.+)$", s)
        if m: return m.group(1), m.group(2)
        return None, None

    pid, title = parse(filename_stem)
    if not pid and parent_hint:
        pid, pt = parse(parent_hint)
        if pid:
            title = filename_stem if len(filename_stem) > len(pt) else pt
    if not title:
        title = filename_stem

    def sanitize(s):
        s = s.strip()
        s = re.sub(r"[\\/:\*\?\"<>\|]", "", s)
        s = re.sub(r"\s+", "_", s)
        return s[:120] if s else "untitled"

    return pid, sanitize(title)

def already_organized_per_problem(rel_parts):
    """
    우리가 원하는 형태인가?
    Python/BOJ/<문제폴더>/<파일>
    (부모 폴더가 날짜가 아니어야 함)
    """
    if len(rel_parts) < 4: return False
    if rel_parts[0] not in {"Python","SQL"}: return False
    if rel_parts[1] not in ALLOW_PLATFORMS: return False
    # 부모 폴더가 날짜면 "옛 구조"로 보고 재정리
    if DATE_RE.match(rel_parts[-2]): return False
    return True

def read_top_comment_block(src_path):
    """
    소스 파일 상단의 주석 블록을 README로 옮기기 위해 추출 (# 또는 '''...''')
    """
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
    except:
        return ""

    # triple quote 우선
    tq = re.search(r'^\s*(?:[ruRU]{0,2})("""|\'\'\')(.*?)\1', text, re.S|re.M)
    if tq:
        return tq.group(2).strip()

    # 연속 # 블록
    lines = []
    for line in text.splitlines():
        if re.match(r'^\s*#', line):
            lines.append(re.sub(r'^\s*#\s?', '', line))
        elif not line.strip():   # 빈 줄은 주석 블록에 포함
            if lines: lines.append("")
        else:
            break
    return "\n".join(lines).strip()

def ensure_readme(dst_dir, platform, pid, title, solved_date, lang, src_path):
    readme = os.path.join(dst_dir, "README.md")
    if os.path.exists(readme):
        return  # 이미 있으면 보존

    meta = git_last_commit_message(src_path)
    # BaekjoonHub 기본 커밋 메시지에서 Time/Memory 대충 파싱
    m_time = re.search(r"Time:\s*([0-9]+)\s*ms", meta)
    m_mem  = re.search(r"Memory:\s*([0-9]+)\s*KB", meta)

    note = read_top_comment_block(src_path)

    problem_url = ""
    if platform == "BOJ" and pid:
        problem_url = f"https://www.acmicpc.net/problem/{pid}"

    contents = []
    contents.append(f"# {pid+' ' if pid else ''}{title}")
    contents.append("")
    contents.append(f"- **Platform**: {platform}")
    contents.append(f"- **Solved date**: {solved_date} (KST)")
    contents.append(f"- **Language**: {lang}")
    if problem_url:
        contents.append(f"- **Link**: {problem_url}")
    if m_time or m_mem:
        tm = []
        if m_time: tm.append(f"{m_time.group(1)} ms")
        if m_mem:  tm.append(f"{m_mem.group(1)} KB")
        contents.append(f"- **Perf**: {', '.join(tm)}")
    contents.append("")
    contents.append("## Notes")
    contents.append(note if note else "_(no notes)_")
    contents.append("")
    with open(readme, "w", encoding="utf-8") as f:
        f.write("\n".join(contents))

def main():
    repo_root = os.getcwd()
    moves = []

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel_root = os.path.relpath(root, repo_root)
        parts = [] if rel_root == "." else rel_root.split(os.sep)

        for f in files:
            src = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()

            lang = detect_language(f)
            if not lang:
                continue

            rel_parts = os.path.relpath(src, repo_root).split(os.sep)
            if already_organized_per_problem(rel_parts):
                continue  # 이미 우리가 원하는 형태

            # 플랫폼 추정
            platform = detect_platform([p.lower() for p in parts] + [f.lower()]) or "BOJ"

            # 문제번호/제목
            parent_hint = parts[-1] if parts else None
            pid, title = extract_id_title(src, os.path.splitext(f)[0], parent_hint)

            # 제출일(커밋일자) 보존
            solved_date = git_last_commit_date_kst(src)

            # 대상 경로: Python/<Platform>/<문제번호_제목>/
            folder_name = f"{pid}_{title}" if pid else title
            dst_dir = os.path.join(repo_root, lang, platform, folder_name)
            os.makedirs(dst_dir, exist_ok=True)

            # 파일명 충돌 방지: 동일 이름이 있으면 __1, __2 …
            dst = os.path.join(dst_dir, f)
            base, ext2 = os.path.splitext(dst)
            k = 1
            while os.path.exists(dst):
                dst = f"{base}__{k}{ext2}"
                k += 1

            shutil.move(src, dst)
            ensure_readme(dst_dir, platform, pid, title, solved_date, lang, dst)

            moves.append((os.path.relpath(src, repo_root), os.path.relpath(dst, repo_root)))

    if moves:
        print("Moved files:")
        for a, b in moves:
            print(f" - {a} -> {b}")
    else:
        print("No files moved.")

if __name__ == "__main__":
    main()
