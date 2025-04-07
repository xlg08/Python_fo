import streamlit as st
"""
    部署格式：
        在终端中运行：streamlit run 模块名称

"""

# 1. 标题
st.title("Streamlit 初体验")

# 2. 段落
st.write("哈哈哈")
st.write("啦啦啦")

# 3. 标题
'# 1级标题'
'## 2级标题'
'### 3级标题'
'#### 4级标题'

# 4. 分割线
st.divider()

# 5.演示markdown 函数 等


st.markdown("# 一级标题")
st.markdown("## 二级标题")

# 展示图片
st.image("")