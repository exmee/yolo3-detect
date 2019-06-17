# yolo3-detect
object detect, face detect, video detect
安装环境：
	按照env文件夹中的文件安装虚拟环境

object detect:
1、云盘中下载相应的权重(yolo.h5)放入model_data文件夹
2、在yolo.py/def my_detect_img(yolo): 中输入要检测的图片路径
3、运行yolo.py即可以检测物体

face detect:
1、云盘中下载相应的权重（yolo_face.h5）放入model_data文件夹
2、在yolo.py/def __init__(self): 改为face detect
3、在yolo.py/def my_detect_img(yolo): 中输入要检测的图片路径
4、运行yolo.py即可以检测人脸

train:
1、根据train.txt的格式构造数据集的输入文件，代码中修改路径annotation_path
	行格式:' image_file_path box1 box2…boxN ';
	box格式:' x_min,y_min,x_max,y_max,class_id '
2、根据'model_data/yolo_anchors.txt'的格式构造数据集的类别文件放入model_data文件夹，代码中修改路径classes_path
3、选择训练的初始权重，代码中修改路径def _main():/weights_path
	一般为yolo.h5或者darknet53_weights.h5（yolo3的原始权重）
4、运行train.py

检测视频中的物体：
1、云盘中下载相应的权重放入model_data文件夹
2、输入检测视频文件的路径
3、运行yolo_video.py



另：
convert.py可以把Darknet模型转换为Keras模型
	例：python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
