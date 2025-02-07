import os
import numpy as np
import pickle
import cv2

farsi_digits_en = [
    'sefr', 'yek', 'do', 'se', 'char', 'panj', 'shish', 'haft', 'hasht', 'noh',
    'alef', 'be', 'pe', 'te', 'se', 'jim', 'che', 'he', 'khe', 'dal',
    'zal', 're', 'ze', 'zhe', 'sin', 'shin', 'sad', 'zad', 'ta', 'za',
    'ein', 'ghein', 'fe', 'ghaf', 'kaf', 'gaf', 'lam', 'mim', 'non', 'vav',
    'he', 'ye',
]
farsi_digits_fa = [
    '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹',
    'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د',
    'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
    'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و',
    'ه', 'ی',
]

with open('farsi_handwritten_64.pkl', 'rb') as f:
    data = pickle.load(f)
    digit_data = data['digit']
    for i in range(10):
        print(farsi_digits_en[digit_data['train']['target'][i]])
        cv2_imshow(digit_data['train']['data'][i])
