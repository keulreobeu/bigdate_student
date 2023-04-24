html = \
"""
<html>
<head>
    <title>제목</title>
</head>
<body>
    냉무
</body>
</html>
"""
byte_html = html.encode('euc-kr')
print(byte_html)



print(byte_html.decode('euc-kr'))