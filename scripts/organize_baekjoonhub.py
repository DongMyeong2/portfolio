#!/usr/bin/env python3
import os, re, shutil, subprocess
from datetime import datetime, timezone, timedelta

# ===== 기본 설정 =====
KST = timezone(timedelta(hours=9))  # Asia/Seoul
# 날짜를 "오늘(KST)"로 찍습니다. (제출/커밋 시간으로 쓰고 싶으면 get_git_date() 사용하도록 바꾸세요)
TODAY = datetime.now(KST).strftime("%Y-%m-%d")

# 최상위 언어 폴더: Python, SQL만 사용
LANG_BY_EXT = {
    ".py": "Python",
    ".sql": "SQL",
}

# 플랫폼 키워드 → 표준 폴더명
PLATFORM_ALIASES = {
    # BOJ/SWEA/Programmers
    "boj": "BOJ", "baekjoon": "BOJ", "백준": "BOJ",
    "swea": "SWEA", "sw expert": "SWEA", "sw expert academy": "SWEA",
    "programmers": "Programmers", "프로그래머스": "Programmers",
    # SQL 플랫폼 추가
    "leetcode": "LeetCode", "leet code": "LeetCode", "lc": "LeetCode", "리트코드": "LeetCode",
    "hackerrank": "HackerRank", "해커랭크": "HackerRank", "hr": "HackerRank",
}

ALLOW_PLATFORMS = {"BOJ", "Programmers", "SWEA", "LeetCode", "HackerRank"}
DEFAULT_PLATFORM = "BOJ"  # 감지 실패 시 기본 플랫폼 (원하면 "Programmers"로 바꾸세요)

IGNORE_DIRS = {".git", ".github", "scripts", ".venv", "venv", "__pycache__"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def detect_language(file):
    return LANG_BY_EXT.get(os.path.splitext(file)[1].lower())

def detect_platform(parts_lower):
    # 경로/파일명 컴포넌트에서 키워드 탐지
    for p in parts_lower:
        for key, name in PLATFORM_ALIASES.items():
            if key in p:
                return name
    return None

def get_git_date(path):
    """
    파일의 마지막 커밋 날짜를 KST YYYY-MM-DD로 반환.
    원하면 TODAY 대신 이 값을 써서 '제출일자≈커밋일자'로 폴더를 만들 수 있습니다.
    """
    try:
        iso = subprocess.check_output(
            ["git", "log", "-1", '--format=%cI', path],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        if iso:
            dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(KST)
            return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    return TODAY

def extract_id_title(path, filename_stem):
    """
    파일명/상위폴더명에서 문제번호와 제목을 추출.
    - 우선 파일명에서 '숫자 + 구분자 + 제목' 패턴을 시도: '12368_제목', '1. Two Sum', '175-Combine Two Tables' 등
    - 실패하면 숫자 없는 제목만 사용
    - 상위폴더가 날짜(YYYY-MM-DD)이면 힌트에서 제외
    """
    parent = os.path.basename(os.path.dirname(path))
    parent_for_hint = parent if not DATE_RE.match(parent) else ""

    # 1) 파일명에서 "앞부분 숫자 + 구분자 + 제목"
    m = re.match(r"^\s*(\d+)[.\s_-]+(.+)$", filename_stem)
    if m:
        pid = m.group(1)
        title = m.group(2)
    else:
        # 2) 부모 폴더명이 날짜가 아니고 "앞부분 숫자 + 구분자 + 제목"이면 활용
        if parent_for_hint:
            m2 = re.match(r"^\s*(\d+)[.\s_-]+(.+)$", parent_for_hint)
        else:
            m2 = None
        if m2:
            pid = m2.group(1)
            # 제목은 파일명/부모 중 더 정보가 많은 쪽을 사용
            title = filename_stem if len(filename_stem) > len(m2.group(2)) else m2.group(2)
        else:
            # 3) 그래도 실패하면 숫자 없이 제목만
            pid = None
            title = filename_stem

    # 제목 정리: 공백->_, 금지문자 제거
    def sanitize(s):
        s = s.strip()
        s = re.sub(r"[\\/:\*\?\"<>\|]", "", s)
        s = re.sub(r"\s+", "_", s)
        return s[:120] if s else "untitled"

    title = sanitize(title)
    return pid, title

def already_organized(parts):
    # <Language>/<Platform>/<YYYY-MM-DD>/filename ?
    if len(parts) < 4: return False
    if parts[0] not in {"Python", "SQL"}: return False
    if parts[1] not in ALLOW_PLATFORMS: return False
    if not DATE_RE.match(parts[2]): return False
    return True

def main():
    repo_root = os.getcwd()
    moves = []

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel_root = os.path.relpath(root, repo_root)
        parts = [] if rel_root == "." else rel_root.split(os.sep)

        for f in files:
            src = os.path.join(root, f)

            lang = detect_language(f)    # Python/SQL만 대상
            if not lang:
                continue

            # 이미 정리된 파일은 스킵
            rel = os.path.relpath(src, repo_root)
            rel_parts = rel.split(os.sep)
            if already_organized(rel_parts):
                continue

            # 플랫폼 추정
            platform = detect_platform([p.lower() for p in parts] + [f.lower()]) or DEFAULT_PLATFORM

            # 파일명에서 문제번호/제목 파싱
            stem, ext = os.path.splitext(f)
            pid, title = extract_id_title(src, stem)
            new_name = f"{pid}_{title}{ext}" if pid else f"{title}{ext}"

            # 날짜(폴더명) 결정: TODAY 사용 (제출/커밋일 쓰려면 아래 줄로 교체)
            date_folder = TODAY
            # date_folder = get_git_date(src)  # 마지막 커밋 일자로 사용하고 싶을 때

            dst = os.path.join(repo_root, lang, platform, date_folder, new_name)

            # 파일명 충돌 방지
            base, ext2 = os.path.splitext(dst)
            k = 1
            while os.path.exists(dst):
                dst = f"{base}__{k}{ext2}"
                k += 1

            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            moves.append((rel, os.path.relpath(dst, repo_root)))

    if moves:
        print("Moved files:")
        for a, b in moves:
            print(f" - {a} -> {b}")
    else:
        print("No files moved.")

if __name__ == "__main__":
    main()
