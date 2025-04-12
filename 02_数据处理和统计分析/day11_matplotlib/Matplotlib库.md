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



