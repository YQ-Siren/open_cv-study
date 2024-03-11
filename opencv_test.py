import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# 读取彩色图像
img = cv2.imread(r'C:\Users\Administrator.USER-20211026YD\AppData\Roaming\kingsoft\wpsphoto+\userInfo\1273684823'
                 r'\avatar.png')

# 检查图像是否成功加载
if img is None:
    print("Error: Image not loaded")
else:
    # 显示原始彩色图像
    cv2.imshow("Original Image", img)
    # 将彩色图像转换为灰度图像
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图像保存为 JPEG 文件
    cv2.imwrite(r'C:\Users\Administrator.USER-20211026YD\AppData\Roaming\kingsoft\wpsphoto+\userInfo\1273684823'
                r'\avatar.png', img_grayscale)
    # 使用 Matplotlib 显示灰度图像
    plt.imshow(img_grayscale, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')  # 隐藏坐标轴
    plt.show()