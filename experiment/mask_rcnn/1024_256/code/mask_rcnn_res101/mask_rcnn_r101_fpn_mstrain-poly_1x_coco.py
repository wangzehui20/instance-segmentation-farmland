_base_ = [
    'mask_rcnn_r50_fpn.py',
    'coco_instance.py',
    'schedule.py', 'default_runtime.py'
]

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))