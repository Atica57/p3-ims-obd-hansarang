""" Mission """

# 기존 baseline code로 제공되었던 faster_rcnn architecture의 config base에 추가
_base_ = [
    './cascade_mask_rcnn_swin_small_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py'
]
model = dict(
    neck=dict(
        # model의 neck 부분만 BiFPN으로 변경
        type='BiFPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        strides=[4, 8, 16, 32],
        norm_cfg=dict(type='BN', requires_grad=True),
        num_outs=5)
)
