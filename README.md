![Image](https://github.com/user-attachments/assets/fce71699-0fd9-47da-a567-d5344f8f64d5)

---

### 📥 요구사항

## Installation
Python 3.4+  
```bash
https://www.python.org/downloads/
```
### Pip
```bash
python3 -m pip install -U gallery-dl
```
---

### 🔧 변경사항

※ webp > jpg 강제 변환 기능 제거  
※ +url/-url 기능 추가  
※ 파일 이름 미리 설정 (ex:{파일이름}_1.jpg..) 이런 형식  
※ 에러시 3번 재시도  
※ config.json 샘플 파일 수정  
※ 암튼 여러개 수정하고 추가함...

---

### ⚙️ config.json 설정법
`config.json`에 있는 내용을 전체 선택 후  
`C:\\Users\\계정폴더\\gallery-dl\\config.json` 에 덮어쓰기 하면 됩니다.  
(※ `config 열기` 버튼 클릭 후 거기에 넣으면 됨)  
*안해도 됨, 그냥 사용해도 됨*

`config`은 본인이 스스로 알아서 수정하는 방법 밖에 없음...  
gallery-dl --list-keywords (url) > cmd 명령어 실행

```bash
gallery-dl --list-keywords (url)
```
