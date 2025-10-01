#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil
import subprocess
from datetime import datetime, timezone, timedelta

# ===== 기본 설정 =====
KST = timezone(timedelta(hours=9))

# 최상위 언어 폴더: Python, SQL만 사용
LANG_BY_EXT = {
    ".py": "Python",
    ".sql": "SQL",
}

# 정리 대상이 되는 최상위 폴더만 허용 (루트에서 이 폴더들만 순회)
ALLOW_TOP_LANG_DIRS = {"Python", "SQL"}

# 플랫폼 키워드 → 표준 폴더명
PLATFORM_ALIASES = {
    "boj": "BOJ", "baekjoon": "BOJ", "백준": "BOJ",
    "swea": "SWEA", "sw expert": "SWEA", "sw expert academy": "SWEA",
    "programmers": "Programmers", "프로그래머스": "Programmers",
    "leetcode": "LeetCode", "leet code": "LeetCode", "lc": "LeetCode", "리트코드": "LeetCode",
    "hackerrank": "HackerRank", "해커랭크": "HackerRank", "hr": "HackerRank",
    "datalemur": "DataLemur",
}
ALLOW_PLATFORMS = {"BOJ", "SWEA", "Programmers", "LeetCode", "HackerRank"}

IGNORE_DIRS = {".git", ".github", "scripts", ".venv", "venv", "__pycache__"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ===== 헬퍼 =====
def detect_language(file: str) -> str | None:
    return LANG_BY_EXT.get(os.path.splitext(file)[1].lower())


def detect_platform(parts_lower: list[str]) -> str | None:
    # 경로/파일명 컴포넌트에서 키워드 탐지
    for p in parts_lower:
        for key, name in PLATFORM_ALIASES.items():
            if key in p:
                return name
    return None


def git_last_commit_date_kst(path: str) -> str:
    """파일의 마지막 커밋 날짜를 KST YYYY-MM-DD로 반환."""
    try:
        iso = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", path],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        if iso:
            dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(KST)
            return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    return datetime.now(KST).strftime("%Y-%m-%d")


def git_last_commit_message(path: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B", path],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return ""


def extract_id_title(path: str, filename_stem: str, parent_hint: str | None):
    """
    문제번호 & 제목 추출:
    - 파일명 '12345_제목', '12345. 제목', '12345-제목' 우선
    - 실패하면 부모폴더에서 같은 패턴 시도
    - 그래도 실패하면 번호 없음
    """
    def parse(s: str):
        m = re.match(r"^\s*(\d+)[.\s_-]+(.+)$", s)
        if m:
            return m.group(1), m.group(2)
        return None, None

    pid, title = parse(filename_stem)
    if not pid and parent_hint:
        pid2, t2 = parse(parent_hint)
        if pid2:
            pid = pid2
            title = filename_stem if len(filename_stem) > len(t2 or "") else (t2 or filename_stem)

    if not title:
        title = filename_stem

    def sanitize(s: str):
        s = s.strip()
        s = re.sub(r"[\\/:\*\?\"<>\|]", "", s)
        s = re.sub(r"\s+", "_", s)
        return s[:120] if s else "untitled"

    return pid, sanitize(title)


def already_organized_per_problem(rel_parts: list[str]) -> bool:
    """
    우리가 원하는 형태인가?
    Python/BOJ/<문제폴더>/<파일>
    (부모 폴더가 날짜면 "옛 구조"로 판단해 재정리)
    """
    if len(rel_parts) < 4:
        return False
    if rel_parts[0] not in {"Python", "SQL"}:
        return False
    if rel_parts[1] not in ALLOW_PLATFORMS:
        return False
    if DATE_RE.match(rel_parts[-2]):  # 부모가 날짜이면 재정리 대상
        return False
    return True


def read_top_comment_block(src_path: str) -> str:
    """
    소스 파일 상단의 주석 블록을 README로 옮기기 위해 추출 (# 또는 '''...''')
    (README가 없을 때만 사용)
    """
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return ""

    # triple quote 우선
    tq = re.search(r'^\s*(?:[ruRU]{0,2})("""|\'\'\')(.*?)\1', text, re.S | re.M)
    if tq:
        return tq.group(2).strip()

    # 연속 # 블록
    lines = []
    for line in text.splitlines():
        if re.match(r'^\s*#', line):
            lines.append(re.sub(r'^\s*#\s?', '', line))
        elif not line.strip():  # 빈 줄은 주석 블록에 포함
            if lines:
                lines.append("")
        else:
            break
    return "\n".join(lines).strip()


def ensure_readme(dst_dir: str, platform: str, pid: str | None, title: str,
                  solved_date: str, lang: str, src_path: str):
    """
    README가 없을 때만 생성. (있으면 건드리지 않음)
    """
    readme = os.path.join(dst_dir, "README.md")
    if os.path.exists(readme):
        return

    meta = git_last_commit_message(src_path)
    m_time = re.search(r"Time:\s*([0-9]+)\s*ms", meta)
    m_mem = re.search(r"Memory:\s*([0-9]+)\s*KB", meta)

    note = read_top_comment_block(src_path)

    problem_url = ""
    if platform == "BOJ" and pid:
        problem_url = f"https://www.acmicpc.net/problem/{pid}"

    lines = []
    lines.append(f"# {pid+' ' if pid else ''}{title}")
    lines.append("")
    lines.append(f"- **Platform**: {platform}")
    lines.append(f"- **Solved date**: {solved_date} (KST)")
    lines.append(f"- **Language**: {lang}")
    if problem_url:
        lines.append(f"- **Link**: {problem_url}")
    if m_time or m_mem:
        perf = []
        if m_time: perf.append(f"{m_time.group(1)} ms")
        if m_mem:  perf.append(f"{m_mem.group(1)} KB")
        lines.append(f"- **Perf**: {', '.join(perf)}")
    lines.append("")
    lines.append("## Notes")
    lines.append(note if note else "_(no notes)_")
    lines.append("")

    with open(readme, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def move_sidecar_readme(src_dir: str, dst_dir: str) -> bool:
    """
    소스가 있던 폴더(src_dir)에 README가 있으면 그대로 dst_dir로 이동.
    있으면 True, 없으면 False.
    """
    for name in ("README.md", "Readme.md", "readme.md"):
        cand = os.path.join(src_dir, name)
        if os.path.exists(cand):
            os.makedirs(dst_dir, exist_ok=True)
            dst = os.path.join(dst_dir, "README.md")
            if not os.path.exists(dst):  # 대상에 없을 때만 이동
                shutil.move(cand, dst)
            return True
    return False


# ===== 메인 =====
def main():
    repo_root = os.getcwd()
    moves: list[tuple[str, str]] = []

    for root, dirs, files in os.walk(repo_root):
        rel_root = os.path.relpath(root, repo_root)

        # 루트에서는 ALLOW_TOP_LANG_DIRS 만 내려가도록 제한
        if rel_root == ".":
            dirs[:] = [d for d in dirs if d in ALLOW_TOP_LANG_DIRS]
        else:
            # 그 외 위치에서는 무시 디렉토리 제외
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        parts = [] if rel_root == "." else rel_root.split(os.sep)

        for f in files:
            src = os.path.join(root, f)

            # 파일 단위 가드: 루트 기준 첫 컴포넌트가 Python/ 또는 SQL/인 파일만 대상
            rel_parts = os.path.relpath(src, repo_root).split(os.sep)
            if len(rel_parts) < 2 or rel_parts[0] not in ALLOW_TOP_LANG_DIRS:
                continue

            lang = detect_language(f)
            if not lang:
                continue  # Python/SQL 이외 스킵

            if already_organized_per_problem(rel_parts):
                continue  # 이미 새 구조

            # 플랫폼 추정
            platform = detect_platform([p.lower() for p in parts] + [f.lower()]) or "BOJ"

            # 문제번호/제목 추출
            parent_hint = parts[-1] if parts else None
            pid, title = extract_id_title(src, os.path.splitext(f)[0], parent_hint)

            # 제출일(커밋일자) 보존
            solved_date = git_last_commit_date_kst(src)

            # 대상 디렉토리: Python/<Platform>/<문제폴더>/
            folder_name = f"{pid}_{title}" if pid else title
            dst_dir = os.path.join(repo_root, lang, platform, folder_name)
            os.makedirs(dst_dir, exist_ok=True)

            # 파일명 충돌 방지
            dst = os.path.join(dst_dir, f)
            base, ext2 = os.path.splitext(dst)
            k = 1
            while os.path.exists(dst):
                dst = f"{base}__{k}{ext2}"
                k += 1

            # 실제 이동
            src_dir = os.path.dirname(src)  # 이동 전 원본 폴더
            shutil.move(src, dst)

            # (A방법) 원본 폴더에 README가 있으면 그대로 이동, 없으면 새로 생성
            moved_readme = move_sidecar_readme(src_dir, dst_dir)
            if not moved_readme:
                ensure_readme(dst_dir, platform, pid, title, solved_date, lang, dst)

            moves.append((
                os.path.relpath(src, repo_root),
                os.path.relpath(dst, repo_root)
            ))

    if moves:
        print("Moved files:")
        for a, b in moves:
            print(f" - {a} -> {b}")
    else:
        print("No files moved.")


if __name__ == "__main__":
    main()
