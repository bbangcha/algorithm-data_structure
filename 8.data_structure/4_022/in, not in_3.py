wrongWord = ['쩔었다', '짭새', '꼽사리', '먹튀', '지린', '쪼개다', '뒷담 까다']
sentence = '짭새 등장에 강도들은 모두 쩔었다, 그리고 강도들은 지린 듯 도망갔다'

for word in wrongWord:
    if word in sentence:
        print(f'비속어 : {word}')