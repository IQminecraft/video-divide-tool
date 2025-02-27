import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout, QSlider, QListWidget
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget 
import os
import shutil


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.files_and_dirs = []
        self.NUM = 0
        self.setWindowTitle("クリップ整理つーる")
        self.resize(1000, 1100)

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
        self.layout = QVBoxLayout(self.central_widget)

        # ビデオウィジェットをレイアウトに追加
        self.layout.addWidget(self.video_widget)
        
        # シークバーの作成
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.sliderMoved.connect(self.set_position)
        self.layout.addWidget(self.slider)

        # ボタン
        self.open_button1 = QPushButton("フォルダを開く", self)
        self.open_button1.clicked.connect(self.open_folder)
        self.open_button2 = QPushButton("Reload", self)
        self.open_button2.clicked.connect(self.reload)
        self.layout.addWidget(self.open_button1)
        self.layout.addWidget(self.open_button2)

        #リストウィジェット
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
        self.list_widget.setFixedHeight(300)

        # ボタンレイアウトの作成
        self.button_layout = QHBoxLayout()
        button1 = QPushButton("べっど", self)
        button1.clicked.connect(self.bed)
        button2 = QPushButton("ぶりっじ", self)
        button2.clicked.connect(self.bridge)
        button3 = QPushButton("くらっち", self)
        button3.clicked.connect(self.clutch)
        button4 = QPushButton("せんとう", self)
        button4.clicked.connect(self.fight)
        button5 = QPushButton("その他", self)
        button5.clicked.connect(self.other)
        button6 = QPushButton("valo", self)
        button6.clicked.connect(self.valo)

        #ボタン追加
        self.button_layout.addWidget(button1)
        self.button_layout.addWidget(button2)
        self.button_layout.addWidget(button3)
        self.button_layout.addWidget(button4)
        self.button_layout.addWidget(button5)
        self.button_layout.addWidget(button6)
        self.text_var = QLabel(self)
        self.layout.addLayout(self.button_layout)

        # メディアプレーヤーのシグナル接続
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        
        #リストクリック時
        self.list_widget.itemClicked.connect(self.list_clicked)

    def play_video(self, video_path):
        self.media_player.setSource(QUrl.fromLocalFile(video_path))
        self.media_player.play()
        self.text_var.setText(video_path)

    def bed(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\bed")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.media_player.play()

    def bridge(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\bridge")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.media_player.play()

    def clutch(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\clutch")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.media_player.play()

    def fight(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\fight")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.media_player.play()

    def other(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\other")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.media_player.play()

    def valo(self):
        l = self.files_and_dirs.index(self.selected_text)
        if self.files_and_dirs[l+1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l+1]))
        elif self.files_and_dirs[l-1]:
            self.media_player.setSource(QUrl.fromLocalFile(self.files_and_dirs[l-1]))
        else:
            pass
        self.media_player.play()
        shutil.move(self.selected_text, "D:\\obs\\Best-Clips\\valo")
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.list_widget.clear()
        self.list_widget.addItems(self.files_and_dirs)

    def list_clicked(self, item):
        self.selected_text = item.text()
        self.media_player.setSource(QUrl.fromLocalFile(self.selected_text))
        self.media_player.play()

    def open_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "フォルダを選択")
        if self.folder_path:
            self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
            self.files_and_dirs.sort(reverse=True)
            self.NUM = 0
            if self.files_and_dirs:
                self.play_video(self.files_and_dirs[self.NUM])
                self.list_widget.clear()
                self.list_widget.addItems(self.files_and_dirs)
                

    def set_position(self, position):
        self.media_player.setPosition(position)

    def reload(self):
        self.files_and_dirs = [f"{self.folder_path}/{f}" for f in os.listdir(self.folder_path) if f.endswith(".mp4")]
        self.files_and_dirs.sort(reverse=True)
        self.list_widget.clear()
        self.list_widget.addItems(self.files_and_dirs)

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())