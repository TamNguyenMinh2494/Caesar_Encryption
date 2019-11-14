class Caesar():
    key='aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'

    def encrypt(self, n, plaintext):
        result = ''
        for pl in plaintext:
            try:
                """EK(i) = (i+k) mod N"""
                i = (self.key.index(pl) + n) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += pl
        return result
    def decrypt(self, n, ciphertext):
        result = ''
        for ci in ciphertext:
            try:
                i = (self.key.index(ci) - n) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += ci
        return result

    def show_result(self, plaintext, n):
        encrypted = self.encrypt(n, plaintext)
        decrypted = self.decrypt(n, encrypted)

        print('Rotation: ',n)
        print('Plaintext: ', plaintext)
        print('Encrypted: ', encrypted)
        print('Decrypted: ',decrypted)
if __name__ == "__main__":
    caesar = Caesar()
    caesar.show_result("Nguyen Minh Tam", 20)