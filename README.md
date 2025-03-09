
# Testing-code

โปรเจคนี้ประกอบด้วยโซลูชันสำหรับปัญหาต่างๆ จาก HackerRank พร้อมเทสต์เคสเพื่อยืนยันความถูกต้องของโค้ด

## ไฟล์และฟังก์ชันหลัก

### 1. alternating_characters.py

**ฟังก์ชัน:**  `alternatingCharacters(s)`  
**วัตถุประสงค์:**  นับจำนวนตัวอักษรที่ต้องลบออกเพื่อไม่ให้มีตัวอักษรซ้ำกันติดกันในสตริง  
**ตัวอย่าง:**

-   `alternatingCharacters("AAAAA")`  → คืนค่า  `4`  (ลบ 'A' 4 ตัวจาก "AAAAA" ได้ "A")
    
-   `alternatingCharacters("ABABAB")`  → คืนค่า  `0`  (ไม่ต้องลบ)
    

**รันเทสต์:**

```bash
python -m unittest -v tests/test_alternating_characters.py
```
----------

### 2. caesar_cipher_1.py

**ฟังก์ชัน:**  `caesarCipher(s, k)`  
**วัตถุประสงค์:**  เข้ารหัสซีซาร์โดยเลื่อนตัวอักษรตามค่า  `k`  (ตัวอักษรพิเศษและตัวเลขไม่เปลี่ยนแปลง)  
**ตัวอย่าง:**

-   `caesarCipher("abc", 3)`  → คืนค่า  `"def"`
    
-   `caesarCipher("XYZ", 2)`  → คืนค่า  `"ZAB"`
    

**รันเทสต์:**

```bash
python -m unittest -v tests/test_caesar_cipher_1.py
```
----------

### 3. funny_string.py

**ฟังก์ชัน:**  `funnyString(s)`  
**วัตถุประสงค์:**  ตรวจสอบว่าผลต่างของค่า ASCII ระหว่างตัวอักษรติดกันในสตริงตรงกับผลต่างของสตริงที่กลับด้านหรือไม่  
**ผลลัพธ์:**  คืนค่า  `"Funny"`  หรือ  `"Not Funny"`  
**ตัวอย่าง:**

-   `funnyString("acxz")`  →  `"Funny"`
    
-   `funnyString("bcxz")`  →  `"Not Funny"`
    

**รันเทสต์:**

```bash
ppython -m unittest -v tests/test_funny_string.py
```
----------

### 4. grid_challenge.py

**ฟังก์ชัน:**  `gridChallenge(grid)`  
**วัตถุประสงค์:**  ตรวจสอบว่าเมื่อเรียงตัวอักษรในแต่ละแถวของกริดแล้ว ทุกคอลัมน์เรียงตามลำดับหรือไม่  
**ผลลัพธ์:**  คืนค่า  `"YES"`  หรือ  `"NO"`  
**ตัวอย่าง:**

-   กริด  `["abc", "def", "ghi"]`  → คืนค่า  `"YES"`
    
-   กริด  `["xyz", "uvw"]`  → คืนค่า  `"NO"`
    

**รันเทสต์:**

```bash
python -m unittest -v tests/test_grid_challenge.py
```
----------

### 5. two_characters.py

**ฟังก์ชัน:**  `alternate(s)`  
**วัตถุประสงค์:**  หาความยาวสูงสุดของสตริงย่อยที่ประกอบด้วยตัวอักษรสองตัวสลับกันโดยไม่มีตัวติดกัน  
**ตัวอย่าง:**

-   `alternate("ababab")`  → คืนค่า  `6`
    
-   `alternate("abba")`  → คืนค่า  `0`
    

**รันเทสต์:**

```bash
python -m unittest -v tests/test_two_characters.py
```
----------

## ข้อกำหนด

-   Python 3.6 ขึ้นไป
    
-   ไม่ต้องติดตั้งไลบรารีเพิ่มเติม (ใช้โมดูลมาตรฐานของ Python)
    

## การติดตั้งและรัน

1.  โคลนรีโพซิทอรี:
    
    ```bash
    git clone https://github.com/w-kaewthorn14/testing-code.git
    ```
2.  รันเทสต์ทั้งหมด:
    
    ```bash
    python -m unittest discover -s tests
    ```
