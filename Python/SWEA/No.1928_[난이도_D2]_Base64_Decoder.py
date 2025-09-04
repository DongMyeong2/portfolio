def base64_decode(encoded_str):
    # Base64 인코딩 테이블
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # 인코딩된 문자열을 6비트 단위로 변환
    binary_string = ""
    for char in encoded_str:
        index = base64_table.index(char)
        binary_string += f"{index:06b}"  # 6비트 이진수로 변환하여 결합
    
    # 24비트씩 잘라서 원래의 8비트로 나누기
    decoded_str = ""
    for i in range(0, len(binary_string), 24):
        chunk = binary_string[i:i+24]
        for j in range(0, 24, 8):
            byte = chunk[j:j+8]
            if len(byte) == 8:
                decoded_str += chr(int(byte, 2))  # 8비트 이진수를 문자로 변환
    
    return decoded_str

T = int(input())

for test_case in range(1, T + 1):
    encoded_str = input() # 입력받는 문자
    result = base64_decode(encoded_str)
    print(f"#{test_case} {result}")