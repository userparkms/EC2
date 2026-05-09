import streamlit as st

st.set_page_config(
    page_title="EC2 Streamlit 배포 실습",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 EC2 Streamlit 배포 실습")
st.markdown("**AWS EC2 환경에서 실행 중인 Streamlit 앱입니다.**")
st.divider()

# 텍스트 입력
st.subheader("👤 이름 입력")
name = st.text_input("이름을 입력하세요", placeholder="홍길동")

# 메시지 입력
st.subheader("💬 메시지 입력")
message = st.text_area("전달할 메시지를 입력하세요", placeholder="메시지를 입력해주세요")

# 버튼
if st.button("✅ 제출하기", use_container_width=True):
    if name and message:
        st.success(f"안녕하세요, **{name}**님! 메시지가 정상적으로 접수되었습니다.")
        st.info(f"📨 입력하신 메시지: {message}")
        st.balloons()
    elif not name:
        st.warning("이름을 입력해주세요.")
    elif not message:
        st.warning("메시지를 입력해주세요.")

st.divider()
st.caption("실습 3 — AWS Learner Lab EC2 배포 실습")