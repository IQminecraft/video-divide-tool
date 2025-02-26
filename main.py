import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget 
import os

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clip divider")
        self.setGeometry(100, 100, 800, 600)

        # メディアプレーヤーのセットアップ
        self.media_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.media_player.setAudioOutput(self.audio_output)

        # ビデオウィジェットのセットアップ
        self.video_widget = QVideoWidget(self)
        self.media_player.setVideoOutput(self.video_widget)

        # メインウィジェットとレイアウト
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # ビデオウィジェットをレイアウトに追加
        self.main_layout.addWidget(self.video_widget)
        
        # ボタン
        self.open_button1 = QPushButton("フォルダを開く", self)
        self.open_button1.clicked.connect(self.open_folder)
        self.main_layout.addWidget(self.open_button1)

        # ボタンレイアウトの作成
        self.button_layout = QHBoxLayout()

        prev_button = QPushButton("前", self)
        prev_button.clicked.connect(self.ago)
        
        next_button = QPushButton("次", self)
        next_button.clicked.connect(self.next)

        self.button_layout.addWidget(prev_button)
        self.button_layout.addWidget(next_button)

        self.files_and_dirs = []
        self.NUM = 0
        self.text_var = QLabel(self)
        self.main_layout.addWidget(self.text_var)
        self.main_layout.addLayout(self.button_layout)

    def play_video(self, video_path):
        self.media_player.setSource(QUrl.fromLocalFile(video_path))
        self.media_player.play()
        self.text_var.setText(video_path)

    def ago(self):
        if self.NUM > 0:
            self.NUM -= 1
            self.play_video(self.files_and_dirs[self.NUM])

    def next(self):
        if self.NUM < len(self.files_and_dirs) - 1:
            self.NUM += 1
            self.play_video(self.files_and_dirs[self.NUM])

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "フォルダを選択")
        if folder_path:
            self.files_and_dirs = [f"{folder_path}/{f}" for f in os.listdir(folder_path) if f.endswith(".mp4")]
            self.files_and_dirs.sort(reverse=True)
            self.NUM = 0
            if self.files_and_dirs:
                self.play_video(self.files_and_dirs[self.NUM])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())