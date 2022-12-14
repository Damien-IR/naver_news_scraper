from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    id: str
    name: str
    oid: str
    url: str


@dataclass
class News:
    """
    한 뉴스에 대한 정보를 포함한 dataclass
    """

    oid: str  # 언론사 고유 ID
    aid: str  # 뉴스 고유 ID
    title: str  # 뉴스 제목
    content: str  # 뉴스 본문
    sid1: str  # 1분류 ID
    sid2: str  # 2분류 ID
    sid3: str  # 3분류 ID
    url: str  # 뉴스 URL
    upload_time: str  # 뉴스 업로드 날짜
    edited_time: str  # 뉴스 수정 날짜 (미 수정 시 upload_date 와 동일)
    press: str  # 언론사
    authors: List[Author]  # 기자
