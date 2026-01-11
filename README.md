# Super Tone Translator (超・翻訳機) 🎭

入力されたテキストを、生成AI（GPT-4o-mini）が「指定された極端な人格」になりきって翻訳・変換するWebアプリケーションです。

## 概要
LINEヤフー株式会社のエントリーに向けた技術キャッチアップの一環として作成しました。
OpenAI APIの `ChatCompletion` を活用し、System Promptの工夫によってキャラクターの口調や思考プロセスを制御しています。

## 🚀 機能
* **テキスト変換**: ユーザーが入力した文章を、選択したキャラクターの口調にリライトします。
* **キャラクター選択**:
    * 激怒した上司 
    * 厨二病の学生 
    * 慈愛に満ちた女神 
    * IQが3になった人 
    * 京都の女将 
* **UI**: Streamlitを用いたインタラクティブなチャット風UI。

## 🛠 使用技術
* **言語**: Python 3.10+
* **フレームワーク**: Streamlit
* **API**: OpenAI API (gpt-4o-mini)
* **ライブラリ**: openai, python-dotenv

## 💡 工夫した点
* **プロンプト**: 単なる語尾の変換だけでなく、「思考プロセス」や「使ってはいけない言葉（制約条件）」をSystem Promptに組み込むことで、人格の憑依レベルを高めました。
* **セキュリティ**: API Keyは `.env` で管理し、GitHubにはアップロードされないよう `.gitignore` を徹底しました。
* **可読性**: 可読性を意識し、UI構築部分とロジック部分を整理して実装しました。

## 📦 インストールと実行

```bash
# リポジトリのクローン
git clone [https://github.com/](https://github.com/)<あなたのユーザー名>/super-translator.git

# パッケージのインストール
pip install -r requirements.txt

# .envファイルの作成
# OPENAI_API_KEY=sk-xxxx... を記述

# アプリの起動
streamlit run app.py