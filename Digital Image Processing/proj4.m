%NAME: Alexis Phu

img = imread('building.bmp');
figure;
imshow(mat2gray(img));

[height, width, c] = size(img);
origin_h = height/2;
origin_w = (width+1)/2;
r = power(50,2);
h1 = origin_h - 50;
h2 = origin_h + 50;
w1 = origin_w - 50;
w2 = origin_w + 50;

FFT1 = fftshift(fft2(img));
FFT1_img = log(1+abs(FFT1));
figure; imshow(mat2gray(FFT1_img));

iFFT1 = ifft2(FFT1);
iFFT1_img = log(1+abs(iFFT1));
figure; imshow(mat2gray(iFFT1_img));

FFT2 = conj(FFT1);
FFT2_img = log(1+abs(FFT2));
figure; imshow(mat2gray(FFT2_img));

iFFT2 = ifft2(FFT2);
iFFT2_img = log(1+abs(iFFT2));
figure; imshow(mat2gray(iFFT2_img));

FFT3 = FFT1;
FFT4 = FFT1;

for ii=1:height
    for jj=1:width
        if (power(ii-origin_h, 2) + power(jj-origin_w, 2)) <= r
            FFT3(ii, jj) = 0;
        else
            FFT4(ii, jj) = 0;
        end
    end
end
FFT3_img = log(1+abs(FFT3));
figure; imshow(mat2gray(FFT3_img))

FFT4_img = log(1+abs(FFT4));
figure; imshow(mat2gray(FFT4_img))

iFFT3 = ifft2(FFT3);
iFFT3_img = log(1+abs(iFFT3));
figure; imshow(mat2gray(iFFT3_img));

iFFT4 = ifft2(FFT4);
iFFT4_img = log(1+abs(iFFT4));
figure; imshow(mat2gray(iFFT4_img));
