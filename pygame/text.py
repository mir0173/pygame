#텍스트 저장파일 입니다.

import pygame

texthero = pygame.Rect(1410, 690, 0, 0)
textrucy1 = pygame.Rect(1450, 690, 0, 0)
textrucy2 = pygame.Rect(1410, 690, 0, 0)
Hero = pygame.image.load('./image/hero2.png')
Lucy = pygame.image.load('./image/lucy.png')
hero = pygame.Rect(-75, 550, 0, 0)
lucy = pygame.Rect(-75, 550, 0, 0)
B6_1 = pygame.image.load('./image/B6.jpg')
B6_2 = pygame.image.load('./image/B6.jpg')
B6_3 = pygame.image.load('./image/B6.jpg')
B5_1 = pygame.image.load('./image/B5.jpg')
B5_2 = pygame.image.load('./image/B5.jpg')
B5_3 = pygame.image.load('./image/B5.jpg')
B5_4 = pygame.image.load('./image/B5.jpg')
B5_5 = pygame.image.load('./image/B5.jpg')
B4_1 = pygame.image.load('./image/B4.jpg')
B4_2 = pygame.image.load('./image/B4.jpg')
B4_3 = pygame.image.load('./image/B4.jpg')
B4_4 = pygame.image.load('./image/B4.jpg')
B3_1 = pygame.image.load('./image/B3.jpg')
B3_2 = pygame.image.load('./image/B3.jpg')
B3_3 = pygame.image.load('./image/B3.jpg')
B3_4 = pygame.image.load('./image/B3.jpg')
B2 = pygame.image.load('./image/B2.jpg')
B1 = pygame.image.load('./image/B1.jpg')
ilus_1= pygame.image.load('./image/B3.jpg')
ilus_2 = pygame.image.load('./image/B3.jpg')
ilus_3 = pygame.image.load('./image/B3.jpg')
bgpos = (0, 0)


text = [[0, "으윽...", "여기가... 어디지?", "왜 이렇게 어둡지...? 사고라도 난 건가...", "다친 곳은 없는 것 같으니... 일단 앞으로 가야겠군", 0],
[0, "흠... 아무래도 문이 잠겨있는 것 같군", "어떻게 나가야 하지?", 0],
[0, "흠… 아무것도 하지 않았는데 문이 열리다니", "혹시, 내 생각대로 문을 조종할 수 있는 건가?", 0],
[0, "왠지는 모르겠지만 나한테 초능력이라도 생긴 모양이군", "계속해서 앞으로 가보자", 0],
[0, "혹시 문 말고 다른 것도 조종할 수 있으려나...", 0],
[0, "전자기기면 다 가능한 모양이군", "앞에 사다리가 있으니 올라가면 되겠어", 0],
[0, "흠... 여기도 어둡군,  ", "아무래도 불을 켜면서 가야겠어", 0],
[0, "...왜 사람들이 다 죽어 있지...?", "도대체 무슨 일이 있었던 거야...", 0],
[0, "인간의 정신을 컴퓨터에 옮기는 실험이라...", "누가 이런 정신 나간 짓을 한 거지?", "일단 계속 앞으로 가는 수밖에...", 0],
[0, "이런 곳에 연구 일지가 있군", "한번 읽어 보는 게 좋겠어", 0],
[0, "왜 다 내용이 조금씩 지워진 건지는 모르겠지만, 뭔가 문제가 있었던 건 확실한 것 같군", "계속 앞으로 가보자", 0],
[0, "엘리베이터는 해킹이 안 되는 걸 보니 아예 전기가 흐르지 않는 것 같군", "뒤에 있던 회로를 손봐야겠어...", 0],
[0, "이 회로를 손보면 되겠군", 0],
[0, "이제 엘리베이터에 다시 전기가 흐르겠지", 0],
[0 ,"여긴 물건들이 너무 어질러져 있군", "하나씩 치우면서 가야겠어", 0],
[0, "여긴 뭔가 익숙한 장소인데...", "계속 치우면서 앞으로 가야겠어", 0],
[0, "이건... 내 연구 일지인가?", 0],
[0, "나는 연구소에서 무슨 실험을 하고 있었던 거지...", "나는 연구소에서 무슨 실험을 하고 있었던 거지...", "일단 계속 앞으로 나아가자", 0],
[0, "여기만 치우면 다음 층으로 올라갈 수 있겠군", 0],
[0, "이곳은 왜 이렇게 시체가 많은 거지...?", 0],
[0, "(주인공 이름)님! 살아있으셨군요...!", "전... (주인공 이름)님이 죽은 줄 알았어요...", "그... 미안한데 제가 기억을 잃어서...", "누구신가요...?", "그렇군요... 제 이름은 나다니엘이에요... 혹시 기억나시나요...?", "죄송해요... 기억이 쉽게 돌아오지는 않는 것 같아요", "괜찮아요... (주인공 이름)님은 저의 상사셨으니 존댓말 하실 필요는 없어요", "혹시 기억이 얼마나 사라진 거예요?", "음... 정확하진 않지만 내가 임금 문제로 실험실을 고발한 것까지는 기억나", "그럼 제가 (주인공 이름)님의 연구 기록을 찾아볼 테니, 그걸 한번 봐보는 게 어때요?", "연구 기록을 보면 기억이 돌아올 수도 있어요", "좋아", 0 ],
[0, "제가 확인해 봤는데, (주인공 이름)님의 연구 기록은 사고에 휘말려 사라진 것 같아요", "하지만 이 컴퓨터에 (주인공 이름)님의 연구 기록이 저장돼있을 거예요", "제가 지금 찾아볼게요", "괜찮아, 내가 직접 찾아볼게", "잠깐 기다리고 있어", 0],
[0, "초능력은 이런 것도 가능하군..." ,"그나저나, 여기는 굉장히 평화로워...", "마치 유토피아 같아", 0],
[0, "여긴 건너가기에는 너무 넓군...", "모처럼 가상세계에 들어왔으니 새로 생긴 초능력을 시험해볼까?", 0],
[0, "저기에 있는 게 내 연구 기록인 건가?", 0],
[0, "내... 내가 이런 실험을 했었다고...?", "말도 안 돼... 내가 왜 이런 잔인한 실험을 했던 거지...?", "후... 일단 여기서 나가자", 0],
[0, "(주인공 이름)님!", "으... 머리야...", "(주인공 이름)님!! 정신 차려요!!!", "무슨 일이야...?", "(주인공 이름)님이 갑자기 쓰러져서 깜짝 놀랐다고요...", "아... 난 괜찮으니까 신경 쓰지 마", "그런데 왜 갑자기 쓰러지신 거예요?", "방금 데이터 세계에 들어가서 내 연구 기록을 보고 왔어", "설마 내가 생체 실험을 했었다니...", "나 자신을 용서할 수가 없군...", "그런 소리 하지 마세요...", "전 (주인공 이름)님을 존경해요...", "그 실험은 세상을 위한 일이었으니까요...", "이게... 세상을 위한 일이었다고...?", "솔직히 잘 모르겠어...", "하지만 계속 이러고 있을 수는 없지", "다음 층으로 가는 게 좋겠어", 0],
[0, "이 동물들은 데이터 세계에서 잘살고 있었나요?", "아주 행복하게 사는 것 같았어...", "만약 넌 데이터 세계에 들어가 행복하게 살 수 있다면 들어갈 건가?", "음... 잘 모르겠어요", "데이터 세계가 현실보다 행복할 수도 있겠지만, 저는 현실을 살아가는 게 더 가치가 있는 것 같아요...", 0]]

char = [[0, Hero, Hero, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, 0],
[0, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, 0],
[0, Hero, Hero, Hero, 0],
[0, Hero, 0],
[0, Hero, 0],
[0, Lucy, Lucy, Hero, Hero, Lucy, Hero, Lucy, Lucy, Hero, Lucy, Lucy, Hero, 0],
[0, Lucy, Lucy, Lucy, Hero, Hero, 0],
[0, Hero, Hero, Hero, 0],
[0, Hero, Hero, 0],
[0, Hero, 0],
[0, Hero, Hero, Hero, 0],
[0, Lucy, Hero, Lucy, Hero, Lucy, Hero, Lucy, Hero, Hero, Hero, Lucy, Lucy, Lucy, Hero, Hero, Hero, Hero, 0],
[0, Lucy, Hero, Hero, Lucy, Lucy, 0]]


pos = [[0, hero, hero, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, 0],
[0, hero, 0],
[0, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, 0],
[0, hero, hero, hero, 0],
[0, hero, 0],
[0, hero, 0],
[0, lucy, lucy, hero, hero, lucy, hero, lucy, lucy, hero, lucy, lucy, hero, 0],
[0, lucy, lucy, lucy, hero, hero, 0],
[0, hero, hero, hero, 0],
[0, hero, hero, 0],
[0, hero, 0],
[0, hero, hero, hero, 0],
[0, lucy, hero, lucy, hero, lucy, hero, lucy, hero, hero, hero, lucy, lucy, lucy, hero, hero, hero, hero, 0],
[0, lucy, hero, hero, lucy, lucy, 0]]



name = [[0, "주인공", "주인공", "주인공", "주인공", 0],
[ 0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", 0],
[0, "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", 0],
[0, "주인공", "주인공", "주인공",  0],
[0, "주인공", 0],
[0, "주인공", 0],
[0, "???", "???", "주인공", "주인공", "루시퍼", "주인공", "루시퍼", "루시퍼", "주인공", "루시퍼", "루시퍼", "주인공", 0],
[0, "루시퍼", "루시퍼", "루시퍼", "주인공", "주인공", 0],
[0, "주인공", "주인공", "주인공", 0],
[0, "주인공", "주인공", 0],
[0, "주인공", 0],
[0, "주인공", "주인공", "주인공", 0],
[0, "루시퍼", "주인공", "루시퍼", "주인공", "루시퍼", "주인공", "루시퍼", "주인공", "주인공", "주인공", "루시퍼", "루시퍼", "루시퍼" , "주인공", "주인공", "주인공", "주인공", 0],
[0, "루시퍼", "주인공", "주인공", "루시퍼", "루시퍼", 0]]


namepos = [[0, texthero, texthero, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, 0],
[0, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, 0],
[0, texthero, texthero, texthero, 0],
[0, texthero, 0],
[0, texthero, 0],
[0, textrucy1, textrucy1, texthero, texthero, textrucy2, texthero, textrucy2, textrucy2, texthero, textrucy2, textrucy2, texthero, 0],
[0, textrucy2, textrucy2, textrucy2, texthero, texthero, 0],
[0, texthero, texthero, texthero, 0],
[0, texthero, texthero, 0],
[0, texthero, 0],
[0, texthero, texthero, texthero, 0],
[0, textrucy2, texthero, textrucy2, texthero, textrucy2, texthero,textrucy2, texthero, texthero, texthero, textrucy2, textrucy2, textrucy2, texthero, texthero, texthero, texthero, 0],
[0, textrucy2, texthero, texthero, textrucy2, textrucy2, 0]]


background = [B6_1, B6_2, B6_2, B6_2, B6_3, B6_3, B5_1, B5_2, B5_3, B5_4, B5_4, B5_5, B5_5, B5_5, B4_1, B4_2, B4_3, B4_3, B4_4, B3_1, B3_1, B3_2, ilus_1, ilus_2, ilus_3, ilus_3, B3_3]
'''tuto = ["A, D키를 이용해 좌우로 이동할 수 있습니다", "어떤 물체들은 가까이 갈 시 E키를 통해 상호작용할 수 있습니다", "이제부터 주인공이 가까이 가면 전등이 자동으로 켜집니다"]
inter1 = [0, "이 정도로 큰 사고가 일어났다니...", "내가 살아 남은 게 기적이군...", 0]'''
