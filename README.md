## 使用说明
    Usage: work4.py [options]
    
    Options:
      -h, --help                            show this help message and exit
      -c CATEGORY, --category=CATEGORY      Select Category
      -t THREAD, --thread=THREAD            threads
      -l LENGTH, --length=LENGTH            length
      -o OUTPUT, --output=OUTPUT            output files

## 参数详解
* -c CATEGORY, --category=CATEGORY 选择需要抓取的分类,默认为`qingchun(清纯)`,参数内容根据url中的特征码来定,比如需要抓取这张页面：`http://www.mnsfz.com/h/meihuo/`,参数内容为`meihuo`
* -t THREAD, --thread=THREAD 设置需求的线程数,每个线程会去抓取不同的页面进行下载,如果遇到错误则结束此线程
* -l LENGTH, --length=LENGTH 设置需要抓取的数量,如果超过这个数量则自动结束
* -o OUTPUT, --output=OUTPUT 输出的目录位置,如果目录不存在则会自动创建

## 实现基本需求的思路：
* 根据用户选择模式请求对应网址内容
	* 分析网址。除去“推荐图片”外，其余栏目url均有固定规则"http://www.mnsfz.com/h/qingchun/" + (qingchun|meihuo|yangguang|qiaopi)
	* 给“推荐图片”此栏单独定义一个url地址，如果用户选择的是推荐栏目，则使用指定的网址。其余的地址，通过固定规则来根据用户的输入拼接。
	* 判断传递过来的page值，如果是第一页直接发送请求，否则通过拼接来取得网址
*  从获取到的内容中使用正则匹配出需要的图片网址
	* 判读返回的状态码，根据状态来判断接下来的动作
	* 返回的状态码为“200”，并且判断不为安全狗的404页面,根据匹配出来的图片网址，发送请求，下载图片到指定目录下
	* 下载前进行COUNT总数+1,如果下载过程中捕捉到异常则-1
* 判断页面中是否还有下一页
	* 如果有则返回对应页数，继续请求拼接后网址的内容
	* 如果没有则跳出循环,结束该线程
