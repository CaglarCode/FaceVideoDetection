This script uses OpenCV to detect faces from a live webcam feed and plays a siren sound when a face is detected. The primary goal is to demonstrate basic face detection using the Haar Cascade method and triggering an alarm based on the detection.

Requirements
Python 3.x
OpenCV
Pygame
Numpy
Installation
Install OpenCV:

sh
Copy code
pip install opencv-python
Install Pygame:

sh
Copy code
pip install pygame
Ensure you have the Haar Cascade file for face detection. You can download it from here.

Usage
Place the Haar Cascade XML file and the siren sound file (siren.mp3) in your working directory.

Run the script:

sh
Copy code
python face_detection_alarm.py
The webcam feed will open, and the program will start detecting faces. When a face is detected, the siren will sound.

Code Explanation
Pygame Initialization: Sets up the mixer for sound playback.
Face Cascade: Loads the Haar Cascade XML for face detection.
Video Capture: Opens the webcam for capturing video frames.
Face Detection Loop: Continuously reads frames, converts them to grayscale, and applies the face detection algorithm. If a face is detected and certain conditions are met, the siren plays.
Troubleshooting
If the camera does not open, ensure it is not being used by another application.
Make sure the Haar Cascade XML file path is correct.
Adjust the detection parameters (scaleFactor, minNeighbors, minSize) for better results.
Türkçe
Bu betik, OpenCV kullanarak canlı webcam akışından yüzleri algılar ve bir yüz algılandığında siren sesi çalar. Ana amaç, Haar Cascade yöntemi kullanarak temel yüz algılamayı ve algılamaya dayalı bir alarmı tetiklemeyi göstermektir.

Gereksinimler
Python 3.x
OpenCV
Pygame
Numpy
Kurulum
OpenCV'yi yükleyin:

sh
Copy code
pip install opencv-python
Pygame'i yükleyin:

sh
Copy code
pip install pygame
Yüz algılama için Haar Cascade dosyasını edinin. Buradan indirebilirsiniz.

Kullanım
Haar Cascade XML dosyasını ve siren ses dosyasını (siren.mp3) çalışma dizininize yerleştirin.

Betiği çalıştırın:

sh
Copy code
python face_detection_alarm.py
Webcam akışı açılacak ve program yüz algılamaya başlayacaktır. Yüz algılandığında siren sesi çalacaktır.

Kod Açıklaması
Pygame Başlatma: Ses oynatma için mikseri ayarlar.
Yüz Cascade: Yüz algılama için Haar Cascade XML dosyasını yükler.
Video Yakalama: Video karelerini yakalamak için kamerayı açar.
Yüz Algılama Döngüsü: Sürekli olarak kareleri okur, gri tonlamaya dönüştürür ve yüz algılama algoritmasını uygular. Eğer bir yüz algılanır ve belirli koşullar sağlanırsa, siren çalar.
Sorun Giderme
Kamera açılmıyorsa, başka bir uygulama tarafından kullanılmadığından emin olun.
Haar Cascade XML dosya yolunun doğru olduğundan emin olun.
Daha iyi sonuçlar için algılama parametrelerini (scaleFactor, minNeighbors, minSize) ayarlayın.
