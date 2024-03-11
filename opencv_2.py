import cv2

# 读取彩色图像
img = cv2.imread('C:\\Users\\Administrator.USER-20211026YD\\AppData\\Roaming\\kingsoft\\wpsphoto+\\userInfo\\1273684823\\avatar.png')

# 检查图像是否成功加载
if img is None:
    print("Error: Image not loaded")
else:
    # 显示原始彩色图像
    cv2.imshow("Original Image", img)

    # 将彩色图像转换为灰度图像
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 显示灰度图像
    cv2.imshow("Grayscale Image", img_grayscale)

    # 等待按键输入或等待一段时间后关闭窗口
    cv2.waitKey(0)

    # 关闭所有窗口
    cv2.destroyAllWindows()
