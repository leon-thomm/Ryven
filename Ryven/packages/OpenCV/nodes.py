from NENV import *
widgets = import_widgets(__file__)


# OpenCVNode_MainWidget,\
# ChooseFileInputWidget,\
# PathInput, \
# WebcamFeedWidget, \
#  = load_from_file(file='widgets.py', caller_file=__file__, components_list=[
#         'OpenCVNode_MainWidget', 'ChooseFileInputWidget', 'PathInput', 'WebcamFeedWidget'
#     ], gui=True)




import cv2



class ReadImage(Node):
    title = 'Read Image'
    doc = 'Reads an image from a file'
    input_widget_classes = {
        'choose file IW': widgets.ChooseFileInputWidget
    }
    init_inputs = [
        NodeInputBP(label='f_path', add_config={'widget name': 'choose file IW', 'widget pos': 'besides'})
    ]
    init_outputs = [
        NodeOutputBP(label='img')
    ]
    color = '#00a6ff'

    def __init__(self, params):
        super().__init__(params)

        self.image_filepath = ''
    
    def view_place_event(self):
        self.input_widget(0).path_chosen.connect(self.path_chosen)
        # self.main_widget_message.connect(self.main_widget().show_path)

    def update_event(self, input_called=-1):
        if self.image_filepath == '':
            return
        
        try:
            self.log_message(
                'loading image, fpath: '+self.image_filepath,
                target='Global'
            )
            self.set_output_val(0, cv2.imread(self.image_filepath))
            # self.main_widget_message.emit(self.image_filepath)
        except Exception as e:
            # self.main_widget_message.emit('couldn\'t open file')
            self.log_message(e, target='Errors')

    def get_state(self):
        data = {'image file path': self.image_filepath}
        return data

    def set_state(self, data):
        self.path_chosen(data['image file path'])
        # self.image_filepath = data['image file path']

    def path_chosen(self, file_path):
        self.image_filepath = file_path
        self.update()



class SaveImg(Node):
    title = 'Save Image'
    doc = ''
    input_widget_classes = {
        'path input': widgets.PathInput
    }
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='path', add_config={'widget name': 'path input', 'widget pos': 'below'}),
    ]
    color = '#00a6ff'

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

    def update_event(self, input_called=-1):
        if not self.active or (self.active and input_called == 0):
            cv2.imwrite(self.file_path, self.input(0))
    
    def get_state(self):
        return {'path': self.file_path}
    
    def set_state(self, data):
        self.file_path = data['path']


# ----------------------------------------------------------------

class WebcamFeed(Node):
    title = 'Webcam Feed'
    doc = ''
    init_inputs = []
    init_outputs = [
        NodeOutputBP(),
    ]
    main_widget_class = widgets.WebcamFeedWidget
    color = '#00a6ff'

    def video_picture_updated(self, frame):
        self.set_output_val(0, frame)

# ----------------------------------------------------------------


class OpenCVNodeBase(Node):
    
    init_outputs = [
        NodeOutputBP()
    ]
    main_widget_class = widgets.OpenCVNode_MainWidget
    main_widget_pos = 'below ports'
    color = '#00a6ff'

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
    
    def update_event(self, input_called=-1):
        new_img = self.get_img()
        
        if self.session.gui:
            self.SIGNALS.new_img.emit(new_img)
        
        self.set_output_val(0, new_img)



class DisplayImg(OpenCVNodeBase):
    title = 'Display Image'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return self.input(0)


class AdjustBrightness(OpenCVNodeBase):
    title = 'Adjust Brightness'
    doc = 'Changes the brightness of an image'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]

    def get_img(self):
        return cv2.convertScaleAbs(
            src=self.input(0), 
            alpha=self.input(1), 
            beta=self.input(2)
        )


class Blur(OpenCVNodeBase):
    title = 'Blur'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
    ]

    def get_img(self):
        return cv2.blur(
            src=self.input(0), 
            ksize=self.input(1),
        )


class GaussianBlur(OpenCVNodeBase):
    title = 'Gaussian Blur'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
    ]

    def get_img(self):
        return cv2.GaussianBlur(
            src=self.input(0), 
            ksize=self.input(1),
        )


class BlurMedian(OpenCVNodeBase):
    title = 'Blur Median'
    doc = 'Performs a median blur on an img'
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ksize'),
    ]

    def get_img(self):
        return cv2.medianBlur(src=self.input(0), ksize=self.input(1))


class Circle(OpenCVNodeBase):
    title = 'Circle'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='center'),
        NodeInputBP(label='radius'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
    ]

    def get_img(self):
        return cv2.circle(
            img=self.input(0).copy(),
            center=self.input(1),
            radius=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class ArrowedLine(OpenCVNodeBase):
    title = 'Arrowed liked'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='col'),
        NodeInputBP(label='wdth'),
    ]

    def get_img(self):
        return cv2.arrowedLine(
            img=self.input(0).copy(), 
            pt1=self.input(1), 
            pt2=self.input(2), 
            color=self.input(3), 
            thickness=self.input(4)
        )


class Line(OpenCVNodeBase):
    title = 'Line'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
    ]

    def get_img(self):
        return cv2.line(
            src=self.input(0).copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class Rectangle(OpenCVNodeBase):
    title = 'Rectangle'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='pt1'),
        NodeInputBP(label='pt2'),
        NodeInputBP(label='color'),
        NodeInputBP(label='thkns'),
    ]

    def get_img(self):
        return cv2.rectangle(
            src=self.input(0).copy(),
            pt1=self.input(1),
            pt2=self.input(2),
            color=self.input(3),
            thickness=self.input(4),
        )


class BilateralFilter(OpenCVNodeBase):
    title = 'Biliteral Filter'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='d'),
        NodeInputBP(label='sigma color'),
        NodeInputBP(label='sigma space'),
    ]

    def get_img(self):
        return cv2.bilateralFilter(
            src=self.input(0), 
            d=self.input(1), 
            sigmaColor=self.input(2),
            sigmaSpace=self.input(3)
        )


class BlackHat(OpenCVNodeBase):  # ???
    title = 'Black Hat'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernnel'),
    ]

    def get_img(self):
        return cv2.morphologyEx(
            src=self.input(0), 
            op=cv2.MORPH_BLACKHAT, 
            kernel=self.input(1)
        )


class CannyEdgeDetection(OpenCVNodeBase):
    title = 'Canny'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='threshold1'),
        NodeInputBP(label='threshold2'),
    ]

    def get_img(self):
        return cv2.Canny(
            image=self.input(0), 
            threshold1=self.input(1), 
            threshold2=self.input(2)
        )


class HarrisCornerDetection(OpenCVNodeBase):
    title = 'Harris Corner Detection'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='block size'),
        NodeInputBP(label='ksize'),
        NodeInputBP(label='k'),
    ]

    def get_img(self):
        return cv2.cornerHarris(
            src=self.input(0), 
            blockSize=self.input(1), 
            ksize=self.input(2), 
            k=self.input(3)
        )


class GreySclCircleDetections(OpenCVNodeBase):
    title = 'GreyScl Circle Detection'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='dp'),
        NodeInputBP(label='min_dist'),
    ]

    def get_img(self):
        
        img = self.input(0).copy()
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
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        return cv2.morphologyEx(
            src=self.input(0), 
            op=cv2.MORPH_CLOSE,
            kernel=self.input(2),
        )


class Dilate(OpenCVNodeBase):
    title = 'Dilate'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        return cv2.dilate(src=self.input(0), kernel=self.input(1))


class Fourier(OpenCVNodeBase):
    title = 'Fourier'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.dft(self.input(0))


class Erode(OpenCVNodeBase):
    title = 'Erode'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        return cv2.erode(self.input(0), self.input(1))


class Filter2D(OpenCVNodeBase):
    title = 'Filter 2D'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='ddpepth'),
        NodeInputBP(label='kernel'),
    ]

    def get_img(self):
        from numpy import ones, float32
        return cv2.filter2D(
            srd=self.input(0), 
            ddepth=self.input(1),
            kernel=ones(self.input(2), float32)/25
        )


class RGBToGrayscale(OpenCVNodeBase):
    title = 'RGB To Greyscale'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.cvtColor(
            src=self.input(0),
            code=cv2.COLOR_BGRA2GRAY,
        )


class GreyscaleToRGB(OpenCVNodeBase):
    title = 'Grayscale to RGB'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
    ]

    def get_img(self):
        return cv2.cvtColor(
            src=self.input(0),
            code=cv2.COLOR_BGRA2RGBA
        )


class ImgBlend(OpenCVNodeBase):
    title = 'Image Blend'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img1'),
        NodeInputBP(label='alpha'),
        NodeInputBP(label='img2'),
        NodeInputBP(label='beta'),
        NodeInputBP(label='gamma'),
    ]

    def get_img(self):
        return cv2.addWeighted(
            src1=self.input(0),
            alpha=self.input(1),
            src2=self.input(2),
            beta=self.input(2),
            gamma=0.0,
        )


class Resize(OpenCVNodeBase):
    title = 'Resize'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='size'),
    ]

    def get_img(self):
        return cv2.resize(
            src=self.input(0),
            dsize=self.input(1),
        )


class ThresholdAdaptiveGaussian(OpenCVNodeBase):
    title = 'Threshold-Adaptive Gaussian'
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='max val'),
    ]

    def get_img(self):
        img_gray = cv2.cvtColor(self.input(0), cv2.COLOR_BGR2GRAY)
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
    doc = ''
    init_inputs = [
        NodeInputBP(label='img'),
        NodeInputBP(label='max val'),
    ]

    def get_img(self):
        img_gray = cv2.cvtColor(self.input(0), cv2.COLOR_BGR2GRAY)
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
        img_gray = cv2.cvtColor(self.input(0), cv2.COLOR_BGR2GRAY)
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
