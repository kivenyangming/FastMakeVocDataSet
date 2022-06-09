function [FaceImg,r,c] = FindFace(Img)
fycbcr=rgb2ycbcr(Img);
cr = fycbcr(:,:,3);
cr(cr>140&cr<160)=255;
cr(cr~=255)=0;
ba=bwareaopen(cr,500);
[r,c]=find(ba);
FaceImg=Img(min(r):max(r),min(c):max(c),:);
end