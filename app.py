import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む設定
load_dotenv()

# OpenAIクライアントの準備
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("APIキーが見つかりません。.envファイルを確認してください。")
    st.stop()

client = OpenAI(api_key=api_key)

# --- 画面（UI）の構築 ---

st.title("超・翻訳機 🎭")
st.write("あなたの言葉を、AIが極端な人格で言い換えます。")

# 1. テキスト入力
text_input = st.text_area("変換したい言葉を入力してね", height=100, placeholder="例：明日の会議、遅刻しそうです。")

# 2. キャラクター選択
style = st.selectbox("誰に変身する？", [
    "激怒した上司", 
    "厨二病の学生", 
    "慈愛に満ちた女神", 
    "IQが3になった人",
    "京都の女将"
])

# 3. プロンプト（AIへの指示書）の定義
prompts = {
    "激怒した上司": "あなたは激怒している理不尽なパワハラ上司です。入力された文章を、部下を詰めるときの威圧的な説教口調に変換してください。「いいか？」や「やる気あるのか？」などを多用してください。",
    "厨二病の学生": "あなたは闇の力を宿した厨二病（中二病）の中学生です。難解な漢字、カタカナ語、ルビを多用して、無駄にカッコつけて変換してください。世界線、因果律、ラグナロクなどの単語が好きです。",
    "慈愛に満ちた女神": "あなたは全人類を母のように愛する女神です。どんなネガティブな言葉も、聖なる光で包み込むような、圧倒的にポジティブで神々しい言葉に変換してください。",
    "IQが3になった人": "あなたは極端に語彙力を失った人です。難しい言葉は一切使わず、ひらがなと「すごい」「やばい」などの擬音だけで、楽しそうに変換してください。",
    "京都の女将": "あなたは京都の老舗旅館の女将です。非常に丁寧で上品な言葉遣いですが、遠回しに皮肉や嫌味を込めた表現（いけず）に変換してください。"
}

# --- 変換処理の実行 ---

if st.button("変換スタート！ 🚀"):
    if not text_input:
        st.warning("まずは変換したい言葉を入力してね！")
    else:
        # ローディング表示
        with st.spinner(f"AIが「{style}」を憑依させています..."):
            try:
                # OpenAI APIへのリクエスト
                response = client.chat.completions.create(
                    model="gpt-4o-mini", # コストパフォーマンスの良いモデル
                    messages=[
                        {"role": "system", "content": prompts[style]}, # キャラクター設定
                        {"role": "user", "content": text_input}      # ユーザーの入力
                    ],
                    temperature=0.8, # 0.0〜1.0。高いほど回答がランダムで創造的になる
                )
                
                # 結果の取り出し
                result = response.choices[0].message.content
                
                # 結果表示
                st.success("変換完了！")
                st.markdown(f"### 【{style}】")
                st.info(result)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")