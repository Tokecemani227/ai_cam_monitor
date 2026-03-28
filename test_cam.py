import cv2

url = "http://192.168.101.11:8080/video"
cap = cv2.VideoCapture(url)

# Buat window dan konfigurasi ukuran
window_name = "Monitor Kamera"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) 
cv2.resizeWindow(window_name, 640, 480)

print("Berhasil! Tekan tombol 'q' di KEYBOARD untuk menutup.")

while True:
    # Kode jalan kalau 
    ret, frame = cap.read()
    if not ret:
        break

    # Tampilkan frame ke window
    cv2.imshow(window_name, frame)

    # Menutup window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()