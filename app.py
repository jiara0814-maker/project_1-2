
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Search Fatigue Dashboard", layout="wide")

selection = st.sidebar.selectbox(
    "메뉴 선택",
    ["2단계: 이탈의 임계점 분석"]
)

# --- 2단계: 이탈의 임계점 분석 ---
if selection == "2단계: 이탈의 임계점 분석":
    st.header("Phase 2: 이탈의 임계점 (Tipping Point) 분석")

    # 데이터 생성
    data_p2 = {
        'Group': ['Immediate Exit', 'Quick Scan', 'Standard Browse', 'Deep Consideration', 'Decision Fatigue'],
        'Churn_Rate(%)': [13.74, 14.63, 14.69, 15.72, 15.36],
        'Abandon_Rate': [51.14, 51.31, 50.78, 52.12, 51.62],
        'Churn_in_Abandon': [14.07, 14.36, 15.06, 15.87, 15.33]
    }
    df_p2 = pd.DataFrame(data_p2)

    # 탭 구성
    tab1, tab2, tab3 = st.tabs(["📊 사용자 그룹별 이탈률 분석", "📊 검색 포기자 내 이탈률 분석", "💡 인사이트 & 액션플랜"])

    with tab1:
        st.subheader("사용자 그룹별 이탈률")
        
        # 컬러 코딩
        colors = ['gray', 'gray', 'gray', '#D32F2F', '#E9967A']
        
        fig3 = px.bar(
            df_p2,
            x='Group',
            y='Churn_Rate(%)',
            text='Churn_Rate(%)',
            title="** Deep Consideration (28-48초) 구간에서 이탈률 최대 상승<br>- 결정 붕괴가 행동 리스크(이탈 확률 상승)로 처음 드러나는 구간<br> ",
            color='Group',
            color_discrete_sequence=colors
        )
        
        fig3.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig3.update_layout(
            showlegend=False,
            yaxis_range=[12.5, 17],
            xaxis_title="Group",
            yaxis_title="Churn Rate (%)",
            margin=dict(t=100)
        )
        
        fig3.add_hline(
            y=14.73,
            line_dash="dash",
            line_color="blue",
            annotation_text="Overall Average (14.73%)",
            annotation_position="top right"
        )
        st.plotly_chart(fig3, use_container_width=True)

    with tab2:
        st.subheader("검색 포기자 내 이탈률")
        
        colors = ['gray', 'gray', 'gray', '#D32F2F', '#E9967A']
        
        fig_abandon = px.bar(
            df_p2,
            x='Group',
            y='Churn_in_Abandon',
            text='Churn_in_Abandon',
            title=(
                "** 전체 평균: 무클릭 종료 자체는 ‘즉각적인 이탈 신호’라기보다는 약한 위험 신호→ OTT/콘텐츠 서비스에서 매우 정상적인 구조"
                "<br><br>** Deep Consideration (28-48초): 이탈 위험(좌절+기대감 붕괴)이 실제로 ‘행동으로 처음 드러나는 지점’"
                "<br><br>** Decision Fatigue (48초 이상): 이미 관여도 높은 유저만 남아 있으나, ‘즉시 이탈’이 아니라 ‘장기 전이 위험’ 상태<br> "
            ),
            color='Group',
            color_discrete_sequence=colors
        )
        
        fig_abandon.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_abandon.update_layout(
            showlegend=False,
            yaxis_range=[13, 17],
            xaxis_title="Group",
            yaxis_title="Churn Rate (%)",
            margin=dict(t=180)
        )
        
        fig_abandon.add_hline(
            y=14.94,
            line_dash="dash",
            line_color="blue",
            annotation_text="Overall Average (14.94%)",
            annotation_position="top right"
        )
        st.plotly_chart(fig_abandon, use_container_width=True)

    with tab3:
        st.subheader("💡 비즈니스 인사이트 & 액션플랜")
        st.markdown("""
        * **핵심 발견:** Deep Consideration 그룹의 이탈률이 가장 높으므로, 이 구간에 대한 집중적인 케어가 필요합니다.
        * **액션 플랜:**
            1. **Deep Consideration 조기 개입:** 30초 경과 시 "지금 인기 있는 콘텐츠" 팝업 제안.
            2. **Decision Fatigue 관리:** 강요하지 않고 "다음에 이어보기", "찜하기" 유도하여 세션 종료 경험 개선.
        """)
