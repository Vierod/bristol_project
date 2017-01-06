import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from scipy import misc
import argparse

#pass files into script
#eg, python image_select_tool.py -i IMAGEFILE

parser = argparse.ArgumentParser(description='')
parser.add_argument('-i','--image', help='Image input file.')
args = parser.parse_args()

image = misc.imread(args.image)

pg.setConfigOptions(imageAxisOrder='row-major')



## create GUI
app = QtGui.QApplication([])
w = pg.GraphicsWindow(size=(1000,800), border=True)
w.setWindowTitle('pyqtgraph example: ROI Examples')

text = """Data Selection From Image.<br>\n
    Drag an ROI or its handles to update the selected image.<br>
    Hold CTRL while dragging to snap to pixel boundaries<br>
    and 15-degree rotation angles.<br>
    To export selected area right click and select export.<br>
    Choose second view area and export as PNG.
    """
w1 = w.addLayout(row=0, col=0)
label1 = w1.addLabel(text, row=0, col=0)
v1a = w1.addViewBox(row=1, col=0, lockAspect=True)
v1b = w1.addViewBox(row=2, col=0, lockAspect=True)
img1a = pg.ImageItem(image)
v1a.addItem(img1a)
img1b = pg.ImageItem()
v1b.addItem(img1b)
v1a.disableAutoRange('xy')
v1b.disableAutoRange('xy')
v1a.autoRange()
v1b.autoRange()

rois = []
rois.append(pg.EllipseROI([60, 10], [30, 20], pen=(3,9)))

def update(roi):
    img1b.setImage(roi.getArrayRegion(image, img1a), levels=(0, image.max()))
    v1b.autoRange()

for roi in rois:
    roi.sigRegionChanged.connect(update)
    v1a.addItem(roi)

update(rois[-1])



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

