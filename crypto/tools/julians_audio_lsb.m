% LSB .WAV

clear all

nummod =16;

[y, fs]=audioread('space.wav','native');

nbits2=16;

yleft=y(:,1);

% Convert public to filtered bin.

yshift=yleft+1;

str=dec2bin(typecast(int16(yleft),'uint16'));

strnew=str(:,15:16);

strlong='';

for k=1:1:length(strnew)

strlong=strcat(strlong,char(strnew(k,1)),char(strnew(k,2)));

% Convert back to Matlab Vectors

% alldone=(y2rec./(2^15))-1;    



end

print 'Done'