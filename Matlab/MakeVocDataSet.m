clc
clear
close all 
%%
imaqhwinfo('winvideo');% transfer:winvideo
src = videoinput( 'winvideo', 1 );%Play video and DeviceIDs=1
preview( src );%Display data in default format
% build loop
while 1 == 1
frame = getsnapshot(src); % Get the current screen
ResizeFrame = imresize(frame,[500 750]); %Modify image size
[FaceImg,r,c] = FindFace(ResizeFrame); % Get Face.r.c
ReturnValue = isempty(FaceImg); %empty=1
if ReturnValue == 0
    % ImageName
    ImageNumber = string(100+(100-1)*rand(1,1)); 
    ImageFormat = ".jpg";
    ImageName = strcat(ImageNumber,ImageFormat);
    imwrite(ResizeFrame,strcat('./face/imgs/',ImageName)); %save Picture
    %%TXTinfo
    label = 'Kiven';
    space = {32};
    Xmin = string(min(r));
    Ymin = string(min(c));
    Xmax = string(max(r));
    Ymax = string(max(c));
    TxtInfo = strcat(ImageName,space,label,space,Xmin,space,Ymin,space,Xmax,space,Ymax);
    TxtName = ImageNumber;
    TxtFormat = ".txt";
    writematrix(TxtInfo,strcat('./face/txt/',strcat(TxtName,TxtFormat)))
elseif ReturnValue == 1
    disp("No Face")
end
end