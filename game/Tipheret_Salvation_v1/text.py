# 텍스트 저장파일 입니다.

import pygame

textluci = pygame.Rect(1410, 690, 0, 0)
texturi1 = pygame.Rect(1450, 690, 0, 0)
texturi2 = pygame.Rect(1410, 690, 0, 0)
textbul = pygame.Rect(1240, 690, 0, 0)
textsil = pygame.Rect(1370, 690, 0, 0)
textqmark = pygame.Rect(1450, 690, 0, 0)
textrapha = pygame.Rect(1370, 690, 0, 0)
textmich = pygame.Rect(1410, 690, 0, 0)

Luci = pygame.transform.scale(pygame.image.load('./assets/lucifer.png'), (526/3, 914/3))
Uri = pygame.transform.scale(pygame.image.load('./assets/uriel.png'), (526/3, 914/3))
Bul = pygame.image.load('./assets/bul.png')
SilA = pygame.transform.scale(pygame.image.load('./assets/silA.png'), (526/3, 914/3))
SilB = pygame.transform.scale(pygame.image.load('./assets/silB.png'), (526/3, 914/3))
SilC = pygame.transform.scale(pygame.image.load('./assets/silC.png'), (526/3, 914/3))
Rapha = pygame.transform.scale(pygame.image.load('./assets/raphael.png'), (526/3, 914/3))
Mich = pygame.transform.scale(pygame.image.load('./assets/michael.png'), (526/3, 914/3))

luci = pygame.Rect(0, 596, 0, 0)
uri = pygame.Rect(0, 596, 0, 0)
bul = pygame.Rect(0, 596, 0, 0)
sil = pygame.Rect(0, 596, 0, 0)
qmark = pygame.Rect(0, 596, 0, 0)
rapha = pygame.Rect(0, 596, 0, 0)
mich = pygame.Rect(0, 596, 0, 0)

text = [[0, "으윽...", "여기가... 어디지?", "벽이 왜 다 부서졌지...? 사고라도 난 건가...", "다친 곳은 없는 것 같으니... 일단 앞으로 가보자.", 0],
        [0, "문이 잠겨있는 건가?", "어떻게 나가야 하지?", 0],
        [0, "문이 열리면 좋겠다고 생각만 했는데 문이 열렸네...", "설마 내 생각대로 문을 조종할 수 있는 건가?", 0],
        [0, "문이 알아서 움직이다니... 초능력이라도 생긴 건가?", "우선 계속 앞으로 가보자.", 0],
        [0, "전등도 켤 수 있으려나?", 0],
        [0, "전자기기면 다 가능한 것 같네.", "일단 위로 올라가자.", 0],
        [0, "여기는 불이 다 꺼져 있네...", "아무래도 불을 켜면서 가야겠어", 0],
        [0, "...왜 사람들이 다 죽어 있지...?", "도대체 무슨 일이 있었던 거야...", 0],
        [0, "인간의 정신을 컴퓨터에 옮기는 실험이라...", "누가 이런 끔찍한 짓을 한 거지?", 0],
        [0, "이 정도로 큰 사고가 일어났다니...", "내가 살아남은 건 기적이네", 0],
        [0, "이건 무슨 노트지?", 0],
        [0, "아까 컴퓨터에서 봤던 그 실험의 연구 일지인가...?", "실험 도중 문제가 생긴 건가?", 0],
        [0, "엘리베이터는 조종할 수가 없네.", "뒤에 있는 회로를 손봐야겠어.", 0],
        [0, "이제 불이 들어오네.", 0],
        [0, "여긴 길이 막혀있네.", "조금 치우면서 가야겠어", 0],
        [0, "여긴 뭔가 익숙한 느낌이 드는데...", "계속 치우면서 앞으로 가자.", 0],
        [0, "또 연구 일지인가?", "이건... 내 이름이잖아?", 0],
        [0, "나는 연구소에서 무슨 실험을 하고 있었던 거지...", "임금 문제를 신고했다고 생체 실험을 당한 건가...?", 0],
        [0, "여기만 치우면 다음 층으로 올라갈 수 있겠어", 0],
        [0, "이곳은 왜 이렇게 시체가 많은 거지...?", 0],
        [0, "루시퍼 님! 살아계셨군요...!", "전... 루시퍼 님이 죽은 줄 알았어요...", "미안한데 내가 기억을 잃어서 그러는데...", "누구?",
         "그렇군요... 제 이름은 우리엘이에요.", "루시퍼 님과 연구를 하고 있었어요.", "혹시 기억나시나요?", "미안... 기억이 쉽게 돌아오지는 않는 것 같아",
         "괜찮아요... 혹시 기억이 얼마나 사라진 거예요?", "사실 아무것도 기억나지 않아",
         "하지만 연구일지를 찾아보니 내가 임금 문제로 실험실을 고발했더군.", "그럼 제가 루시퍼 님이 참여한 프로젝트의 연구 기록을 찾아볼게요.",
         "연구 기록을 보면 기억이 돌아올 수도 있어요", "좋아", 0],
        [0, "정말... 끔찍한 광경이군...", 0],
        [0, "제가 확인해 봤는데, 연구 기록은 사고에 휘말려 사라진 것 같아요", "하지만 이 컴퓨터에 연구 기록이 저장돼있을 거예요", "제가 지금 찾아볼게요",
         "괜찮아, 내가 직접 찾아볼게", "잠깐 기다리고 있어", 0],
        [0, "여긴... 어디지?", "이것도 초능력의 영향인가?", "여기는 아까 연구 일지에서 봤던 데이터 세계인가?", "그나저나, 여기는 굉장히 평화롭네.", "마치 유토피아 같아.", 0],
        [0, "데이터 세계에 업로드된 의식은 이런 식으로 자아를 가지는 건가...?", "진심으로 행복한 것처럼 보이네...", 0],
        [0, "여긴 건너가기에는 너무 넓은데...", "가상세계에 들어왔으니 다른 능력도 생기지 않았을까?", 0],
        [0, "저기에 있는 게 내 연구 기록인 건가?", 0],
        [0, "내... 내가 이런 실험을 했었다고...?", "말도 안 돼... 내가 왜 이런 잔인한 실험을 했던 거지...?", "... 일단 여기서 나가자", 0],
        [0, "루시퍼 님!", "루시퍼 님!! 정신 차려요!!!", "아... 우리엘", "루시퍼 님이 갑자기 쓰러져서 깜짝 놀랐어요.",
         "아... 난 괜찮으니까 신경 쓰지 마", "그런데 왜 갑자기 쓰러지신 거예요?", "방금 데이터 세계에 들어가서 내 연구 기록을 보고 왔어", "네...?", "믿기 힘들겠지만 사실이야.", "아니요. 저는 루시퍼님을 믿어요.", "내가 생명을 해치는 실험을 했다니...",
         "나 자신을 용서할 수가 없어...", "그런 소리 하지 마세요...", "전 루시퍼 님을 존경해요.", "그 실험은 세상을 위한 일이었잖아요.",
         "이 실험이... 세상을 위한 일이었다고...?", "난 잘 모르겠어...", "기억을 잃기 전의 내가 어떤 생각을 했었는지는 모르겠지만...", "지금의 나로서는 이해할 수 없어...", 0],
        [0, "저기 바로 앞에 엘리베이터가 있어요!", 0],
        [0, "작동을 안 하네요...", "고장 난 건가?", "잠깐 뒤로 비켜봐.", 0],
        [0, "이제 위층으로 올라가자.", "엥...? 어떻게 하신 거예요?", "아까 컴퓨터 속으로 들어갔던 것과 비슷한 건가요?", "응.", "사실 기억을 잃고 쓰러진 후 깨어났더니 초능력이 생겼어.", "아무래도 주변 전자기기들을 해킹해 마음대로 쓸 수 있는 것 같아.", "정말 엄청나네요...", "...", "한 가지 물어볼 게 있어.", "데이터 세계 속 연구일지에서 미카엘이라는 이름을 봤어.", "혹시 누군지 알고 있어?", "미카엘 회장님은 이 회사의 CEO에요.", "루시퍼 님과 같이 프로젝트 에덴을 진행한 사람이에요.", "프로젝트 에덴을 계획하고 주도한 장본인이죠.", "프로젝트 에덴이 뭔데?", "저도 뭔지 자세히는 모르지만, 인류 전체를 구원할 궁극의 계획이라고 들었어요!", "(그 생체실험은 프로젝트 에덴의 일환이었던 건가...)", 0],
        [0, "여긴 사고 때문에 유리가 다 부서져 있네요.", "빨리 다음 방으로 가봐요.", "위로 올라갈수록 충격적인 장면들밖에 없네...", 0],
        [0, "이건... 일기인가?", 0],
        [0, "여기에 아직 갇혀있는 실험체들이 있어요.", "여기가 내가 생체실험을 자행한 곳인가...?", "지금 당장 저 사람들을 꺼내줘야겠어.", 0],
        [0, "괜찮으세요?", 0],
        [0, "저희는 여러분을 헤치려는 게 아니에요...", ".........", "저희랑 같이 밖으로 나가요... 네?", "싫어요...", "왜 그러세요...? 저희가 여러분을 보살펴 드릴게요...", "당신들이...", "당신들이... 우리를 가지고 실험했잖아요...", "우리는... 하지 말아 달라고 했는데...", "적어도 당신들이 사람이라면...", "제 딸은 실험에 쓰지 않았어야 하는 거 아닌가요...?", "이제 와서 착한 사람인 척 해봤자...", "당신들을 믿을 수 없어요...", "......", "죄송합니다...", "정말 죄송합니다...", "하지만 지금은 같이 이곳을 탈출해야 해요...", "제발 저희를 믿어주세요...", "......", "알았어요...", "(설마 연구소에서 이런 끔찍한 실험을 하고 있었다니...)", "(나는 이 연구소가 선량한 곳인 줄만 알았는데...)", "(미카엘... 날 속이다니... 용서할 수 없어...)", "(다음에 만날 때 꼭 죽여버리겠어...!!!)", "그런데 제 딸은 왜 시험관에서 나오지 않는거죠...?", "어...?", "루시퍼 님이 초능력으로 시험관을 연 거 아니었나요...?", "(이상하네... 문이 왜 안 열리지?)", "제가 확인해 볼게요.", 0],
        [0, "이상하네...", "여기는 아까와 다르게 별로 밝은 분위기는 아닌 것 같아.", "사람들의 의식은 아직 완벽하게 업로드하지 못하는 건가...", "여기서 시험관이 열리지 않는 이유를 찾아야겠어.", 0],
        [0, "이번에도 데이터 세계의 연구 일지인가...", 0],
        [0, "'불완전한 의식3'을 믿지 마...", 0],
        [0, "'불완전한 의식1'은 진실을 말하고 있어...", 0],
        [0, "'불완전한 의식 4'를 구해야 해...", 0],
        [0, "'불완전한 의식2' 구해...", 0],
        [0, "아무래도 이 중 한 명이 아까 마지막으로 갇힌 실험체의 의식인 것 같네...", "이 데이터 세계는 불안정해서 한 명의 의식만 구해도 바로 무너질 것 같아.", "누구를 구해야 할까...?", 0],
        [0, "공간이 붕괴하기 시작했어.", "빨리 탈출해야겠어", 0],
        [0, "딸! 괜찮아?", "엄...마?", "다행이다... 정말 다행이야...", "다행히 구출하는데 성공했어...", "솔직히 아직 당신을 믿을 수 없지만...", "고마워요...", "이제 빨리 다음 층으로 올라가요.", "위에서 누군가 싸우는 소리가 들리는 것 같아요.", 0],
        [0, "죄송합니다...", "당신의 딸은 이미 구할 수 없는 상태였습니다...", "당신들은 또 거짓말이네요.", "애초에 당신들을 믿었던 게 잘못이었어요.", "죄송합니다...", 0],
        [0, "우리엘, 넌 날 어떻게 생각하지?", "...", "생체 실험을 하신 게 후회되세요?", "맞아... 내 자신이 너무 혐오스러워.", "그리고 이 실험을 진행한 미카엘도 용서할 수 없어.", "저도 미카엘을 용서할 수 없어요.", "좋은 목적이라면서 뒤에서는 생체 실험을 진행한 사람이에요.", "루시퍼 님과 같이 싸울게요.", "고마워... 우리엘.", 0],
        [0, "앞에서 싸우는 소리가 들려요!", 0],
        [0, "라파엘라... 설마 너가 우리를 막을 줄이야...", "조용히 해 실험체 A", "미카엘 님의 이상을 가로막는 건 용서하지 않겠다.", "그런데 뒤에 너희는 언제 온 거지?", "참 익숙한 얼굴들이 많군.", "라파엘라...? 당신이 연구소 경비대를 이끌고 있다니...", "당신은 그냥 평범한 연구원인 줄 알았는데...", "넌 신참이니까 모를 만도 하지", "그나저나, 우리 루시퍼 씨는 말 한마디가 없네?", "내가 반갑지 않은 건가?", "미안하지만... 내가 지금 기억을 잃은 상태라...", "뭐, 상관없지.", "그래서, 여긴 뭐하러 온 거지?", 0],
        [0, "미카엘 님을 만나러 왔어요", "죄송하지만 길 좀 비켜주시죠.", "그렇게 이 연구소를 존경하던 너가 반항이라니", "이제 연구소의 진실이라도 깨달은 건가?", "당신 같은 사람이랑 할 얘기는 없어요.", "빨리 비켜주시죠?", "그럴 순 없지.", "경비대, 저 녀석들을 제압해.", "어딜 감히!!", 0],
        [0, "지금이에요. 빨리 달려요!", 0],
        [0, "쳇, 어쩔 수 없지.", "딱히 보내줘도 상관없지만 말이야.", "경비대 추가 지원을 요청한다.", "미카엘 님의 방으로 신속하게 출동하도록.", 0],
        [0, "오. 이게 누구야! 우리 활기찬 신입 아닌가?", "오늘은 무슨 일이지?", "미카엘 님, 절 속이셨더군요.", "응? 그게 무슨 섭섭한 소리야? 신입.", "당신은 분명히 이 연구소가 세상을 위한 연구를 하고 있다고 했었죠...", "무고한 사람들을 잡아다가 생체실험을 하면서 그딴 소리를 하신 거예요?", "이런, 뭔가 오해한 모양이군.", "그 실험은 세상을 구원할 실험이야", "그게 무슨 소리죠?", "실험체들의 숭고한 희생을 통해 나는 마침내 사람의 의식을 데이터 세계로 업로드하는 기술을 개발하는 것에 성공했어.", "이 기술만 있으면 더 이상 그 누구도 현실에서 고통받지 않을 수 있지.", "그 기술 때문에 고통받은 사람들은 어쩌고요?", "희생도 없이 구원을 원한다는 것은 오만방자하기 짝이 없는 짓이지.", "인류는 지금까지 그렇게 살아왔다고.", "진짜 미치셨군요.","당신과는 더 이상 대화할 가치가 없네요.", "죽어주시죠, 미카엘 님.", 0],
        [0, "으윽...", "우리엘!!", "죽으면 안 돼 우리엘!!", "우리엘이라면 총을 가져올 줄 알았지. 준비성이 철저하니깐 말이야.", "미리 은신 로봇을 준비해둬서 다행이군.", "그래서 너는 용건이 뭐지 루시퍼?", "......", "왜 아무 말도 없어?", "이제야 모든 게 기억났어.", "미카엘... 넌 용서할 수 없어...", "넌 또 왜 그래?", "넌 처음부터 생체실험에 동참했잖아.", "이제 와서 그걸 후회하는 건가?", "그래... 그때는 분명 돈에 눈이 멀어서 그랬었지.", "나 자신도 용서할 순 없어.", "하지만 너가 사람을 죽이고도 아무렇지 않은 걸 보니 더 화가 나기 시작했어", "넌 내 손으로 죽여줄게", "어머, 동료가 죽어서 분노하는 건가?", "정말 너답지 않군. 루시퍼.", "말하는 걸 보니 기억상실증이라도 걸렸었나 보지?", "옛날의 넌 이렇게 무르지 않았는데...", "닥쳐", "정말 단단히 화가 났군.", "하지만, 너가 날 막을 수 있을까?", 0],
        [0, "망설임 없이 총을 쏘다니... 정말 대단한군.", "하지만, 아까도 말했듯이 난 사람의 의식을 데이터 세계에 업로드하는 기술을 이미 완성했어", "이미 내 의식은 데이터 세계에 업로드됐어.", "그럼, 잘 있어 루시퍼", "데이터 세계로 가면 도망칠 수 있을 것 같아?", "넌 아무 데도 못 가. 날 쓰러트기리 전까지.", 0],
        [0, "넌 어떻게 데이터 세계로 들어온 거지?", "그 짧은 시간에 의식을 업로드한 것 같지는 않고...", "무슨 짓을 한 거지?", "내가 새로운 능력이 하나 생겨서 말이야.", "설마 사고 때문에 너한테 그 시약이 들어간 건가...", "뭐 상관없어.", "...", "뭐지...? 왜 인터넷과 연결이 끊긴 거지...?", "인터넷은 이미 내 통제 아래에 있다.", "다시 말해 너는 이 세계에서 도망칠 수 없다는 거지.", "어리석은 녀석...", "이 공간 안에서 나는 신과 같은 존재다.", "그에 비해 이 공간에서 너의 능력은 온전하지 못하지", "하지만 너의 능력, 꽤 쓸 만해 보이는 걸?", "일이 귀찮아졌지만 어쩔 수 없지.", "영광으로 생각해라. 너를 나의 새로운 낙원의 밑거름으로 삼아주마.", "그 더러운 주둥아리를 닫게 만들어주마!", 0],
        [0, "여... 여기서 끝나다니...", "큰소리치더니 고작 이 정도인가?", "닥쳐... 아직 더 싸울 수 있어...", "입만 살았군. 현실을 직시하지 못하는 너의 모습이 참 안타깝구나.", "넌 더 이상 상대할 가치도 없다.", "하지만 너의 그 능력은 잘 써줄게", "그럼, 이만.", 0],
        [0, "루시퍼... 나쁘지 않았어...", "내 세계에서 이 정도로 싸울 수 있다니 상상 이상이야.", "미카엘.", "넌 아직도 데이터 세계로 세상을 구할 수 있다고 생각하나?", "반대로 질문하지.", "너는 인간이 현실에서 행복할 수 있다고 생각하나?", "인간은 끊임없이 불행을 불러오는 존재들일 뿐이야", "우리 가족은 매우 평범했고 화목한 가정이었다.", "서로 사랑했고 웃음이 끊이지 않았지.", "나는 테러로 내 집, 부모님, 모든 것을 잃었다.", "하지만 정부는 이 사건을 덮는 데에만 급급했고, 마지막 남았던 나의 동생마저 앗아갔다.", "이 '불의의 사고'로 나는 한없이 나락으로 떨어졌다.", "나는 세상 가장 밑바닥에서 왜 나에게 이런 일이 벌어져야 하는가 곰곰이 생각했어.", "결국 그 답을 찾아내고 말았다.", "'인간'", "인간은 한없이 불안정하고, 합리적인 판단을 할 수 없지.", "인간은 잘못된 선택을 하고 이는 잘못된 결과를 불러온다.", "나는 그들이 잘못된 선택을 해야하는 비참한 운명에서 그들을 구원해주겠다.", "사람은 누구나 잘못된 선택을 할 수 있어.", "하지만 그렇기에 인간은 더 아름다운거다.", "잘못된 선택을 바로잡고자 노력하는 것. 결국 이를 통해 성장하는 것이 하늘을 향한 인간의 외침이다.", "그리고 지금 가장 잘못된 선택을 하고 있는 것은 너다!", "모든 사람을 데이터 세계에 옮겨서 완벽한 행복을 실현한다고?", "그건 그저 현실을 외면한 거짓된 행복에 불과해.", "넌 데이터 세계에서 모두가 끝없이 행복한 세상이 만들고 싶었겠지.", "하지만 행복이라는 건 그런 방식으로 얻을 수 있는 게 아니야.", "행복은 고생 끝에 비로소 찾아오는 한 줄기의 빛과도 같지.", "불행이 있어야 행복도 있는 것.", "너의 그런 오만한 생각으로 인간의 정신을 통제해 항상 행복을 주겠다고?", "인간에게 자유가 없는데 어떻게 행복할 수 있지?", "그것은 거짓된, 통제된 행복일 뿐이야!", "말도 안 되는 소리 하지 마,", "모두가 평화롭게 평생 살아갈 수 있는 곳이... 행복하지 않다고?", "그럼 도데체 뭐가 행복이지?", "아무도 죽지 않고 평화로운 것보다 더 큰 행복도 있는 건가?", "통제된 세계 속에서 가축처럼 키워지는 것이 너에게는 행복인가?", "인간은 자유의 동물이다. 자유 없는 인간은 가축과 다를 바가 없어", "쓸데없는 소리다. 세계의 진실을 아는 자는 아무도 없을 것이고 모든 인간이 나의 낙원에 업로드될 것이다.", "개인의 자유? 그깟 하찮은 것이 인류 전체의 행복과 맞바꿀 수 있나?", "도무지 말이 통하지 않는군.", "너의 데이터 세계에서 사람들은 잠깐 행복을 느끼겠지.", "하지만 그것도 잠시 뿐이야.", "누군가는 세계의 진실을 찾아낼 것이고, 결국 사람들은 공허함만 느끼게 될 거라고.", "그리고 모두 업로드될 것이라는 건 인류 모두를 몰살하겠다는 말인가?", "너의 신을 자처하는 그 오만함이 너를 파멸로 이끌 것이다.", "......", "말도 안 되는 소리를 잘도 하는군...", "너의 그 뚫린 입이 이렇게 짜증 나는 건 처음이야.", "더 이상 너와 대화할 가치도 없다.", "이만 널 끝장내주지", 0],
        [0, "천사의 은총으로 너를 진정한 구원으로 인도해주마.", "가장 악마 같은 녀석이 천사의 모습이라니...", "너의 오만도 여기서 끝이다!", 0],
        [0, "이제 너의 무력함을 좀 깨달았을까 루시퍼?", "이걸로 끝이다.", 0],
        [0, "무... 무슨 일이지?", 0],
        [0, "밖에서 무슨 일이 일어나고 있는 거야?", 0],
        [0, "아저씨가 위험해!", 0],
        [0, "당장 멈추지 못해!", "멈춰!", "저 아이는 건들지 마.", "하지만 그러면 미카엘 님이...", "내 말 못 들었어? 저 아이는 건들지 마.", 0],
        [0, "안 돼!!!", "라파엘라! 나를 배신하다니! 너의 딸을 잊은건가! 인간을 구하는 방법은 이것뿐이라고!", "이제 너의 오만함의 끝을 선고한다. 미카엘", "자신이 생각한 최고의 세계에서 죽어가는 건 어떤 느낌일지 궁금하군.", "네가 만든 너의 '낙원'과 함께 영원히 사라져라. 미카엘..", "으아아아아악!!!", 0],
        [0, "(우리엘. 네 원수는 갚았어...)", "루시퍼. 미카엘은 어떻게 됐지?", "데이터 세계 속에서 죽었어.", "결국 그렇게 된 건가...", "......", "라파엘라, 넌 아직 데이터 세계가 인류를 구할 수 있을 거라고 생각하나?", "당연하지.", "데이터 세계는 어떤 사고도 일어나지 않고 아무도 죽지 않아.", "이것이야말로 인류가 추구하던 이상적인 세계 아닌가?", "하지만 그러면 방금 너의 그 선택은...", "잘못된 선택이라고 생각할 수도 있겠지.", "하지만 내가 옳았다는 것을 너도 언젠가는 알게 될 거다.", "아무도 죽지 않고, 항상 행복한 세상이라...", "행복을 느낄 수 없는 세계와 평화로운 세계...", "무엇이 정답인 걸까?", "미카엘의 이상은 정말 틀린 걸까...", "이것이 진짜 정답이었다면... 나는 무슨 짓을 한 거지...", 0],
        [0, "이제 너의 무력함을 좀 깨달았을까 루시퍼?", "끝장을 내주지", "이제 아무도 나를 막을 수 없어.", "너를 나의 낙원의 밑거름으로 써주지.", "이제 사람들은 모두 데이터 세계애서 헹복하게 살아갈 거야.", 0],
        [0, "루시퍼...!!!", "나의 이상이... 나의 꿈이...!!!", "아직도 자신의 패배를 인정하지 못하는 건가?", "그 완벽하신 신이 겨우 이 정도인가?", "그만 끝내자고", 0],
        [0, "여기서... 끝나는 건가...", "어머니... 아버지... 죄송해요... 세상을 구원하지 못했어요...", "여기서 너의 오만함의 끝을 선고하겠다!", 0],
        [0, "으아아아아악!!!", 0],
        [0, "(우리엘. 네 원수는 갚았어...)", "루시퍼. 미카엘은 어떻게 됐지?", "데이터 세계 속에서 죽었어.", "결국 그렇게 된 건가...", "......", "라파엘라, 넌 아직 데이터 세계가 인류를 구할 수 있을 거라고 생각하나?", "당연하지.", "데이터 세계는 어떤 사고도 일어나지 않고 아무도 죽지 않아.", "이것이야말로 인류가 추구하던 이상적인 세계 아닌가?", "하지만 그러면 방금 너의 그 선택은...", "잘못된 선택이라고 생각할 수도 있겠지.", "하지만 내가 옳았다는 것을 너도 언젠가는 알게 될 거다.", "아무도 죽지 않고, 항상 행복한 세상이라...", "행복을 느낄 수 없는 세계와 평화로운 세계...", "무엇이 정답인 걸까?", "미카엘의 이상은 정말 틀린 걸까...", "이것이 진짜 정답이었다면... 나는 무슨 짓을 한 거지...", 0]]



name = [[0, "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],
        [0, "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", 0],

        [0, "루시퍼", 0],
        [0, "???", "???", "루시퍼", "루시퍼", "우리엘", "우리엘", "우리엘", "루시퍼", "우리엘", "루시퍼", "루시퍼", "우리엘", "우리엘", "루시퍼", 0],
        [0, "루시퍼", 0],

        [0, "우리엘", "우리엘", "우리엘", "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", 0],

        [0, "루시퍼", 0],
        [0, "루시퍼", "루시퍼", "루시퍼", 0],

        [0, "우리엘", "우리엘", "루시퍼", "우리엘", "루시퍼", "우리엘", "루시퍼", "우리엘", "루시퍼", "우리엘", "루시퍼", "루시퍼", "우리엘", "우리엘", "우리엘", "우리엘", "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0],

        [0, "우리엘", 0],
        [0, "우리엘", "우리엘", "루시퍼", 0],
        [0, "루시퍼", "우리엘", "우리엘", "루시퍼", "루시퍼", "루시퍼", "우리엘", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "우리엘", "우리엘", "우리엘", "루시퍼", "우리엘", "루시퍼"],

        [0, "우리엘", "우리엘", "루시퍼", 0],
        [0, "루시퍼", 0],

        [0, "우리엘", "루시퍼", "루시퍼", 0],
        [0, "루시퍼", 0],
        [0, "루시퍼", "실험체 B", "우리엘", "실험체 B", "우리엘", "실험체 B", "실험체 B", "실험체 B", "실험체 B", "실험체 B", "실험체 B", "실험체 B", "루시퍼", "루시퍼", "우리엘", "우리엘", "우리엘", "실험체 B", "실험체 B", "우리엘", "우리엘", "우리엘", "우리엘", "실험체 B", "루시퍼", "우리엘", "루시퍼", "루시퍼", 0],

        [0, "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0],
        [0, "루시퍼", 0],
        [0, "불완전한 의식 1", 0],
        [0, "불완전한 의식 2", 0],
        [0, "불완전한 의식 3", 0],
        [0, "불완전한 의식 4", 0],
        [0, "루시퍼", "루시퍼", "루시퍼", 0],
        [0, "루시퍼", "루시퍼", 0],

        [0, "실험체 B", "실험체 C", "실험체 B", "루시퍼", "실험체 B", "실험체 B", "우리엘", "우리엘", 0],
        [0, "루시퍼", "루시퍼", "실험체 B", "실험체 B", "우리엘", 0],

        [0, "루시퍼", "우리엘", "우리엘", "루시퍼", "루시퍼", "우리엘", "우리엘", "우리엘", "루시퍼", 0],

        [0, "우리엘", 0],

        [0, "???", "라파엘라", "라파엘라", "라파엘라", "라파엘라", "우리엘", "우리엘", "라파엘라", "라파엘라", "라파엘라", "루시퍼", "라파엘라", "라파엘라", 0],
        [0, "우리엘", "우리엘", "라파엘라", "라파엘라", "우리엘", "우리엘", "라파엘라", "라파엘라", "우리엘", 0],
        [0, "우리엘", 0],

        [0, "라파엘라", "라파엘라", "라파엘라", "라파엘라", 0],

        [0, "미카엘", "미카엘", "우리엘", "미카엘", "우리엘", "우리엘", "미카엘", "미카엘", "우리엘", "미카엘", "미카엘", "우리엘", "미카엘", "미카엘", "우리엘", "우리엘", "우리엘", 0],
        [0, "우리엘", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "루시퍼", "미카엘", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", "미카엘", "미카엘", 0],
        [0, "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", "루시퍼", 0],

        [0, "미카엘", "미카엘", "미카엘", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", 0],
        [0, "루시퍼", "미카엘", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", 0],

        [0, "미카엘", "미카엘", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "루시퍼", "루시퍼", "미카엘", "미카엘", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", 0],
        [0, "미카엘", "루시퍼", "루시퍼", 0],
        [0, "미카엘", "미카엘", 0],
        [0, "미카엘", 0],
        [0, "미카엘", 0],
        [0, "실험체 C", 0],
        [0, "경비대", "라파엘라", "라파엘라", "경비대", "라파엘라", 0],
        [0, "미카엘", "미카엘", "루시퍼", "루시퍼", "루시퍼", "미카엘", 0],
        [0, "루시퍼", "라파엘라", "루시퍼", "라파엘라", "루시퍼", "루시퍼", "라파엘라", "라파엘라", "라파엘라", "루시퍼", "라파엘라", "라파엘라", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0],
        [0, "미카엘", "미카엘", "미카엘", "미카엘", "미카엘", 0],
        [0, "미카엘", "미카엘", "루시퍼", "루시퍼", "루시퍼", 0],
        [0, "미카엘", "미카엘", "루시퍼", 0],
        [0, "미카엘", 0],
        [0, "루시퍼", "라파엘라", "루시퍼", "라파엘라", "루시퍼", "루시퍼", "라파엘라", "라파엘라", "라파엘라", "루시퍼", "라파엘라", "라파엘라", "루시퍼", "루시퍼", "루시퍼", "루시퍼", "루시퍼", 0]]

char = []

for i in range(len(name)):
    char.append([])
    for k in name[i]:
        if k == 0:
            char[i].append(0)
        elif k == "루시퍼":
            char[i].append(Luci)
        elif k == "우리엘":
            char[i].append(Uri)
        elif i == 20 and k == "???":
            char[i].append(Uri)
        elif k == "불완전한 의식 1" or k == "불완전한 의식 2" or k == "불완전한 의식 3" or k == "불완전한 의식 4":
            char[i].append(Bul)
        elif i == 49 and k == "???":
            char[i].append(SilA)
        elif k == "실험체 B":
            char[i].append(SilB)
        elif k == "실험체 C":
            char[i].append(SilC)
        elif k == "라파엘라":
            char[i].append(Rapha)
        elif k == "미카엘":
            char[i].append(Mich)
        elif k == "경비대":
            char[i].append(Bul)


pos = []

for i in range(len(name)):
    pos.append([])
    for k in name[i]:
        if k == 0:
            pos[i].append(0)
        elif k == "루시퍼":
            pos[i].append(luci)
        elif k == "우리엘":
            pos[i].append(uri)
        elif i == 20 and k == "???":
            pos[i].append(uri)
        elif k == "불완전한 의식 1" or k == "불완전한 의식 2" or k == "불완전한 의식 3" or k == "불완전한 의식 4":
            pos[i].append(bul)
        elif i == 49 and k == "???":
            pos[i].append(sil)
        elif k == "실험체 B":
            pos[i].append(sil)
        elif k == "실험체 C":
            pos[i].append(sil)
        elif k == "라파엘라":
            pos[i].append(rapha)
        elif k == "미카엘":
            pos[i].append(mich)
        elif k == "경비대":
            pos[i].append(mich)

namepos = []

for i in range(len(name)):
    namepos.append([])
    for k in name[i]:
        if k == 0:
            namepos[i].append(0)
        elif k == "루시퍼":
            namepos[i].append(textluci)
        elif k == "우리엘":
            namepos[i].append(texturi2)
        elif i == 20 and k == "???":
            namepos[i].append(texturi1)
        elif k == "불완전한 의식 1" or k == "불완전한 의식 2" or k == "불완전한 의식 3" or k == "불완전한 의식 4":
            namepos[i].append(textbul)
        elif i == 49 and k == "???":
            namepos[i].append(textsil)
        elif k == "실험체 B":
            namepos[i].append(textsil)
        elif k == "실험체 C":
            namepos[i].append(textsil)
        elif k == "라파엘라":
            namepos[i].append(textrapha)
        elif k == "미카엘":
            namepos[i].append(textmich)
        elif k == "경비대":
            namepos[i].append(textmich)