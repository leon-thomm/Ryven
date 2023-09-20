from ryven.node_env import *

widgets = import_guis(__file__)

import cv2
import numpy as np


class CVImage:
    """
    The OpenCV Mat(rix) data type seems to have overridden comparison operations to perform element-wise comparisons
    which breaks ryverncore-internal object comparisons.
    To avoid this, I'll simply use this wrapper class and recreate a new object every time for now, so ryvencore
    doesn't think two different images are the same.
    """

    def __init__(self, img):
        self.img = img


class NodeBase(Node):
    color = '#00a6ff'


class ReadImage(NodeBase):
    """Reads an image from a file"""

    title = 'Read Image'
    input_widget_classes = {
        'choose file IW': widgets.ChooseFileInputWidget
    }
    init_inputs = [
        NodeInputBP('f_path', add_data={'widget name': 'choose file IW', 'widget pos': 'besides'})
    ]
    init_outputs = [
        NodeOutputBP('img')
    ]

    def __init__(self, params):
        super().__init__(params)

        self.image_filepath = ''

    def view_place_event(self):
        self.input_widget(0).path_chosen.connect(self.path_chosen)
        # self.main_widget_message.connect(self.main_widget().show_path)

    def update_event(self, inp=-1):
        if self.image_filepath == '':
            return

        try:
            self.set_output_val(0, CVImage(cv2.imread(self.image_filepath)))
        except Exception as e:
            print(e)

    def get_state(self):
        data = {'image file path': self.image_filepath}
        return data

    def set_state(self, data, version):
        self.path_chosen(data['image file path'])
        # self.image_filepath = data['image file path']

    def path_chosen(self, file_path):
        self.image_filepath = file_path
        self.update()


class SaveImg(NodeBase):
    title = 'Save Image'
    input_widget_classes = {
        'path input': widgets.PathInput
    }
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('path', add_data={'widget name': 'path input', 'widget pos': 'below'}),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.active = False
        self.file_path = ''
        self.actions['make executable'] = {'method': self.action_make_executable}

    def view_place_event(self):
        self.input_widget(1).path_chosen.connect(self.path_chosen)

    def path_chosen(self, new_path):
        self.file_path = new_path
        self.update()

    def action_make_executable(self):
        self.create_input(type_='exec', insert=0)
        self.active = True

        del self.actions['make executable']
        self.actions['make passive'] = {'method': self.action_make_passive}

    def action_make_passive(self):
        self.delete_input(0)
        self.active = False

        del self.actions['make passive']
        self.actions['make executable'] = {'method': self.action_make_executable}

    def update_event(self, inp=-1):
        if not self.active or (self.active and inp == 0):
            CVImage(cv2.imwrite(self.file_path, self.input(0).img))

    def get_state(self):
        return {'path': self.file_path}

    def set_state(self, data, version):
        self.file_path = data['path']


# ----------------------------------------------------------------

class WebcamFeed(NodeBase):
    title = 'Webcam Feed'
    init_inputs = []
    init_outputs = [
        NodeOutputBP(),
    ]
    main_widget_class = widgets.WebcamFeedWidget

    def video_picture_updated(self, frame):
        self.set_output_val(0, CVImage(frame))


# ----------------------------------------------------------------


class OpenCVNodeBase(NodeBase):
    init_outputs = [
        NodeOutputBP()
    ]
    main_widget_class = widgets.OpenCVNode_MainWidget
    main_widget_pos = 'below ports'

    def __init__(self, params):
        super().__init__(params)

        if self.session.gui:
            from qtpy.QtCore import QObject, Signal
            class Signals(QObject):
                new_img = Signal(object)

            # to send images to main_widget in gui mode
            self.SIGNALS = Signals()

    def view_place_event(self):
        self.SIGNALS.new_img.connect(self.main_widget().show_image)

        try:
            self.SIGNALS.new_img.emit(self.get_img())
        except:  # there might not be an image ready yet
            pass

    def update_event(self, inp=-1):
        new_img_wrp = CVImage(self.get_img())

        if self.session.gui:
            self.SIGNALS.new_img.emit(new_img_wrp.img)

        self.set_output_val(0, new_img_wrp)

    def get_img(self):
        return None


class CustomOpenCV(OpenCVNodeBase):
    """Provides a simple interface to run an OpenCV operation on an image.
    To access the input image write 'img = self.input(0).img'."""

    title = 'OpenCV'
    init_inputs = [
        NodeInputBP()
    ]
    main_widget_class = widgets.CustomOpenCVNode_MainWidget

    def __init__(self, params):
        super().__init__(params)

        self.code = ''

    def get_img(self):
        d = {**locals(), 'img': None}
        exec(self.code, d)
        img = d['img']
        return img

    def get_state(self) -> dict:
        return {
            'code': self.code,
        }

    def set_state(self, data: dict, version):
        self.code = data['code']


class DisplayImg(OpenCVNodeBase):
    title = 'Display Image'
    init_inputs = [
        NodeInputBP('img'),
    ]

    def get_img(self):
        return self.input(0).img


class CvtColor(OpenCVNodeBase):
    color_codes = {
        'COLOR_BayerBG2BGR': cv2.COLOR_BayerBG2BGR, 'COLOR_BayerBG2BGRA': cv2.COLOR_BayerBG2BGRA,
        'COLOR_BayerBG2BGR_EA': cv2.COLOR_BayerBG2BGR_EA, 'COLOR_BayerBG2BGR_VNG': cv2.COLOR_BayerBG2BGR_VNG,
        'COLOR_BayerBG2GRAY': cv2.COLOR_BayerBG2GRAY, 'COLOR_BayerBG2RGB': cv2.COLOR_BayerBG2RGB,
        'COLOR_BayerBG2RGBA': cv2.COLOR_BayerBG2RGBA, 'COLOR_BayerBG2RGB_EA': cv2.COLOR_BayerBG2RGB_EA,
        'COLOR_BayerBG2RGB_VNG': cv2.COLOR_BayerBG2RGB_VNG, 'COLOR_BayerGB2BGR': cv2.COLOR_BayerGB2BGR,
        'COLOR_BayerGB2BGRA': cv2.COLOR_BayerGB2BGRA, 'COLOR_BayerGB2BGR_EA': cv2.COLOR_BayerGB2BGR_EA,
        'COLOR_BayerGB2BGR_VNG': cv2.COLOR_BayerGB2BGR_VNG, 'COLOR_BayerGB2GRAY': cv2.COLOR_BayerGB2GRAY,
        'COLOR_BayerGB2RGB': cv2.COLOR_BayerGB2RGB, 'COLOR_BayerGB2RGBA': cv2.COLOR_BayerGB2RGBA,
        'COLOR_BayerGB2RGB_EA': cv2.COLOR_BayerGB2RGB_EA, 'COLOR_BayerGB2RGB_VNG': cv2.COLOR_BayerGB2RGB_VNG,
        'COLOR_BayerGR2BGR': cv2.COLOR_BayerGR2BGR, 'COLOR_BayerGR2BGRA': cv2.COLOR_BayerGR2BGRA,
        'COLOR_BayerGR2BGR_EA': cv2.COLOR_BayerGR2BGR_EA, 'COLOR_BayerGR2BGR_VNG': cv2.COLOR_BayerGR2BGR_VNG,
        'COLOR_BayerGR2GRAY': cv2.COLOR_BayerGR2GRAY, 'COLOR_BayerGR2RGB': cv2.COLOR_BayerGR2RGB,
        'COLOR_BayerGR2RGBA': cv2.COLOR_BayerGR2RGBA, 'COLOR_BayerGR2RGB_EA': cv2.COLOR_BayerGR2RGB_EA,
        'COLOR_BayerGR2RGB_VNG': cv2.COLOR_BayerGR2RGB_VNG, 'COLOR_BayerRG2BGR': cv2.COLOR_BayerRG2BGR,
        'COLOR_BayerRG2BGRA': cv2.COLOR_BayerRG2BGRA, 'COLOR_BayerRG2BGR_EA': cv2.COLOR_BayerRG2BGR_EA,
        'COLOR_BayerRG2BGR_VNG': cv2.COLOR_BayerRG2BGR_VNG, 'COLOR_BayerRG2GRAY': cv2.COLOR_BayerRG2GRAY,
        'COLOR_BayerRG2RGB': cv2.COLOR_BayerRG2RGB, 'COLOR_BayerRG2RGBA': cv2.COLOR_BayerRG2RGBA,
        'COLOR_BayerRG2RGB_EA': cv2.COLOR_BayerRG2RGB_EA, 'COLOR_BayerRG2RGB_VNG': cv2.COLOR_BayerRG2RGB_VNG,
        'COLOR_BAYER_BG2BGR': cv2.COLOR_BAYER_BG2BGR, 'COLOR_BAYER_BG2BGRA': cv2.COLOR_BAYER_BG2BGRA,
        'COLOR_BAYER_BG2BGR_EA': cv2.COLOR_BAYER_BG2BGR_EA, 'COLOR_BAYER_BG2BGR_VNG': cv2.COLOR_BAYER_BG2BGR_VNG,
        'COLOR_BAYER_BG2GRAY': cv2.COLOR_BAYER_BG2GRAY, 'COLOR_BAYER_BG2RGB': cv2.COLOR_BAYER_BG2RGB,
        'COLOR_BAYER_BG2RGBA': cv2.COLOR_BAYER_BG2RGBA, 'COLOR_BAYER_BG2RGB_EA': cv2.COLOR_BAYER_BG2RGB_EA,
        'COLOR_BAYER_BG2RGB_VNG': cv2.COLOR_BAYER_BG2RGB_VNG, 'COLOR_BAYER_GB2BGR': cv2.COLOR_BAYER_GB2BGR,
        'COLOR_BAYER_GB2BGRA': cv2.COLOR_BAYER_GB2BGRA, 'COLOR_BAYER_GB2BGR_EA': cv2.COLOR_BAYER_GB2BGR_EA,
        'COLOR_BAYER_GB2BGR_VNG': cv2.COLOR_BAYER_GB2BGR_VNG, 'COLOR_BAYER_GB2GRAY': cv2.COLOR_BAYER_GB2GRAY,
        'COLOR_BAYER_GB2RGB': cv2.COLOR_BAYER_GB2RGB, 'COLOR_BAYER_GB2RGBA': cv2.COLOR_BAYER_GB2RGBA,
        'COLOR_BAYER_GB2RGB_EA': cv2.COLOR_BAYER_GB2RGB_EA, 'COLOR_BAYER_GB2RGB_VNG': cv2.COLOR_BAYER_GB2RGB_VNG,
        'COLOR_BAYER_GR2BGR': cv2.COLOR_BAYER_GR2BGR, 'COLOR_BAYER_GR2BGRA': cv2.COLOR_BAYER_GR2BGRA,
        'COLOR_BAYER_GR2BGR_EA': cv2.COLOR_BAYER_GR2BGR_EA, 'COLOR_BAYER_GR2BGR_VNG': cv2.COLOR_BAYER_GR2BGR_VNG,
        'COLOR_BAYER_GR2GRAY': cv2.COLOR_BAYER_GR2GRAY, 'COLOR_BAYER_GR2RGB': cv2.COLOR_BAYER_GR2RGB,
        'COLOR_BAYER_GR2RGBA': cv2.COLOR_BAYER_GR2RGBA, 'COLOR_BAYER_GR2RGB_EA': cv2.COLOR_BAYER_GR2RGB_EA,
        'COLOR_BAYER_GR2RGB_VNG': cv2.COLOR_BAYER_GR2RGB_VNG, 'COLOR_BAYER_RG2BGR': cv2.COLOR_BAYER_RG2BGR,
        'COLOR_BAYER_RG2BGRA': cv2.COLOR_BAYER_RG2BGRA, 'COLOR_BAYER_RG2BGR_EA': cv2.COLOR_BAYER_RG2BGR_EA,
        'COLOR_BAYER_RG2BGR_VNG': cv2.COLOR_BAYER_RG2BGR_VNG, 'COLOR_BAYER_RG2GRAY': cv2.COLOR_BAYER_RG2GRAY,
        'COLOR_BAYER_RG2RGB': cv2.COLOR_BAYER_RG2RGB, 'COLOR_BAYER_RG2RGBA': cv2.COLOR_BAYER_RG2RGBA,
        'COLOR_BAYER_RG2RGB_EA': cv2.COLOR_BAYER_RG2RGB_EA, 'COLOR_BAYER_RG2RGB_VNG': cv2.COLOR_BAYER_RG2RGB_VNG,
        'COLOR_BGR2BGR555': cv2.COLOR_BGR2BGR555, 'COLOR_BGR2BGR565': cv2.COLOR_BGR2BGR565,
        'COLOR_BGR2BGRA': cv2.COLOR_BGR2BGRA, 'COLOR_BGR2GRAY': cv2.COLOR_BGR2GRAY, 'COLOR_BGR2HLS': cv2.COLOR_BGR2HLS,
        'COLOR_BGR2HLS_FULL': cv2.COLOR_BGR2HLS_FULL, 'COLOR_BGR2HSV': cv2.COLOR_BGR2HSV,
        'COLOR_BGR2HSV_FULL': cv2.COLOR_BGR2HSV_FULL, 'COLOR_BGR2Lab': cv2.COLOR_BGR2Lab,
        'COLOR_BGR2LAB': cv2.COLOR_BGR2LAB, 'COLOR_BGR2Luv': cv2.COLOR_BGR2Luv, 'COLOR_BGR2LUV': cv2.COLOR_BGR2LUV,
        'COLOR_BGR2RGB': cv2.COLOR_BGR2RGB, 'COLOR_BGR2RGBA': cv2.COLOR_BGR2RGBA, 'COLOR_BGR2XYZ': cv2.COLOR_BGR2XYZ,
        'COLOR_BGR2YCrCb': cv2.COLOR_BGR2YCrCb, 'COLOR_BGR2YCR_CB': cv2.COLOR_BGR2YCR_CB,
        'COLOR_BGR2YUV': cv2.COLOR_BGR2YUV, 'COLOR_BGR2YUV_I420': cv2.COLOR_BGR2YUV_I420,
        'COLOR_BGR2YUV_IYUV': cv2.COLOR_BGR2YUV_IYUV, 'COLOR_BGR2YUV_YV12': cv2.COLOR_BGR2YUV_YV12,
        'COLOR_BGR5552BGR': cv2.COLOR_BGR5552BGR, 'COLOR_BGR5552BGRA': cv2.COLOR_BGR5552BGRA,
        'COLOR_BGR5552GRAY': cv2.COLOR_BGR5552GRAY, 'COLOR_BGR5552RGB': cv2.COLOR_BGR5552RGB,
        'COLOR_BGR5552RGBA': cv2.COLOR_BGR5552RGBA, 'COLOR_BGR5652BGR': cv2.COLOR_BGR5652BGR,
        'COLOR_BGR5652BGRA': cv2.COLOR_BGR5652BGRA, 'COLOR_BGR5652GRAY': cv2.COLOR_BGR5652GRAY,
        'COLOR_BGR5652RGB': cv2.COLOR_BGR5652RGB, 'COLOR_BGR5652RGBA': cv2.COLOR_BGR5652RGBA,
        'COLOR_BGRA2BGR': cv2.COLOR_BGRA2BGR, 'COLOR_BGRA2BGR555': cv2.COLOR_BGRA2BGR555,
        'COLOR_BGRA2BGR565': cv2.COLOR_BGRA2BGR565, 'COLOR_BGRA2GRAY': cv2.COLOR_BGRA2GRAY,
        'COLOR_BGRA2RGB': cv2.COLOR_BGRA2RGB, 'COLOR_BGRA2RGBA': cv2.COLOR_BGRA2RGBA,
        'COLOR_BGRA2YUV_I420': cv2.COLOR_BGRA2YUV_I420, 'COLOR_BGRA2YUV_IYUV': cv2.COLOR_BGRA2YUV_IYUV,
        'COLOR_BGRA2YUV_YV12': cv2.COLOR_BGRA2YUV_YV12, 'COLOR_COLORCVT_MAX': cv2.COLOR_COLORCVT_MAX,
        'COLOR_GRAY2BGR': cv2.COLOR_GRAY2BGR, 'COLOR_GRAY2BGR555': cv2.COLOR_GRAY2BGR555,
        'COLOR_GRAY2BGR565': cv2.COLOR_GRAY2BGR565, 'COLOR_GRAY2BGRA': cv2.COLOR_GRAY2BGRA,
        'COLOR_GRAY2RGB': cv2.COLOR_GRAY2RGB, 'COLOR_GRAY2RGBA': cv2.COLOR_GRAY2RGBA,
        'COLOR_HLS2BGR': cv2.COLOR_HLS2BGR, 'COLOR_HLS2BGR_FULL': cv2.COLOR_HLS2BGR_FULL,
        'COLOR_HLS2RGB': cv2.COLOR_HLS2RGB, 'COLOR_HLS2RGB_FULL': cv2.COLOR_HLS2RGB_FULL,
        'COLOR_HSV2BGR': cv2.COLOR_HSV2BGR, 'COLOR_HSV2BGR_FULL': cv2.COLOR_HSV2BGR_FULL,
        'COLOR_HSV2RGB': cv2.COLOR_HSV2RGB, 'COLOR_HSV2RGB_FULL': cv2.COLOR_HSV2RGB_FULL,
        'COLOR_Lab2BGR': cv2.COLOR_Lab2BGR, 'COLOR_LAB2BGR': cv2.COLOR_LAB2BGR, 'COLOR_Lab2LBGR': cv2.COLOR_Lab2LBGR,
        'COLOR_LAB2LBGR': cv2.COLOR_LAB2LBGR, 'COLOR_Lab2LRGB': cv2.COLOR_Lab2LRGB,
        'COLOR_LAB2LRGB': cv2.COLOR_LAB2LRGB, 'COLOR_Lab2RGB': cv2.COLOR_Lab2RGB, 'COLOR_LAB2RGB': cv2.COLOR_LAB2RGB,
        'COLOR_LBGR2Lab': cv2.COLOR_LBGR2Lab, 'COLOR_LBGR2LAB': cv2.COLOR_LBGR2LAB,
        'COLOR_LBGR2Luv': cv2.COLOR_LBGR2Luv, 'COLOR_LBGR2LUV': cv2.COLOR_LBGR2LUV,
        'COLOR_LRGB2Lab': cv2.COLOR_LRGB2Lab, 'COLOR_LRGB2LAB': cv2.COLOR_LRGB2LAB,
        'COLOR_LRGB2Luv': cv2.COLOR_LRGB2Luv, 'COLOR_LRGB2LUV': cv2.COLOR_LRGB2LUV, 'COLOR_Luv2BGR': cv2.COLOR_Luv2BGR,
        'COLOR_LUV2BGR': cv2.COLOR_LUV2BGR, 'COLOR_Luv2LBGR': cv2.COLOR_Luv2LBGR, 'COLOR_LUV2LBGR': cv2.COLOR_LUV2LBGR,
        'COLOR_Luv2LRGB': cv2.COLOR_Luv2LRGB, 'COLOR_LUV2LRGB': cv2.COLOR_LUV2LRGB, 'COLOR_Luv2RGB': cv2.COLOR_Luv2RGB,
        'COLOR_LUV2RGB': cv2.COLOR_LUV2RGB, 'COLOR_mRGBA2RGBA': cv2.COLOR_mRGBA2RGBA,
        'COLOR_M_RGBA2RGBA': cv2.COLOR_M_RGBA2RGBA, 'COLOR_RGB2BGR': cv2.COLOR_RGB2BGR,
        'COLOR_RGB2BGR555': cv2.COLOR_RGB2BGR555, 'COLOR_RGB2BGR565': cv2.COLOR_RGB2BGR565,
        'COLOR_RGB2BGRA': cv2.COLOR_RGB2BGRA, 'COLOR_RGB2GRAY': cv2.COLOR_RGB2GRAY, 'COLOR_RGB2HLS': cv2.COLOR_RGB2HLS,
        'COLOR_RGB2HLS_FULL': cv2.COLOR_RGB2HLS_FULL, 'COLOR_RGB2HSV': cv2.COLOR_RGB2HSV,
        'COLOR_RGB2HSV_FULL': cv2.COLOR_RGB2HSV_FULL, 'COLOR_RGB2Lab': cv2.COLOR_RGB2Lab,
        'COLOR_RGB2LAB': cv2.COLOR_RGB2LAB, 'COLOR_RGB2Luv': cv2.COLOR_RGB2Luv, 'COLOR_RGB2LUV': cv2.COLOR_RGB2LUV,
        'COLOR_RGB2RGBA': cv2.COLOR_RGB2RGBA, 'COLOR_RGB2XYZ': cv2.COLOR_RGB2XYZ,
        'COLOR_RGB2YCrCb': cv2.COLOR_RGB2YCrCb, 'COLOR_RGB2YCR_CB': cv2.COLOR_RGB2YCR_CB,
        'COLOR_RGB2YUV': cv2.COLOR_RGB2YUV, 'COLOR_RGB2YUV_I420': cv2.COLOR_RGB2YUV_I420,
        'COLOR_RGB2YUV_IYUV': cv2.COLOR_RGB2YUV_IYUV, 'COLOR_RGB2YUV_YV12': cv2.COLOR_RGB2YUV_YV12,
        'COLOR_RGBA2BGR': cv2.COLOR_RGBA2BGR, 'COLOR_RGBA2BGR555': cv2.COLOR_RGBA2BGR555,
        'COLOR_RGBA2BGR565': cv2.COLOR_RGBA2BGR565, 'COLOR_RGBA2BGRA': cv2.COLOR_RGBA2BGRA,
        'COLOR_RGBA2GRAY': cv2.COLOR_RGBA2GRAY, 'COLOR_RGBA2mRGBA': cv2.COLOR_RGBA2mRGBA,
        'COLOR_RGBA2M_RGBA': cv2.COLOR_RGBA2M_RGBA, 'COLOR_RGBA2RGB': cv2.COLOR_RGBA2RGB,
        'COLOR_RGBA2YUV_I420': cv2.COLOR_RGBA2YUV_I420, 'COLOR_RGBA2YUV_IYUV': cv2.COLOR_RGBA2YUV_IYUV,
        'COLOR_RGBA2YUV_YV12': cv2.COLOR_RGBA2YUV_YV12, 'COLOR_XYZ2BGR': cv2.COLOR_XYZ2BGR,
        'COLOR_XYZ2RGB': cv2.COLOR_XYZ2RGB, 'COLOR_YCrCb2BGR': cv2.COLOR_YCrCb2BGR,
        'COLOR_YCrCb2RGB': cv2.COLOR_YCrCb2RGB, 'COLOR_YCR_CB2BGR': cv2.COLOR_YCR_CB2BGR,
        'COLOR_YCR_CB2RGB': cv2.COLOR_YCR_CB2RGB, 'COLOR_YUV2BGR': cv2.COLOR_YUV2BGR,
        'COLOR_YUV2BGRA_I420': cv2.COLOR_YUV2BGRA_I420, 'COLOR_YUV2BGRA_IYUV': cv2.COLOR_YUV2BGRA_IYUV,
        'COLOR_YUV2BGRA_NV12': cv2.COLOR_YUV2BGRA_NV12, 'COLOR_YUV2BGRA_NV21': cv2.COLOR_YUV2BGRA_NV21,
        'COLOR_YUV2BGRA_UYNV': cv2.COLOR_YUV2BGRA_UYNV, 'COLOR_YUV2BGRA_UYVY': cv2.COLOR_YUV2BGRA_UYVY,
        'COLOR_YUV2BGRA_Y422': cv2.COLOR_YUV2BGRA_Y422, 'COLOR_YUV2BGRA_YUNV': cv2.COLOR_YUV2BGRA_YUNV,
        'COLOR_YUV2BGRA_YUY2': cv2.COLOR_YUV2BGRA_YUY2, 'COLOR_YUV2BGRA_YUYV': cv2.COLOR_YUV2BGRA_YUYV,
        'COLOR_YUV2BGRA_YV12': cv2.COLOR_YUV2BGRA_YV12, 'COLOR_YUV2BGRA_YVYU': cv2.COLOR_YUV2BGRA_YVYU,
        'COLOR_YUV2BGR_I420': cv2.COLOR_YUV2BGR_I420, 'COLOR_YUV2BGR_IYUV': cv2.COLOR_YUV2BGR_IYUV,
        'COLOR_YUV2BGR_NV12': cv2.COLOR_YUV2BGR_NV12, 'COLOR_YUV2BGR_NV21': cv2.COLOR_YUV2BGR_NV21,
        'COLOR_YUV2BGR_UYNV': cv2.COLOR_YUV2BGR_UYNV, 'COLOR_YUV2BGR_UYVY': cv2.COLOR_YUV2BGR_UYVY,
        'COLOR_YUV2BGR_Y422': cv2.COLOR_YUV2BGR_Y422, 'COLOR_YUV2BGR_YUNV': cv2.COLOR_YUV2BGR_YUNV,
        'COLOR_YUV2BGR_YUY2': cv2.COLOR_YUV2BGR_YUY2, 'COLOR_YUV2BGR_YUYV': cv2.COLOR_YUV2BGR_YUYV,
        'COLOR_YUV2BGR_YV12': cv2.COLOR_YUV2BGR_YV12, 'COLOR_YUV2BGR_YVYU': cv2.COLOR_YUV2BGR_YVYU,
        'COLOR_YUV2GRAY_420': cv2.COLOR_YUV2GRAY_420, 'COLOR_YUV2GRAY_I420': cv2.COLOR_YUV2GRAY_I420,
        'COLOR_YUV2GRAY_IYUV': cv2.COLOR_YUV2GRAY_IYUV, 'COLOR_YUV2GRAY_NV12': cv2.COLOR_YUV2GRAY_NV12,
        'COLOR_YUV2GRAY_NV21': cv2.COLOR_YUV2GRAY_NV21, 'COLOR_YUV2GRAY_UYNV': cv2.COLOR_YUV2GRAY_UYNV,
        'COLOR_YUV2GRAY_UYVY': cv2.COLOR_YUV2GRAY_UYVY, 'COLOR_YUV2GRAY_Y422': cv2.COLOR_YUV2GRAY_Y422,
        'COLOR_YUV2GRAY_YUNV': cv2.COLOR_YUV2GRAY_YUNV, 'COLOR_YUV2GRAY_YUY2': cv2.COLOR_YUV2GRAY_YUY2,
        'COLOR_YUV2GRAY_YUYV': cv2.COLOR_YUV2GRAY_YUYV, 'COLOR_YUV2GRAY_YV12': cv2.COLOR_YUV2GRAY_YV12,
        'COLOR_YUV2GRAY_YVYU': cv2.COLOR_YUV2GRAY_YVYU, 'COLOR_YUV2RGB': cv2.COLOR_YUV2RGB,
        'COLOR_YUV2RGBA_I420': cv2.COLOR_YUV2RGBA_I420, 'COLOR_YUV2RGBA_IYUV': cv2.COLOR_YUV2RGBA_IYUV,
        'COLOR_YUV2RGBA_NV12': cv2.COLOR_YUV2RGBA_NV12, 'COLOR_YUV2RGBA_NV21': cv2.COLOR_YUV2RGBA_NV21,
        'COLOR_YUV2RGBA_UYNV': cv2.COLOR_YUV2RGBA_UYNV, 'COLOR_YUV2RGBA_UYVY': cv2.COLOR_YUV2RGBA_UYVY,
        'COLOR_YUV2RGBA_Y422': cv2.COLOR_YUV2RGBA_Y422, 'COLOR_YUV2RGBA_YUNV': cv2.COLOR_YUV2RGBA_YUNV,
        'COLOR_YUV2RGBA_YUY2': cv2.COLOR_YUV2RGBA_YUY2, 'COLOR_YUV2RGBA_YUYV': cv2.COLOR_YUV2RGBA_YUYV,
        'COLOR_YUV2RGBA_YV12': cv2.COLOR_YUV2RGBA_YV12, 'COLOR_YUV2RGBA_YVYU': cv2.COLOR_YUV2RGBA_YVYU,
        'COLOR_YUV2RGB_I420': cv2.COLOR_YUV2RGB_I420, 'COLOR_YUV2RGB_IYUV': cv2.COLOR_YUV2RGB_IYUV,
        'COLOR_YUV2RGB_NV12': cv2.COLOR_YUV2RGB_NV12, 'COLOR_YUV2RGB_NV21': cv2.COLOR_YUV2RGB_NV21,
        'COLOR_YUV2RGB_UYNV': cv2.COLOR_YUV2RGB_UYNV, 'COLOR_YUV2RGB_UYVY': cv2.COLOR_YUV2RGB_UYVY,
        'COLOR_YUV2RGB_Y422': cv2.COLOR_YUV2RGB_Y422, 'COLOR_YUV2RGB_YUNV': cv2.COLOR_YUV2RGB_YUNV,
        'COLOR_YUV2RGB_YUY2': cv2.COLOR_YUV2RGB_YUY2, 'COLOR_YUV2RGB_YUYV': cv2.COLOR_YUV2RGB_YUYV,
        'COLOR_YUV2RGB_YV12': cv2.COLOR_YUV2RGB_YV12, 'COLOR_YUV2RGB_YVYU': cv2.COLOR_YUV2RGB_YVYU,
        'COLOR_YUV420p2BGR': cv2.COLOR_YUV420p2BGR, 'COLOR_YUV420P2BGR': cv2.COLOR_YUV420P2BGR,
        'COLOR_YUV420p2BGRA': cv2.COLOR_YUV420p2BGRA, 'COLOR_YUV420P2BGRA': cv2.COLOR_YUV420P2BGRA,
        'COLOR_YUV420p2GRAY': cv2.COLOR_YUV420p2GRAY, 'COLOR_YUV420P2GRAY': cv2.COLOR_YUV420P2GRAY,
        'COLOR_YUV420p2RGB': cv2.COLOR_YUV420p2RGB, 'COLOR_YUV420P2RGB': cv2.COLOR_YUV420P2RGB,
        'COLOR_YUV420p2RGBA': cv2.COLOR_YUV420p2RGBA, 'COLOR_YUV420P2RGBA': cv2.COLOR_YUV420P2RGBA,
        'COLOR_YUV420sp2BGR': cv2.COLOR_YUV420sp2BGR, 'COLOR_YUV420SP2BGR': cv2.COLOR_YUV420SP2BGR,
        'COLOR_YUV420sp2BGRA': cv2.COLOR_YUV420sp2BGRA, 'COLOR_YUV420SP2BGRA': cv2.COLOR_YUV420SP2BGRA,
        'COLOR_YUV420sp2GRAY': cv2.COLOR_YUV420sp2GRAY, 'COLOR_YUV420SP2GRAY': cv2.COLOR_YUV420SP2GRAY,
        'COLOR_YUV420sp2RGB': cv2.COLOR_YUV420sp2RGB, 'COLOR_YUV420SP2RGB': cv2.COLOR_YUV420SP2RGB,
        'COLOR_YUV420sp2RGBA': cv2.COLOR_YUV420sp2RGBA, 'COLOR_YUV420SP2RGBA': cv2.COLOR_YUV420SP2RGBA,
    }

    title = 'convert color'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('code', dtype=dtypes.Choice(list(color_codes.keys())[0], list(color_codes.keys()))),
    ]

    def get_img(self):
        return cv2.cvtColor(
            src=self.input(0).img,
            code=self.color_codes[self.input(1)],
        )


class SplitColor(NodeBase):
    title = 'split color'
    init_inputs = [
        NodeInputBP('img'),
    ]
    init_outputs = [
        NodeOutputBP('c1'),
        NodeOutputBP('c2'),
        NodeOutputBP('c3'),
    ]

    def update_event(self, inp=-1):
        c1, c2, c3 = cv2.split(self.input(0).img)
        self.set_output_val(0, CVImage(c1))
        self.set_output_val(1, CVImage(c2))
        self.set_output_val(2, CVImage(c3))


class Merge(OpenCVNodeBase):
    title = 'merge'
    init_inputs = [
        NodeInputBP('b'),
        NodeInputBP('g'),
        NodeInputBP('r'),
    ]

    def get_img(self):
        return cv2.merge(
            [self.input(0).img, self.input(1).img, self.input(2).img]
        )


class Bitwise(OpenCVNodeBase):
    ops = {
        'and': cv2.bitwise_and,
        'or': cv2.bitwise_or,
        'xor': cv2.bitwise_xor,
    }

    title = 'bitwise op'
    init_inputs = [
        NodeInputBP('img 1'),
        NodeInputBP('img 2'),
        NodeInputBP('operation', dtype=dtypes.Choice(list(ops.keys())[0], list(ops.keys()))),
    ]

    def get_img(self):
        func = self.ops[self.input(2)]
        return func(self.input(0).img, self.input(1).img)


class Blank(NodeBase):
    title = 'blank img'
    init_inputs = [
        NodeInputBP('dims', dtype=dtypes.Data((100,100))),
        NodeInputBP('from img'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]

    def update_event(self, inp=-1):
        if self.input(1) is not None:
            self.set_output_val(0, CVImage(
                np.zeros(self.input(1).img.shape[:2], dtype='uint8')
            ))
        else:
            self.set_output_val(0, CVImage(
                np.zeros(self.input(0), dtype='uint8')
            ))


class AdjustBrightness(OpenCVNodeBase):
    """Changes the brightness of an image"""
    title = 'Adjust Brightness'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('alpha', dtype=dtypes.Data()),
        NodeInputBP('beta', dtype=dtypes.Data()),
    ]

    def get_img(self):
        return cv2.convertScaleAbs(
            src=self.input(0).img,
            alpha=self.input(1),
            beta=self.input(2)
        )


class Blur(OpenCVNodeBase):
    title = 'Blur'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('ksize', dtype=dtypes.Data((3, 3))),
    ]

    def get_img(self):
        return cv2.blur(
            src=self.input(0).img,
            ksize=self.input(1),
        )


class GaussianBlur(OpenCVNodeBase):
    title = 'Gaussian Blur'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('ksize', dtype=dtypes.Data((3, 3))),
    ]

    def get_img(self):
        return cv2.GaussianBlur(
            src=self.input(0).img,
            ksize=self.input(1),
        )


class BlurMedian(OpenCVNodeBase):
    """Performs a median blur on an img"""
    title = 'Blur Median'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('ksize', dtype=dtypes.Data(3)),
    ]

    def get_img(self):
        return cv2.medianBlur(src=self.input(0).img, ksize=self.input(1))


class Circle(OpenCVNodeBase):
    title = 'Circle'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('center', dtype=dtypes.Data((100, 100))),
        NodeInputBP('radius', dtype=dtypes.Data(100)),
        NodeInputBP('color', dtype=dtypes.Data((255, 255, 255))),
        NodeInputBP('strokeW', dtype=dtypes.Data(-1)),
    ]

    def get_img(self):
        return cv2.circle(
            img=self.input(0).img.copy(),
            center=self.input(1),
            radius=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class ArrowedLine(OpenCVNodeBase):
    title = 'Arrowed liked'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('pt1', dtype=dtypes.Data((100, 100))),
        NodeInputBP('pt2', dtype=dtypes.Data((500, 500))),
        NodeInputBP('color', dtype=dtypes.Data((255, 255, 255))),
        NodeInputBP('strokeW', dtype=dtypes.Data(5)),
    ]

    def get_img(self):
        return cv2.arrowedLine(
            img=self.input(0).img.copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4)
        )


class Line(OpenCVNodeBase):
    title = 'Line'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('pt1', dtype=dtypes.Data((100, 100))),
        NodeInputBP('pt2', dtype=dtypes.Data((500, 500))),
        NodeInputBP('color', dtype=dtypes.Data((255, 255, 255))),
        NodeInputBP('strokeW', dtype=dtypes.Data(5)),
    ]

    def get_img(self):
        return cv2.line(
            img=self.input(0).img.copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class Rectangle(OpenCVNodeBase):
    title = 'Rectangle'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('pt1', dtype=dtypes.Data((0, 0))),
        NodeInputBP('pt2', dtype=dtypes.Data((100, 100))),
        NodeInputBP('color', dtype=dtypes.Data((255, 255, 255))),
        NodeInputBP('strokeW', dtype=dtypes.Data(-1)),
    ]

    def get_img(self):
        return cv2.rectangle(
            img=self.input(0).img.copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class PutText(OpenCVNodeBase):
    font_faces = {
        'italic': cv2.FONT_ITALIC,
        'hershey plain': cv2.FONT_HERSHEY_PLAIN,
        'hershey simplex': cv2.FONT_HERSHEY_SIMPLEX,
        'hershey duplex': cv2.FONT_HERSHEY_DUPLEX,
        'hershey triplex': cv2.FONT_HERSHEY_TRIPLEX,
        'hershey complex': cv2.FONT_HERSHEY_COMPLEX,
        'hershey complex small': cv2.FONT_HERSHEY_COMPLEX_SMALL,
        'hershey script simplex': cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        'hershey script complex': cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    }

    title = 'put text'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('text', dtype=dtypes.String('')),
        NodeInputBP('org', dtype=dtypes.Data((100, 100))),
        NodeInputBP('font face', dtype=dtypes.Choice(default='hershey triplex', items=list(font_faces.keys()))),
        NodeInputBP('font scale', dtype=dtypes.Float(1.0)),
        NodeInputBP('color', dtype=dtypes.Data((255, 255, 255))),
        NodeInputBP('strokeW', dtype=dtypes.Data(2)),
    ]

    def get_img(self):
        return cv2.putText(
            img=self.input(0).img.copy(),
            text=self.input(1),
            org=self.input(2),
            fontFace=self.font_faces[self.input(3)],
            fontScale=self.input(4),
            color=self.input(5),
            thickness=self.input(6),
        )


class BilateralFilter(OpenCVNodeBase):
    title = 'Biliteral Filter'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('diameter', dtype=dtypes.Data(5)),
        NodeInputBP('sigma color', dtype=dtypes.Data(15)),
        NodeInputBP('sigma space', dtype=dtypes.Data(15)),
    ]

    def get_img(self):
        return cv2.bilateralFilter(
            src=self.input(0).img,
            d=self.input(1),
            sigmaColor=self.input(2),
            sigmaSpace=self.input(3)
        )


class BlackHat(OpenCVNodeBase):  # ???
    title = 'Black Hat'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('kernel'),
    ]

    def get_img(self):
        return cv2.morphologyEx(
            src=self.input(0).img,
            op=cv2.MORPH_BLACKHAT,
            kernel=self.input(1)
        )


class CannyEdgeDetection(OpenCVNodeBase):
    title = 'Canny'
    tags = ['edge detection']
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('TS1', dtype=dtypes.Data(100)),
        NodeInputBP('TS2', dtype=dtypes.Data(150)),
    ]

    def get_img(self):
        return cv2.Canny(
            image=self.input(0).img,
            threshold1=self.input(1),
            threshold2=self.input(2)
        )


class HarrisCornerDetection(OpenCVNodeBase):
    title = 'Harris Corner Detection'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('block size', dtype=dtypes.Data()),
        NodeInputBP('ksize', dtype=dtypes.Data()),
        NodeInputBP('k', dtype=dtypes.Data()),
    ]

    def get_img(self):
        return cv2.cornerHarris(
            src=self.input(0).img,
            blockSize=self.input(1),
            ksize=self.input(2),
            k=self.input(3)
        )


class GreySclCircleDetections(OpenCVNodeBase):
    title = 'GreyScl Circle Detection'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('dp', dtype=dtypes.Data()),
        NodeInputBP('min_dist', dtype=dtypes.Data()),
    ]

    def get_img(self):
        img = self.input(0).img.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(
            image=img_gray,
            method=cv2.HOUGH_GRADIENT,
            dp=self.input(1),
            minDist=self.input(2)
        )
        from numpy import uint16, around
        circles = uint16(around(circles))
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

        return img



class Closing(OpenCVNodeBase):
    title = 'Closing'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('kernel', dtype=dtypes.Data()),
    ]

    def get_img(self):
        return cv2.morphologyEx(
            src=self.input(0).img,
            op=cv2.MORPH_CLOSE,
            kernel=self.input(2),
        )


class Dilate(OpenCVNodeBase):
    title = 'Dilate'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('kernel', dtype=dtypes.Data((3, 3))),
        NodeInputBP('iterations', dtype=dtypes.Data(None, size='s')),
    ]

    def get_img(self):
        return cv2.dilate(
            src=self.input(0).img,
            kernel=self.input(1),
            iterations=self.input(2),
        )


class Fourier(OpenCVNodeBase):
    title = 'Fourier'
    init_inputs = [
        NodeInputBP('img'),
    ]

    def get_img(self):
        return cv2.dft(self.input(0).img)


class Erode(OpenCVNodeBase):
    title = 'Erode'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('kernel', dtype=dtypes.Data((3, 3))),
        NodeInputBP('iterations', dtype=dtypes.Data(None, size='s')),
    ]

    def get_img(self):
        return cv2.erode(
            src=self.input(0).img,
            kernel=self.input(1),
            iterations=self.input(2),
        )


class Filter2D(OpenCVNodeBase):
    title = 'Filter 2D'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('ddpepth', dtype=dtypes.Data()),
        NodeInputBP('kernel', dtype=dtypes.Data()),
    ]

    def get_img(self):
        from numpy import ones, float32
        return cv2.filter2D(
            src=self.input(0).img,
            ddepth=self.input(1),
            kernel=ones(self.input(2), float32) / 25
        )


# class RGBToGrayscale(OpenCVNodeBase):
#     title = 'RGB To Greyscale'
#     init_inputs = [
#         NodeInputBP('img'),
#     ]
#
#     def get_img(self):
#         return cv2.cvtColor(
#             src=self.input(0).img,
#             code=cv2.COLOR_BGRA2GRAY,
#         )


# class GreyscaleToRGB(OpenCVNodeBase):
#     title = 'Grayscale to RGB'
#     init_inputs = [
#         NodeInputBP('img'),
#     ]
#
#     def get_img(self):
#         return cv2.cvtColor(
#             src=self.input(0).img,
#             code=cv2.COLOR_BGRA2RGBA
#         )


class ImgBlend(OpenCVNodeBase):
    title = 'Image Blend'
    init_inputs = [
        NodeInputBP('img1'),
        NodeInputBP('alpha'),
        NodeInputBP('img2'),
        NodeInputBP('beta'),
        NodeInputBP('gamma'),
    ]

    def get_img(self):
        return cv2.addWeighted(
            src1=self.input(0).img,
            alpha=self.input(1),
            src2=self.input(2),
            beta=self.input(2),
            gamma=0.0,
        )


class Resize(OpenCVNodeBase):
    title = 'Resize'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('width', dtype=dtypes.Integer(default=500, bounds=(0, 100000))),
        NodeInputBP('height', dtype=dtypes.Integer(default=500, bounds=(0, 100000))),
    ]

    def get_img(self):
        return cv2.resize(
            src=self.input(0).img,
            dsize=(self.input(1), self.input(2)),
        )


class Scale(OpenCVNodeBase):
    title = 'scale'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('scl', dtype=dtypes.Float(1.0)),
    ]

    def get_img(self):
        img = self.input(0).img
        scl = self.input(1)
        dims = (int(img.shape[1] * scl), int(img.shape[0] * scl))
        return cv2.resize(img, dims, interpolation=cv2.INTER_AREA)


class Crop(OpenCVNodeBase):
    title = 'crop'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('slice x', dtype=dtypes.Data((0, 100))),
        NodeInputBP('slice y', dtype=dtypes.Data((0, 100))),
    ]

    def get_img(self):
        img = self.input(0).img
        s_x = self.input(1)
        s_y = self.input(2)
        return img[s_y[0]:s_y[1], s_x[0]:s_x[1]]


class Translate(OpenCVNodeBase):
    title = 'translate'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('x', dtype=dtypes.Data(0)),
        NodeInputBP('y', dtype=dtypes.Data(0)),
    ]

    def get_img(self):
        img = self.input(0).img
        x, y = self.input(1), self.input(2)
        trans_mat = np.float32([[1, 0, x], [0, 1, y]])
        dims = (img.shape[1], img.shape[0])
        return cv2.warpAffine(img, trans_mat, dims)


class Rotate(OpenCVNodeBase):
    title = 'rotate'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('angle', dtype=dtypes.Data(0)),
        NodeInputBP('point', dtype=dtypes.Data(None)),
    ]

    def get_img(self):
        img = self.input(0).img
        height, width = img.shape[:2]

        angle = self.input(1)
        if self.input(2) is None:
            point = (width // 2, height / 2)
        else:
            point = self.input(2)

        rot_mat = cv2.getRotationMatrix2D(point, angle, 1.0)

        return cv2.warpAffine(
            src=img,
            M=rot_mat,
            dsize=(width, height),
        )


class Flip(OpenCVNodeBase):
    title = 'flip'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP(dtype=dtypes.Data(1, size='s'))
    ]

    def get_img(self):
        return cv2.flip(
            src=self.input(0).img,
            flipCode=self.input(1),
        )


class ThresholdAdaptiveGaussian(OpenCVNodeBase):
    title = 'Threshold-Adaptive Gaussian'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('max val', dtype=dtypes.Data(100)),
    ]

    def get_img(self):
        img_gray = cv2.cvtColor(self.input(0).img, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(
            src=img_gray,
            maxValue=self.input(1),
            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType=cv2.THRESH_BINARY,
            blockSize=11,
            C=2,
        )


class ThresholdAdaptiveMean(OpenCVNodeBase):
    title = 'Threshold-Adaptive Mean'
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('max val', dtype=dtypes.Data(100)),
    ]

    def get_img(self):
        img_gray = cv2.cvtColor(self.input(0).img, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(
            src=img_gray,
            maxValue=self.input(1),
            adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
            thresholdType=cv2.THRESH_BINARY,
            blockSize=11,
            C=2,
        )


class ThresholdBase(OpenCVNodeBase):
    init_inputs = [
        NodeInputBP('img'),
        NodeInputBP('thresh', dtype=dtypes.Data(10)),
        NodeInputBP('maxval', dtype=dtypes.Data(100)),
    ]

    thresh_type = None

    def get_img(self):
        img_gray = cv2.cvtColor(self.input(0).img, cv2.COLOR_BGR2GRAY)
        ret, result = cv2.threshold(
            src=img_gray,
            thresh=self.input(1),
            maxval=self.input(2),
            type=self.thresh_type,
        )
        return result


class ThresholdBinary(ThresholdBase):
    title = 'Threshold Binary'
    thresh_type = cv2.THRESH_BINARY


class ThresholdBinaryInverted(ThresholdBase):
    title = 'Threshold Binary Inv'
    thresh_type = cv2.THRESH_BINARY_INV


class ThresholdToZero(ThresholdBase):
    title = 'Threshold To Zero'
    thresh_type = cv2.THRESH_TOZERO


class ThresholdToZeroInverted(ThresholdBase):
    title = 'Threshold To Zero Inv'
    thresh_type = cv2.THRESH_TOZERO_INV


class ThresholdOtsu(ThresholdBase):
    title = 'Threshold Otsu'
    thresh_type = cv2.THRESH_OTSU


class ThresholdMask(ThresholdBase):
    title = 'Threshold Mask'
    thresh_type = cv2.THRESH_MASK


class ThresholdTriangle(ThresholdBase):
    title = 'Threshold Triangle'
    thresh_type = cv2.THRESH_TRIANGLE


class ThresholdTrunc(ThresholdBase):
    title = 'Threshold Trunc'
    thresh_type = cv2.THRESH_TRUNC


# class Histogram(NodeBase):
#     title = 'histogram (matplotlib)'
#     init_inputs = [
#         NodeInputBP('img'),
#     ]
#     main_widget_class = widgets.HistogramView
#     main_widget_pos = 'below ports'
#
#     def update_event(self, inp=-1):
#         hist = cv2.calcHist([self.input(0).img], [0], None, [256], [0,256])
#         if self.session.gui:
#             self.main_widget().show_histogram(hist)


export_nodes(
    ReadImage,
    SaveImg,
    WebcamFeed,
    DisplayImg,
    CvtColor,
    SplitColor,
    Merge,
    Bitwise,
    Blank,
    CustomOpenCV,

    AdjustBrightness,
    Blur,
    GaussianBlur,
    BlurMedian,

    Circle,
    ArrowedLine,
    Line,
    Rectangle,
    PutText,

    BilateralFilter,

    CannyEdgeDetection,
    HarrisCornerDetection,
    GreySclCircleDetections,

    Closing,
    Dilate,
    Fourier,
    Erode,
    Filter2D,

    # RGBToGrayscale,
    # GreyscaleToRGB,

    ImgBlend,

    Resize,
    Scale,
    Crop,
    Translate,
    Rotate,
    Flip,

    ThresholdAdaptiveGaussian,
    ThresholdAdaptiveMean,
    ThresholdBinary,
    ThresholdBinaryInverted,
    ThresholdToZero,
    ThresholdToZeroInverted,
    ThresholdOtsu,
    ThresholdMask,
    ThresholdTriangle,
    ThresholdTrunc,

    # Histogram,
)
