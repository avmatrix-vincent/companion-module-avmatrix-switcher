import struct
from cryptography.fernet import Fernet
import os

class SecureDataManager:
    def __init__(self, key_file=".secret.key", data_file="encrypted_data.bin", backup_key_file=".backup_secret.key"):
        self.key_file = key_file
        self.data_file = data_file
        self.backup_key_file = backup_key_file
        self.key = self.load_or_generate_key()

    ''' 生成密钥 '''
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        self.backup_key(key)
        self.hide_file(self.key_file)
        return key

    ''' 加载密钥 '''
    def load_key(self):
        return open(self.key_file, "rb").read()

    ''' 加载或生成密钥 '''
    def load_or_generate_key(self):
        try:
            return self.load_key()
        except FileNotFoundError:
            return self.generate_key()

    ''' 备份密钥 '''
    def backup_key(self, key):
        with open(self.backup_key_file, "wb") as backup_file:
            backup_file.write(key)
        self.hide_file(self.backup_key_file)

    ''' 从备份文件恢复密钥 '''
    def restore_key_from_backup(self):
        if os.path.exists(self.backup_key_file):
            with open(self.backup_key_file, "rb") as backup_file:
                key = backup_file.read()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            self.hide_file(self.key_file)
            return key
        else:
            raise FileNotFoundError("Backup key file not found.")

    ''' 隐藏文件 '''
    def hide_file(self, file_path):
        if os.name == 'nt':
            os.system(f'attrib +h "{file_path}"')
        else:
            pass  # Unix/Linux系统中，文件名前加点即为隐藏文件

    ''' 加密 '''
    def encrypt_message(self, message: bytes) -> bytes:
        f = Fernet(self.key)
        encrypted_message = f.encrypt(message)
        return encrypted_message

    ''' 解密 '''
    def decrypt_message(self, encrypted_message: bytes) -> bytes:
        f = Fernet(self.key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message

    ''' 保存加密数据 '''
    def save_encrypted_data(self, data: bytes):
        encrypted_data = self.encrypt_message(data)
        with open(self.data_file, "wb") as file:
            file.write(encrypted_data)

    ''' 读取并解密数据 '''
    def load_decrypted_data(self) -> bytes:
        with open(self.data_file, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = self.decrypt_message(encrypted_data)
        return decrypted_data

if __name__ == '__main__':
    # 示例数据
    data = struct.pack('>I', 12345)  # 示例数据，打包成4字节整数

    # 创建SecureDataManager对象
    sdm = SecureDataManager()

    # 保存加密数据
    sdm.save_encrypted_data(data)

    # 读取并解密数据
    loaded_data = sdm.load_decrypted_data()
    print(struct.unpack('>I', loaded_data))  # 解包数据

    # 模拟密钥丢失，从备份恢复密钥
    os.remove(".secret.key")
    sdm.key = sdm.restore_key_from_backup()

    # 再次读取并解密数据
    loaded_data = sdm.load_decrypted_data()
    print(struct.unpack('>I', loaded_data))  # 解包数据
