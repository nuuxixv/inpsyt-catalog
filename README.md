# 📚 2026 인싸이트 카탈로그 뷰어

> **PDF의 한계를 넘어선 차세대 디지털 카탈로그 경험**\
> 대용량 PDF를 WebP 이미지로 변환하고, 반응형 웹 뷰어로 구현한 고성능 카탈로그
> 솔루션

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge)](https://your-github-pages-url.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🎯 프로젝트 개요

### 문제 상황 (Problem)

기존 PDF 기반 카탈로그는 다음과 같은 문제점을 가지고 있었습니다:

- **높은 이탈률**: 대용량 PDF 다운로드로 인한 긴 로딩 시간 (사용자의 53%가 3초
  이상 대기 시 이탈)
- **낮은 모바일 접근성**: PDF는 모바일 환경에서 다운로드 및 열람이 불편
- **검색 불가**: 기존 PDF는 텍스트 검색이 어려워 정보 접근성 저하
- **높은 서버 비용**: 대용량 파일 호스팅 및 전송 비용 부담

### 해결 방법 (Solution)

**1. 이미지 경량화 및 최적화**

- PDF를 WebP 포맷으로 변환하여 파일 크기 70% 감소
- Lazy Loading 적용으로 초기 로딩 속도 획기적 개선
- 점진적 이미지 로딩으로 체감 속도 향상

**2. 반응형 디자인**

- **Mobile**: 웹툰형 세로 스크롤 방식으로 직관적인 탐색
- **PC/Tablet**: 실제 책을 넘기는 듯한 듀얼 뷰 모드
- 모든 디바이스에 최적화된 유연한 레이아웃

**3. 탐색 편의성 강화**

- OCR 기반 전문 텍스트 검색 기능
- 계층형 목차(TOC)로 빠른 페이지 이동
- 퀵링크 기능으로 주요 섹션 즉시 접근

### 기대 효과 및 성과 (Impact)

✅ **사용자 경험(UX) 혁신**: 디바이스별 최적화된 인터페이스로 콘텐츠 몰입도 및
체류 시간 증대\
✅ **접근성 극대화**: 별도 앱 설치 없이 URL 클릭만으로 즉시 열람 가능\
✅ **운영 효율성 확보**: GitHub Pages 활용으로 서버 비용 무료, 유지보수 용이\
✅ **검색 가능성**: OCR 텍스트 데이터로 정보 검색 및 접근성 향상

---

## ✨ 주요 기능

### 📖 뷰어 기능

- **듀얼 뷰 모드**: PC에서 실제 책처럼 2페이지 동시 보기
- **싱글 뷰 모드**: 한 페이지씩 집중해서 보기
- **세로 스크롤 모드**: 모바일에서 웹툰처럼 연속 스크롤
- **확대/축소**: 마우스 휠 또는 버튼으로 자유로운 줌 조절
- **전체화면 모드**: 몰입형 읽기 경험 제공

### 🔍 검색 및 탐색

- **전문 텍스트 검색**: OCR 추출 텍스트 기반 실시간 검색
- **검색 결과 하이라이트**: 검색어가 포함된 페이지 미리보기
- **계층형 목차(TOC)**: 카테고리별 그룹화된 목차 구조
- **퀵링크**: 주요 섹션으로 빠른 이동
- **페이지 점프**: 직접 페이지 번호 입력으로 이동

### 🎨 사용자 인터페이스

- **썸네일 바**: 전체 페이지 미리보기 및 빠른 탐색
- **반응형 툴바**: 디바이스별 최적화된 컨트롤
- **키보드 단축키**: 화살표 키로 페이지 이동
- **터치 제스처**: 모바일에서 스와이프 지원
- **다크 모드 대응**: 시스템 테마 자동 감지

### 📱 모바일 최적화

- **세로 스크롤 레이아웃**: 자연스러운 모바일 읽기 경험
- **터치 친화적 UI**: 큰 버튼과 제스처 지원
- **성능 최적화**: 모바일 환경에서도 부드러운 스크롤
- **오프라인 지원**: 한 번 로드된 페이지는 캐시 활용

---

## 🛠 기술 스택

### Frontend

- **HTML5**: 시맨틱 마크업 및 접근성 준수
- **CSS3**: CSS Variables, Flexbox, Grid, Media Queries
- **Vanilla JavaScript (ES6+)**: 프레임워크 없는 순수 자바스크립트
- **Material Symbols**: Google Material Icons 아이콘 시스템

### 이미지 처리

- **WebP**: 차세대 이미지 포맷 (PNG 대비 70% 용량 감소)
- **Lazy Loading**: Intersection Observer API 활용
- **Python (pdf2image)**: PDF → 이미지 변환 스크립트

### 데이터 구조

- **JSON**: 페이지 메타데이터 및 OCR 텍스트 저장
  - `pages.json`: 전체 페이지 정보 (제목, 노트, 텍스트)
  - `quicklinks.json`: 주요 섹션 퀵링크 데이터

### 배포

- **GitHub Pages**: 정적 사이트 호스팅 (무료)
- **Git**: 버전 관리

---

## 🎨 디자인 시스템

### 컬러 팔레트

```css
:root {
    --primary: #2c3e50; /* 주요 색상 (헤더, 버튼) */
    --accent: #3498db; /* 강조 색상 (활성 상태) */
    --bg: #f8f9fa; /* 배경 색상 */
    --sidebar-bg: #ffffff; /* 사이드바 배경 */
    --text: #333; /* 기본 텍스트 */
    --border: #e0e0e0; /* 테두리 색상 */
}
```

### 레이아웃 변수

```css
:root {
    --toolbar-height: 60px; /* 툴바 높이 */
    --thumb-height: 120px; /* 썸네일 바 높이 */
}

/* 모바일 */
@media (max-width: 768px) {
    :root {
        --toolbar-height: 56px;
        --thumb-height: 100px;
    }
}
```

### 반응형 브레이크포인트

| 디바이스 | 너비         | 레이아웃                      |
| -------- | ------------ | ----------------------------- |
| Mobile   | ~768px       | 세로 스크롤, 단일 컬럼        |
| Tablet   | 769px~1024px | 듀얼 뷰 가능, 축소된 사이드바 |
| Desktop  | 1025px~      | 전체 기능, 넓은 뷰어          |

---

## 📝 타이포그래피

### 폰트 패밀리

```css
body {
    font-family:
        "Pretendard", -apple-system, BlinkMacSystemFont, system-ui, Roboto,
        sans-serif;
}
```

- **Pretendard**: 한글 최적화 시스템 폰트
- **System Fonts**: OS별 네이티브 폰트 폴백

### 아이콘

```html
<!-- Material Symbols Outlined -->
<link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
/>
```

---

## 📁 프로젝트 구조

```
Catalog/
├── index.html                    # 메인 HTML 파일
├── pages.json                    # 페이지 메타데이터 (OCR 텍스트 포함)
├── quicklinks.json               # 퀵링크 데이터
├── webp/                         # WebP 이미지 폴더
│   ├── inpsyt_2026Catalog_001.webp
│   ├── inpsyt_2026Catalog_002.webp
│   └── ... (총 184개 페이지)
├── 2026 인싸이트 카달로그.pdf   # 원본 PDF (참고용)
├── 2026_catalog_text.txt         # OCR 추출 원본 텍스트
├── convert_pdf_to_webp.py        # PDF → WebP 변환 스크립트
├── make_pages_json.py            # pages.json 생성 스크립트
├── update_quicklinks.py          # quicklinks.json 업데이트 스크립트
├── fix_filenames.py              # 파일명 정규화 스크립트
├── .nojekyll                     # GitHub Pages Jekyll 비활성화
├── .gitignore                    # Git 제외 파일 목록
└── README.md                     # 프로젝트 문서 (이 파일)
```

### 주요 파일 설명

#### `index.html`

- 단일 HTML 파일에 모든 기능 포함
- 인라인 CSS 및 JavaScript로 구성
- 외부 의존성 최소화 (Material Icons만 CDN 사용)

#### `pages.json`

```json
[
    {
        "page": 1,
        "title": "인싸이트 심리검사연구소",
        "note": "2026 2026 인싸이트는 신뢰를 최우선의 가치로 생각합니다.",
        "file": "inpsyt_2026Catalog_001.webp",
        "text": "인싸이트 심리검사연구소\n2026..."
    }
]
```

#### `quicklinks.json`

```json
[
    {
        "title": "지능·인지능력 검사",
        "items": [
            { "name": "K-WISC-V", "page": 26 },
            { "name": "K-WPPSI-IV", "page": 27 }
        ]
    }
]
```

---
