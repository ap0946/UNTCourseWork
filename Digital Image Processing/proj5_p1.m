%NAME: Alexis Phu

amp = .5;
targetSize = [512 512];
im1 = makeWave(amp);
%imshow(mat2gray(im1)); //showing the noise by itself

im2 = imread('DIPcover.bmp');
im2 = rgb2gray(im2);
im2 = imresize(im2, targetSize);
%figure; imshow(im2);   //showing the original unaltered image
fft_og = fftshift(fft2(im2));
fft_og_img = log(1+abs(fft_og));
%figure; imshow(mat2gray(fft_og_img));  //showing the original unaltered spectrum

[height, width, c] = size(im2);

im2 = im2double(im2);
im2_noise = im2 + im1;
figure; imshow(im2_noise);

spectrum = fftshift(fft2(im2_noise));
spectrum_img = log(1+abs(spectrum));
figure; imshow(mat2gray(spectrum_img));

notch1 = notch(height, width, 50, 412, 105);
notch2 = notch(height, width, 50, 405, 110);
notch3 = notch(height, width, 50, 472, 42);
notch4 = notch(height, width, 50, 464, 48);
notch5 = notch(height, width, 5, 261, 253);
notch6 = notch(height, width, 100, 500, 15);
notch7 = notch(height, width, 50, 445, 70);
notch8 = notch(height, width, 10, 385, 128);
notch9 = notch(height, width, 5, 491, 24);
notch10 = notch(height, width, 5, 349, 166);
notch11 = notch(height, width, 10, 428, 86);
notch_filter = notch1 .* notch2 .* notch3 .* notch4 .* notch5 .* notch6 .* notch7 .* notch8 .* notch9 .* notch10 .* notch11;
figure; imshow(mat2gray(notch_filter));

filtered = notch_filter .* spectrum;
filtered_img = log(1+abs(filtered));
figure; imshow(mat2gray(filtered_img));

inverse_filtered = ifft2(filtered);
inverse_filtered_img = log(1+abs(inverse_filtered));
figure; imshow(mat2gray(inverse_filtered_img));

%functions
function filter = notch(N, M, d, u, v)
    filter = ones(N, M);
    filter(u, v) = 0;
    for ii=1:N
        for jj=1:M
            if (power(ii-u, 2) + power(jj-v, 2)) <= d
                filter(ii, jj) = 0;
                filter(jj, ii) = 0;
            end
        end
    end
end

function noise = makeWave(A)
    frequency = 12;
    phase = 90;
    amplitude = A;
    [X,Y]=meshgrid(0:0.001:1,0:0.001:1);
    Z = amplitude*sin((2*pi*frequency.*X)+(phase));
    surf(X,Y,Z)
    shading interp
    noise = repmat(Z, 10, 10);
    noise = imrotate(noise, 45, 'crop');
    targetSize = [512, 512];
    window = centerCropWindow2d(size(noise),targetSize);
    noise = imcrop(noise,window);
end