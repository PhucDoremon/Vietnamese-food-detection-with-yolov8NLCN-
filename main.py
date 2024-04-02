from ultralytics import YOLO

model = YOLO("C:/Users/Tran Thien Phuc/Desktop/nlcn/3epo20banh.pt")


results = model("0",show=True)  # predict realtime with webcam on an image


print("ok",results)
