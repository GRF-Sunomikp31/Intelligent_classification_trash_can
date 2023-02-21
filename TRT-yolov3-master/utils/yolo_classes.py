"""yolov3_classes.py

NOTE: Number of YOLOv3 COCO output classes differs from SSD COCO models.
"""

COCO_CLASSES_LIST = [
    "2_香蕉皮","2_大水果","2_小水果","2_果皮","2_菜叶","2_水果皮碎","1_易拉罐","1_纸团",
    "1_水瓶","1_纸盒","1_塑料块","1_瓶","3_电池","3_黑袋","4_烟头","4_餐巾纸"
]

def get_cls_dict(model):
    """Get the class ID to name translation dictionary."""
    if model == 'coco':
        cls_list = COCO_CLASSES_LIST
    else:
        raise ValueError('Bad model name')
    return {i: n for i, n in enumerate(cls_list)}
