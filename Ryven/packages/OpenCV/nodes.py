from NENV import *
widgets = import_widgets(__file__)


import cv2


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
        NodeInputBP(label='f_path', add_config={'widget name': 'choose file IW', 'widget pos': 'besides'})
    ]
    init_outputs = [
        NodeOutputBP(label='img')
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

    def set_state(self, data):
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
        NodeInputBP(label='img'),
        NodeInputBP(label='path', add_config={'widget name': 'path input', 'widget pos': 'below'}),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.active = False
        self.file_path = ''
        self.special_actions['make executable'] = {'method': self.action_make_executable}

    def view_place_event(self):
        self.input_widget(1).path_chosen.connect(self.path_chosen)

    def path_chosen(self, new_path):
        self.file_path = new_path
        self.update()

    def action_make_executable(self):
        self.create_input(type_='exec', insert=0)
        self.active = True

        del self.special_actions['make executable']
        self.special_actions['make passive'] = {'method': self.action_make_passive}

    def action_make_passive(self):
        self.delete_input(0)
        self.active = False

        del self.special_actions['make passive']
        self.special_actions['make executable'] = {'method': self.action_make_executable}

    def update_event(self, inp=-1):
        if not self.active or (self.active and inp == 0):
            CVImage(cv2.imwrite(self.file_path, self.input(0).img))

    def get_state(self):
        return {'path': self.file_path}

    def set_state(self, data):
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

    def set_state(self, data: dict):
        self.code = data['code']



class DisplayImg(OpenCVNodeBase):
    title = 'Display Image'
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return self.input(0).img


class AdjustBrightness(OpenCVNodeBase):
    """Changes the brightness of an image"""
    title = 'Adjust Brightness'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
    ]

    def get_img(self):
        return cv2.blur(
            src=self.input(0).img,
            ksize=self.input(1),
        )


class GaussianBlur(OpenCVNodeBase):
    title = 'Gaussian Blur'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
    ]

    def get_img(self):
        return cv2.medianBlur(src=self.input(0).img, ksize=self.input(1))


class Circle(OpenCVNodeBase):
    title = 'Circle'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='center'),
        NodeInputBP(label='radius'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='col'),
        NodeInputBP(label='wdth'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
    ]

    def get_img(self):
        return cv2.line(
            src=self.input(0).img.copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class Rectangle(OpenCVNodeBase):
    title = 'Rectangle'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
    ]

    def get_img(self):
        return cv2.rectangle(
            src=self.input(0).img.copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class BilateralFilter(OpenCVNodeBase):
    title = 'Biliteral Filter'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='d'),
        NodeInputBP(label='sigma color'),
        NodeInputBP(label='sigma space'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='kernnel'),
    ]

    def get_img(self):
        return cv2.morphologyEx(
            src=self.input(0).img,
            op=cv2.MORPH_BLACKHAT,
            kernel=self.input(1)
        )


class CannyEdgeDetection(OpenCVNodeBase):
    title = 'Canny'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='threshold1'),
        NodeInputBP(label='threshold2'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='block size'),
        NodeInputBP(label='ksize'),
        NodeInputBP(label='k'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='dp'),
        NodeInputBP(label='min_dist'),
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
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

        return img


class Closing(OpenCVNodeBase):
    title = 'Closing'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        return cv2.dilate(src=self.input(0).img, kernel=self.input(1))


class Fourier(OpenCVNodeBase):
    title = 'Fourier'
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.dft(self.input(0).img)


class Erode(OpenCVNodeBase):
    title = 'Erode'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        return cv2.erode(self.input(0).img, self.input(1))


class Filter2D(OpenCVNodeBase):
    title = 'Filter 2D'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ddpepth'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        from numpy import ones, float32
        return cv2.filter2D(
            srd=self.input(0).img,
            ddepth=self.input(1),
            kernel=ones(self.input(2), float32)/25
        )


class RGBToGrayscale(OpenCVNodeBase):
    title = 'RGB To Greyscale'
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.cvtColor(
            src=self.input(0).img,
            code=cv2.COLOR_BGRA2GRAY,
        )


class GreyscaleToRGB(OpenCVNodeBase):
    title = 'Grayscale to RGB'
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.cvtColor(
            src=self.input(0).img,
            code=cv2.COLOR_BGRA2RGBA
        )


class ImgBlend(OpenCVNodeBase):
    title = 'Image Blend'
    init_inputs = [
        NodeInputBP(label='img1'),
        NodeInputBP(label='alpha'),
        NodeInputBP(label='img2'),
        NodeInputBP(label='beta'),
        NodeInputBP(label='gamma'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='size'),
    ]

    def get_img(self):
        return cv2.resize(
            src=self.input(0).img,
            dsize=self.input(1),
        )


class ThresholdAdaptiveGaussian(OpenCVNodeBase):
    title = 'Threshold-Adaptive Gaussian'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='max val'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='max val'),
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
        NodeInputBP(label='img'),
        NodeInputBP(label='thresh'),
        NodeInputBP(label='maxval'),
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






export_nodes(
    ReadImage,
    SaveImg,
    WebcamFeed,
    DisplayImg,
    CustomOpenCV,

    AdjustBrightness,
    Blur,
    GaussianBlur,
    BlurMedian,

    Circle,
    ArrowedLine,
    Line,
    Rectangle,

    BilateralFilter,

    CannyEdgeDetection,
    HarrisCornerDetection,
    GreySclCircleDetections,

    Closing,
    Dilate,
    Fourier,
    Erode,
    Filter2D,

    RGBToGrayscale,
    GreyscaleToRGB,

    ImgBlend,

    Resize,

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
)
