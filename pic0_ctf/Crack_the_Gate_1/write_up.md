# Pico challenge: Crack the Gate #
### Level: <span style="color:green">Easy</span>

## Challenge Description

*We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: **ctf-player@picoctf.org.**  Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?
Additional details will be available after launching your challenge instance.*

## Solution

Đầu tiên, ta truy cập vào trang web được cung cấp trong challenge. Sau đấy thấy được một dòng comment được required là phải xoá rồi mới push lên production được (quên chụp =V) -> ta có thể đoán được rằng có thể có một số thông tin ẩn trong comment, nên ta có thể thử paste dòng comment vào trang ceasar cipher để giải mã thử.

![cipher_hint_1](./image/image_1.jpg)

Sau khi thư shift tầm 13 ta thu được đoạn text như sau (nó thường được gọi là ROT13):

![cipher_hint_2](./image/image_2.jpg)

Ta có thể thấy một đoạn temporary bypass login được user tên Jack cấp cho ctf-player, chỉ cần paste đoạn "X-Dev-Accesss = Yes" vào header của request là có thể bypass được login.

--->
Dùng Burp Suite để chèn cái đoạn:

![cipher_hint_3](./image/image_3.jpg)

Sau khi chèn xong ta gửi request và nhận được response:

![cipher_hint_5](./image/image_5.jpg)

**FLAG: picoCTF{brut4_f0rc4_b3a957eb}**








