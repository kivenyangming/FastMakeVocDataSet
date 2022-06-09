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
[FaceImg,r,c] = FindFace(frame); % Get Face.r.c
ReturnValue = isempty(FaceImg); %empty=1
if ReturnValue == 0
    % ImageName
    ResizeFrame = imresize(FaceImg,[100 100]); %Modify image size
    ImageNumber = string(100+(100-1)*rand(1,1)); 
    ImageFormat = ".jpg";
    ImageName = strcat(ImageNumber,ImageFormat);
    imwrite(ResizeFrame,strcat('./face/',ImageName)); %save Picture
elseif ReturnValue == 1
    disp("No Face")
end
end