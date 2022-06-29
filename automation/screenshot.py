import cvi2
def take_screenshot():
    videoCaptureObject=cv2.videoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        print(ret)
        cv2.imWrite("NewPicture1.jpg",frame)
        result=False
        videoCaptureObject.release()
        cv2.destroyAllWindows()

take_screenshot()           