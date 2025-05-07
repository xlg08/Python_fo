from PIL import Image

def convert_to_8bit(image_path, output_path):
    try:
        # 打开图片
        image = Image.open('../data/8.png')

        # 转换为8位深（模式为'L'表示灰度图，'P'表示调色板模式）
        # 如果想要彩色的8位深图片，可以使用'P'模式
        converted_image = image.convert('L')

        # 保存转换后的图片
        converted_image.save('../data/7.png')
        print(f"图片已成功转换并保存到 {output_path}")
    except Exception as e:
        print(f"转换过程中出现错误: {e}")

# 示例调用
image_path = 'input_image.tif'  # 替换为你的输入图片路径
output_path = 'output_image.jpg'  # 替换为你想要保存的输出图片路径
convert_to_8bit(image_path, output_path)