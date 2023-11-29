import tkinter as tk
import random
import pyperclip

def create_groups():
    names = input_entry.get()
    participant_list = names.split(',')
    
    # リストをシャッフルしてランダムに並び替える
    random.shuffle(participant_list)
    
    groups = []
    group_size = int(group_size_var.get())  # チームサイズを取得
    
    # リストから指定したサイズでグループを作成
    team_names = ["TeamA", "TeamB", "TeamC", "TeamD", "TeamE", "TeamF", "TeamG", "TeamH", "TeamI", "TeamJ", "TeamK", "TeamL", "TeamM", "TeamN"]  # グループ名のリスト
    for i in range(0, len(participant_list), group_size):
        group = participant_list[i:i + group_size]
        if team_names:
            team_name = team_names.pop(0)
        else:
            team_name = "Team" + str(len(groups) + 1)
        groups.append((team_name, group))
    
    # 結果を表示
    result = ""
    for team, members in groups:
        result += f"{team}: {', '.join(members)}\n"
    
    # 結果を表示
    result_text.config(text=result)

def copy_to_clipboard():
    result = result_text.cget("text")
    # 結果をクリップボードにコピー
    pyperclip.copy(result)

def reset_result():
    # 結果をリセット
    result_text.config(text="")
    # エントリウィジェットの内容もリセット
    input_entry.delete(0, tk.END)

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("グループ作成アプリ")

# チームサイズを選択するオプションメニューを作成
group_size_label = tk.Label(window, text="チームサイズを選択してください:")
group_size_label.pack()

group_size_var = tk.StringVar()
group_size_var.set("2")  # デフォルトのチームサイズを2に設定

group_size_menu = tk.OptionMenu(window, group_size_var, "2", "3", "4")
group_size_menu.pack()

# ラベルとエントリウィジェットを作成
input_label = tk.Label(window, text="参加者の名前をカンマ区切りで入力してください:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# グループ作成ボタン、クリップボードにコピーするボタン、結果リセットボタンを作成
create_button = tk.Button(window, text="グループを作成", command=create_groups)
create_button.pack()

copy_button = tk.Button(window, text="クリップボードにコピー", command=copy_to_clipboard)
copy_button.pack()

reset_button = tk.Button(window, text="結果をリセット", command=reset_result)
reset_button.pack()

# 結果表示のテキストウィジェットを作成
result_text = tk.Label(window, text="", wraplength=400)
result_text.pack()

# アプリケーションを開始
window.mainloop()
