import streamlit as st
import textwrap


# ---------------------------------------------------------
# 페이지 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered",
)


# ---------------------------------------------------------
# CSS 디자인
# ---------------------------------------------------------
st.markdown(
    """
<style>
.stApp {
    background: linear-gradient(135deg, #fff7d6 0%, #dff4ff 100%);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #252525;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 17px;
    color: #555555;
    margin-bottom: 30px;
}

.result-card {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 28px;
    border-radius: 22px;
    border: 3px solid #ffcb05;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    text-align: center;
    margin-top: 25px;
}

.pokemon-emoji {
    font-size: 80px;
    margin-bottom: 5px;
}

.pokemon-name {
    font-size: 35px;
    font-weight: 800;
    color: #2a75bb;
    margin-bottom: 5px;
}

.pokemon-type {
    display: inline-block;
    background-color: #ffcb05;
    color: #222222;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 18px;
}

.mbti-title {
    font-size: 20px;
    font-weight: 700;
    color: #333333;
    margin-bottom: 12px;
}

.description {
    font-size: 17px;
    line-height: 1.75;
    color: #444444;
}

.reason-box {
    background-color: #f4f9ff;
    border-radius: 14px;
    padding: 16px;
    margin-top: 18px;
    text-align: left;
}

.reason-box ul {
    margin-bottom: 0;
}

.reason-box li {
    margin-bottom: 8px;
}

.footer {
    text-align: center;
    color: #777777;
    font-size: 13px;
    margin-top: 40px;
}

div.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    background-color: #ef5350;
    color: white;
    font-size: 18px;
    font-weight: 700;
    padding: 12px;
}

div.stButton > button:hover {
    background-color: #d93f3c;
    color: white;
    border: none;
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# MBTI별 포켓몬 데이터
# ---------------------------------------------------------
pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧬",
        "type": "에스퍼",
        "nickname": "전략적인 설계자",
        "description": (
            "높은 지능과 강한 독립심을 가진 뮤츠는 자신만의 계획과 "
            "기준을 중요하게 여기는 INTJ와 잘 어울립니다."
        ),
        "reasons": [
            "복잡한 상황을 빠르게 분석합니다.",
            "다른 사람에게 쉽게 휩쓸리지 않습니다.",
            "뚜렷한 목표와 강한 의지를 가지고 있습니다.",
        ],
    },
    "INTP": {
        "pokemon": "메타몽",
        "emoji": "🫠",
        "type": "노말",
        "nickname": "호기심 많은 논리술사",
        "description": (
            "어떤 모습으로도 변할 수 있는 메타몽은 다양한 가능성을 탐구하고 "
            "새로운 아이디어를 실험하는 INTP와 닮았습니다."
        ),
        "reasons": [
            "정해진 방식보다 새로운 가능성을 선호합니다.",
            "상황에 맞게 유연하게 변화합니다.",
            "끊임없이 관찰하고 탐구합니다.",
        ],
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥",
        "type": "불꽃·비행",
        "nickname": "대담한 통솔자",
        "description": (
            "강한 카리스마와 추진력을 가진 리자몽은 목표를 향해 "
            "팀을 이끄는 ENTJ의 리더십을 잘 보여줍니다."
        ),
        "reasons": [
            "도전을 두려워하지 않습니다.",
            "강한 존재감과 리더십을 지녔습니다.",
            "목표를 향해 빠르게 행동합니다.",
        ],
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "👻",
        "type": "고스트·독",
        "nickname": "재치 있는 변론가",
        "description": (
            "장난기와 재치가 넘치는 팬텀은 새로운 자극을 즐기고 "
            "기발한 생각으로 주변을 놀라게 하는 ENTP와 잘 어울립니다."
        ),
        "reasons": [
            "예측하기 어려운 매력을 가지고 있습니다.",
            "재치 있고 장난스러운 성격입니다.",
            "틀에 얽매이지 않는 아이디어를 냅니다.",
        ],
    },
    "INFJ": {
        "pokemon": "루기아",
        "emoji": "🌊",
        "type": "에스퍼·비행",
        "nickname": "통찰력 있는 옹호자",
        "description": (
            "깊고 평온한 힘을 가진 루기아는 조용하지만 강한 신념으로 "
            "다른 사람을 보호하는 INFJ와 닮았습니다."
        ),
        "reasons": [
            "겉으로는 차분하지만 내면의 힘이 강합니다.",
            "다른 존재를 보호하려는 마음이 큽니다.",
            "깊은 통찰력과 신비로운 분위기를 지녔습니다.",
        ],
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🦊",
        "type": "노말",
        "nickname": "따뜻한 중재자",
        "description": (
            "다양한 모습으로 성장할 가능성을 가진 이브이는 자신의 가치와 "
            "가능성을 소중히 여기는 INFP와 잘 어울립니다."
        ),
        "reasons": [
            "다양한 가능성과 잠재력을 품고 있습니다.",
            "따뜻하고 친근한 매력을 지녔습니다.",
            "환경과 선택에 따라 특별하게 성장합니다.",
        ],
    },
    "ENFJ": {
        "pokemon": "가디안",
        "emoji": "💫",
        "type": "에스퍼·페어리",
        "nickname": "정의로운 선도자",
        "description": (
            "소중한 존재를 지키기 위해 큰 힘을 발휘하는 가디안은 "
            "타인의 성장을 돕고 사람들을 이끄는 ENFJ와 닮았습니다."
        ),
        "reasons": [
            "상대방의 감정을 세심하게 살핍니다.",
            "소중한 사람을 적극적으로 보호합니다.",
            "부드러움과 강한 책임감을 함께 지녔습니다.",
        ],
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "type": "전기",
        "nickname": "활기찬 활동가",
        "description": (
            "밝고 에너지 넘치는 피카츄는 사람들에게 즐거움을 주며 "
            "새로운 모험을 좋아하는 ENFP와 가장 잘 어울립니다."
        ),
        "reasons": [
            "밝고 친근한 에너지를 전합니다.",
            "새로운 만남과 모험을 즐깁니다.",
            "감정 표현이 풍부하고 따뜻합니다.",
        ],
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢",
        "type": "물",
        "nickname": "신뢰할 수 있는 현실주의자",
        "description": (
            "단단한 방어력과 안정적인 전투 능력을 가진 거북왕은 "
            "책임감 있고 신뢰할 수 있는 ISTJ와 잘 어울립니다."
        ),
        "reasons": [
            "맡은 일을 끝까지 책임집니다.",
            "안정적이고 체계적으로 행동합니다.",
            "필요한 순간에 확실한 힘을 보여줍니다.",
        ],
    },
    "ISFJ": {
        "pokemon": "럭키",
        "emoji": "🥚",
        "type": "노말",
        "nickname": "헌신적인 수호자",
        "description": (
            "다친 포켓몬을 돌보는 따뜻한 마음을 가진 럭키는 "
            "주변 사람을 세심하게 챙기는 ISFJ와 닮았습니다."
        ),
        "reasons": [
            "다른 사람을 돌보는 데서 보람을 느낍니다.",
            "친절하고 배려심이 깊습니다.",
            "조용히 곁을 지키며 안정감을 줍니다.",
        ],
    },
    "ESTJ": {
        "pokemon": "윈디",
        "emoji": "🐕",
        "type": "불꽃",
        "nickname": "체계적인 경영자",
        "description": (
            "충성심과 빠른 실행력을 가진 윈디는 질서와 책임을 중요하게 "
            "생각하며 조직을 이끄는 ESTJ와 잘 어울립니다."
        ),
        "reasons": [
            "결단력이 있고 행동이 빠릅니다.",
            "책임감과 충성심이 강합니다.",
            "주변을 안정적으로 이끄는 힘이 있습니다.",
        ],
    },
    "ESFJ": {
        "pokemon": "님피아",
        "emoji": "🎀",
        "type": "페어리",
        "nickname": "다정한 집정관",
        "description": (
            "사랑스럽고 친밀한 유대를 중요하게 여기는 님피아는 "
            "주변 사람을 세심하게 챙기고 조화를 만드는 ESFJ와 닮았습니다."
        ),
        "reasons": [
            "사람들과 친밀한 관계를 잘 형성합니다.",
            "밝고 따뜻한 분위기를 만듭니다.",
            "상대방의 감정을 빠르게 알아차립니다.",
        ],
    },
    "ISTP": {
        "pokemon": "개굴닌자",
        "emoji": "🥷",
        "type": "물·악",
        "nickname": "냉철한 장인",
        "description": (
            "민첩하고 침착하게 상황에 대응하는 개굴닌자는 "
            "뛰어난 관찰력과 실전 감각을 가진 ISTP와 잘 어울립니다."
        ),
        "reasons": [
            "위기에서도 침착함을 유지합니다.",
            "상황에 맞는 실용적인 해결책을 찾습니다.",
            "독립적이고 민첩하게 행동합니다.",
        ],
    },
    "ISFP": {
        "pokemon": "샤미드",
        "emoji": "💧",
        "type": "물",
        "nickname": "온화한 모험가",
        "description": (
            "부드럽고 자유로운 분위기를 가진 샤미드는 감수성이 풍부하고 "
            "자신의 방식대로 세상을 경험하는 ISFP와 닮았습니다."
        ),
        "reasons": [
            "차분하고 부드러운 매력을 지녔습니다.",
            "주변 환경에 자연스럽게 적응합니다.",
            "자신만의 감성과 자유를 중요하게 생각합니다.",
        ],
    },
    "ESTP": {
        "pokemon": "루카리오",
        "emoji": "🥊",
        "type": "격투·강철",
        "nickname": "대담한 사업가",
        "description": (
            "빠른 판단력과 뛰어난 전투 감각을 가진 루카리오는 "
            "현실적인 문제를 즉시 해결하고 도전을 즐기는 ESTP와 잘 어울립니다."
        ),
        "reasons": [
            "빠르게 상황을 파악하고 행동합니다.",
            "도전과 경쟁을 즐깁니다.",
            "강한 자신감과 실전 감각을 지녔습니다.",
        ],
    },
    "ESFP": {
        "pokemon": "푸린",
        "emoji": "🎤",
        "type": "노말·페어리",
        "nickname": "자유로운 연예인",
        "description": (
            "노래와 표현을 좋아하는 푸린은 밝은 에너지로 사람들의 "
            "관심을 모으고 순간을 즐기는 ESFP와 닮았습니다."
        ),
        "reasons": [
            "자신을 표현하는 것을 좋아합니다.",
            "주변에 즐거운 분위기를 만듭니다.",
            "감정이 풍부하고 즉흥적인 매력이 있습니다.",
        ],
    },
}


# ---------------------------------------------------------
# 화면 제목
# ---------------------------------------------------------
st.markdown(
    """
<div class="main-title">⚡ MBTI 포켓몬 추천</div>
<div class="sub-title">
MBTI를 선택하면 당신과 잘 어울리는 포켓몬을 추천해 드립니다.
</div>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# MBTI 선택
# ---------------------------------------------------------
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요.",
    options=list(pokemon_data.keys()),
    index=None,
    placeholder="MBTI를 선택해 주세요.",
)

recommend_button = st.button("나와 어울리는 포켓몬 확인하기")


# ---------------------------------------------------------
# 추천 결과
# ---------------------------------------------------------
if recommend_button:
    if mbti is None:
        st.warning("먼저 MBTI를 선택해 주세요.")

    else:
        result = pokemon_data[mbti]

        reason_html = "".join(
            f"<li>{reason}</li>"
            for reason in result["reasons"]
        )

        result_html = textwrap.dedent(
            f"""
            <div class="result-card">
                <div class="pokemon-emoji">
                    {result["emoji"]}
                </div>

                <div class="mbti-title">
                    {mbti} · {result["nickname"]}
                </div>

                <div class="pokemon-name">
                    {result["pokemon"]}
                </div>

                <div class="pokemon-type">
                    타입: {result["type"]}
                </div>

                <div class="description">
                    {result["description"]}
                </div>

                <div class="reason-box">
                    <strong>✨ 추천 포인트</strong>
                    <ul>
                        {reason_html}
                    </ul>
                </div>
            </div>
            """
        ).strip()

        st.balloons()

        st.markdown(
            result_html,
            unsafe_allow_html=True,
        )

        st.info(
            "이 추천 결과는 재미를 위한 콘텐츠이며, "
            "공식 MBTI 또는 포켓몬 진단이 아닙니다."
        )


# ---------------------------------------------------------
# 하단 안내
# ---------------------------------------------------------
st.markdown(
    """
<div class="footer">
Pokémon 캐릭터의 권리는 각 권리자에게 있습니다.<br>
본 웹앱은 학습 및 비상업적 예시 목적으로 제작되었습니다.
</div>
""",
    unsafe_allow_html=True,
)
