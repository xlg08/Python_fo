# Matplotlib库

## plt.rcParams

> ​	在 Python 的 Matplotlib 库中，*plt.rcParams* 是一个非常重要的配置工具。它允许用户自定义图形的各种属性，从而轻松打造出符合个人或项目需求的图表样式。*plt.rcParams* 实际上是一个字典对象，存储了 Matplotlib 的所有默认配置参数。通过修改这个字典中的键值对，可以全局地改变 Matplotlib 的默认行为
>
> ​	\# 设置全局字体大小
>
> ​	plt.rcParams['font.size'] = 14
>
> ​	# 设置坐标轴标签字体大小
>
> ​	plt.rcParams['axes.labelsize'] = 12
>
> ​	# 设置图形尺寸
>
> ​	plt.rcParams['figure.figsize'] = (10.0, 8.0)
>
> ​	# 设置线条样式和宽度
>
> ​	plt.rcParams['lines.linestyle'] = '--'
>
> ​	plt.rcParams['lines.linewidth'] = 2
>
> ​	# 设置网格透明度
>
> ​	plt.rcParams['grid.alpha'] = 0.75

### plt.rcParams 的原理

> ​	在 Matplotlib 这个强大的 Python 数据可视化库中，plt.rcParams 是一个至关重要的配置工具，它允许自定义图形的各种属性，从而轻松打造出符合个人或项目需求的图表样式。
>
> ​	plt.rcParams 实际上是一个字典对象，存储了 Matplotlib 的所有默认配置参数。通过修改这个字典中的键值对，可以 全局地 改变 Matplotlib 的默认行为。

> 例如：希望默认的图形尺寸是 10x8 英寸，而不是 Matplotlib 的默认尺寸
>
> 可以通过以下方式设置：
>
> ​	import matplotlib.pyplot as plt
>
> ​	plt.rcParams['figure.figsize'] = (10.0, 8.0)
> ​	
>
> 之后，创建的每一个图形都会默认使用这个尺寸，除非显式地改变它。

### plt.rcParams 的作用

#### plt.rcParams 的作用主要体现在以下几个方面：



> 全局样式统一：通过 plt.rcParams，可以确保整个项目或应用中所有图形的样式统一，从而增强图表的可读性和美观性。
>
> 个性化定制：Matplotlib 提供了大量的配置选项，通过 plt.rcParams，可以根据自己的喜好或项目的需求，定制出个性化的图表样式。
>
> 动态调整：plt.rcParams 可以在脚本的任意位置进行修改，意味着可以在运行时动态地调整图形的样式，以适应不同的场景。

> 例如：使用 plt.rcParams 修改字体和轴标签大小：
>
> ​	plt.rcParams['font.size'] = 14  # 设置全局字体大小
> ​	plt.rcParams['axes.labelsize'] = 12  # 设置坐标轴标签字体大小

### plt.rcParams 的注意事项
#### 在使用 plt.rcParams 时，有几点需要注意：

> 谨慎修改全局设置：由于 plt.rcParams 修改的是全局配置，因此在修改之前要谨慎考虑，以免影响到其他部分的代码或图形。如果需要临时修改某个图形的样式，可以使用 with plt.rc_context() 上下文管理器来局部修改配置。
>
> 配置参数名称的准确性：Matplotlib 的配置参数名称是固定的，因此在设置时要确保参数名称的准确性。可以通过 plt.rcParams.keys() 查看所有可用的配置参数。
>
> 配置文件的使用：除了直接在代码中修改 plt.rcParams，我们还可以将配置信息保存在一个配置文件中（通常是 .matplotlibrc 文件），然后在代码中通过 matplotlib.rc_file() 加载这个文件。这种方式更适合于长期、大量的配置修改。


### plt.rcParams 的高级用法

### 除了基本的配置修改，plt.rcParams 还有一些高级用法可以更灵活地控制图形的样式

#### 使用字典更新：可以通过一次性传入一个字典来更新多个配置参数，这样可以更加简洁地设置样式
> new_rc_params = {
> ​    'figure.figsize': (12, 8),
> ​    'lines.linewidth': 2,
> ​    'font.family': 'serif'
> }
> plt.rcParams.update(new_rc_params)

#### 使用 rc_context 局部修改：如果只想在特定代码块中修改配置，而不影响其他部分的代码，可以使用 with plt.rc_context()

> with plt.rc_context({'lines.linewidth': 3}):
> ​    plt.plot([1, 2, 3], [1, 2, 3])
>
> 在这个代码块之后，lines.linewidth 会恢复为之前的值


#### 配置文件的使用：通过创建 .matplotlibrc 文件，可以在其中指定默认的配置参数，这样每次启动 Python 或 Matplotlib 时，都会自动加载这些配置

### plt.rcParams 的代码示例

#### 例如：想要绘制一个简单的正弦波图形，并希望这个图形具有特定的样式。

> 可以首先设置 `plt.rcParams`，然后绘制图形：
>
> ​	import matplotlib.pyplot as plt
>
> ​	import numpy as np
>
>
>
> ​	#生成正弦波数据
>
> ​	x = np.linspace(0, 2 * np.pi, 100)
> ​	y = np.sin(x)
>
>
>
> ​	#使用plt.rcParams设计样式
>
> ​	plt.rcParams['axes.labelsize'] = 14  # 设置坐标轴标签字体大小
> ​	plt.rcParams['axes.titlesize'] = 16  # 设置标题字体大小
>
> ​	plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度标签字体大小
> ​	plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度标签字体大小
> ​	plt.rcParams['grid.alpha'] = 0.75  # 设置网格透明度
>
>
>
> ​	#绘制图形
>
> ​	plt.plot(x, y, label='Sine Wave', color='blue', linestyle='-')
> ​	plt.title('Sine Wave Example')
> ​	plt.xlabel('x')
> ​	plt.ylabel('y')
> ​	plt.legend()
> ​	plt.grid(True)  # 显示网格
>
>
>
> ​	#显示图形
>
> ​	plt.show()
>
>

> ​	首先生成了正弦波的数据，然后设置了多个与图形显示相关的 plt.rcParams 配置项。接着，使用 plt.plot() 绘制了图形，并添加了标题、坐标轴标签和图例。最后，通过 plt.grid(True) 开启了网格，并使用 plt.show() 显示了图形。由于已经通过 plt.rcParams 设置了样式，所以最终的图形将具有设置的指定的外观。

### plt.rcParams 的进一步定制

> 除了上述的基本配置外，`plt.rcParams` 还提供了大量的选项，允许进一步定制图形的外观。
>
> 以下是一些常见的定制项：
>
> ​	1.颜色定制：通过修改 axes.prop_cycle 可以设置线条、标记等元素的颜色循环。
> ​	plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['r', 'g', 'b', 'c'])
>
> ​	2.线条样式和标记：通过 lines.linestyle 和 lines.marker 可以分别设置线条的样式和标记的形状。
> ​	plt.rcParams['lines.linestyle'] = '--'  		# 设置虚线
> ​	plt.rcParams['lines.marker'] = 'o'  		# 设置圆形标记
>
> ​	3.背景色和边框：使用 figure.facecolor 和 axes.edgecolor 可以分别设置图形背景和坐标轴边框的颜色。
> ​	plt.rcParams['figure.facecolor'] = 'lightgrey'  		# 设置图形背景色为浅灰色
> ​	plt.rcParams['axes.edgecolor'] = 'black'  		# 设置坐标轴边框颜色为黑色
>
> ​	通过组合这些配置选项，可以创建出高度个性化的图表，以满足不同的视觉需求和项目规范。
>

